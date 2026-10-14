"""Bilan du troupeau au robot — moteur de calcul.

Méthode décrite sur https://lesdeuxrecoltes.fr/elevage/suivre-son-troupeau-entre-deux-controles/

Exécuté dans le navigateur du visiteur par l'outil en ligne : aucune donnée
n'est envoyée. Deux sortes d'exports CSV de Lely Horizon sont acceptées :

  - « photo du jour » : les rapports standard d'Horizon, tels que livrés,
    une ligne par vache et pas de colonne de date :
      « Traite – Production journalière par vache » (lait, taux, cellules)
      « Traite – Données de traites » (traites, refus, échecs),
    l'un, l'autre ou les deux, fusionnés par numéro d'animal ;
  - « historique » : une copie enrichie du rapport de production
    journalière, avec la colonne « Date de production », sur les 3 à 5
    derniers jours (une ligne par vache et par jour).

Principes de calcul :
  - le troupeau étudié = les vaches présentes le dernier jour de l'export ;
  - en historique, chaque indicateur d'une vache est la moyenne de ses valeurs
    sur la période, cases vides ignorées (une case vide n'est jamais comptée
    comme un zéro) ; en photo du jour, c'est la valeur calculée par Horizon ;
  - les taux et les cellules du troupeau sont pondérés par le lait, comme un
    lait de tank ; les autres moyennes sont des moyennes par vache ;
  - TB et TP des premiers jours de lactation (colostrum, lait de transition)
    ne sont pas pris en compte : ils déclencheraient de fausses alertes ;
  - concentré : la quantité programmée, comme dans la méthode ; la quantité
    consommée seulement si l'export ne donne pas la programmée ;
  - TB, TP et cellules sont des indications mesurées au robot, pas des
    analyses de laboratoire ;
  - niveau d'étable estimé : moyenne des vaches de (lait moyen de la période
    x 305 x coefficient de stade x coefficient de rang) — une projection
    d'ordre de grandeur, pas le niveau d'étable officiel ;
  - alerte cellules si la moyenne de la période OU la dernière indication
    dépasse le seuil : une moyenne seule noierait une mammite récente.
"""
import csv
import io
import json
import re
import unicodedata
from datetime import date, datetime

PARAMETRES = {
    "cetose_ratio": 1.5,      # TB/TP au-dessus : suspicion de cétose (début de lactation)
    "cetose_jel": 100,        # ... appliqué jusqu'à ce stade (jours de lactation)
    "acidose_ratio": 1.0,     # TB/TP en dessous (TB < TP) : signal d'acidose à vérifier
    "cellules_saine": 300,    # milliers de cellules/ml : en dessous, mamelle considérée saine
    "cellules_infectee": 800, # au-dessus, mamelle considérée infectée
    "stades": [100, 200],     # bornes des stades de lactation (jours)
    "taux_jel_min": 5,        # TB et TP non interprétés avant ce stade : colostrum et
                              # lait de transition (TB/TP faussés juste après le vêlage)
    # Niveau d'étable estimé : lait du jour x 305, corrigé du stade et du rang.
    # Projection d'ordre de grandeur, pas le niveau d'étable du contrôle laitier.
    "niveau_stade": [[60, 1.15], [100, 1.08], [200, 1.03], [305, 0.98], [None, 0.88]],
    "niveau_rang": {"1": 1.12, "2": 1.04, "autres": 1.0},
}


def _projection(lait, jel, rang, p):
    """Lait du jour projeté sur une lactation de 305 jours."""
    if lait is None or jel is None:
        return None
    fs = next(c for borne, c in p["niveau_stade"] if borne is None or jel < borne)
    r = p["niveau_rang"]
    fr = r["1"] if rang == 1 else r["2"] if rang == 2 else r["autres"]
    return lait * 305 * fs * fr


class ErreurExport(Exception):
    """Export illisible ou incomplet : message destiné à l'éleveur."""


def _norm(t):
    t = str(t).replace("’", "'").replace("‘", "'")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return " ".join(t.lower().replace(".", " ").replace("°", " ").split())


COLONNES = {
    # clé: (intitulés acceptés, par ordre de préférence)
    "vache": ["N° d'animal", "No d'animal", "Numéro d'animal"],
    "date": ["Date de production"],
    "lait": ["Production journalière"],
    "jel": ["Jours de lactation"],
    "rang": ["N° de Lactation", "Numéro de lactation", "N°. lac."],
    "mg": ["MG indication"],
    "mp": ["MP indication"],
    "cell": ["Indication Cellules"],
    # concentré : la quantité programmée ; la consommée seulement à défaut
    "conc": ["Alim. total programmé", "Alim total programmé", "Total programmé aujourd'hui",
             "Consommation totale réelle"],
    "rum": ["Minutes de rumination"],
    "ing": ["Minutes d'ingestion totales"],
    "poids": ["Poids"],
    # robot : le compte du jour (historique), sinon la moyenne calculée par Horizon
    "traites": ["Nbre de traites", "Traites moyennes", "Moy. Traites"],
    "refus": ["Nbre de refus", "Refus moyens", "Moy. Refus"],
    "echecs": ["Nbre d'échecs", "Echecs moyens", "Moy. Echecs"],
    "etat": ["Etat reprod."],
}
OBLIGATOIRES = ["vache", "lait", "jel"]
CONC_REEL = _norm("Consommation totale réelle")


def _lire(texte, nom=""):
    """Lit un export : lignes, colonnes reconnues, et sorte d'export."""
    texte = (texte or "").lstrip("﻿")
    premiere = texte.splitlines()[0] if texte.strip() else ""
    sep = ";" if premiere.count(";") > premiere.count(",") else ","
    lignes = list(csv.reader(io.StringIO(texte), delimiter=sep))
    for i, ligne in enumerate(lignes[:5]):
        entetes = [_norm(c) for c in ligne]
        index, libelles = {}, {}
        for cle, noms in COLONNES.items():
            for n in noms:                       # premier intitulé présent = préféré
                if _norm(n) in entetes:
                    index[cle] = entetes.index(_norm(n))
                    libelles[cle] = entetes[index[cle]]
                    break
        if "vache" not in index:
            continue
        historique = "date" in index
        manquantes = [COLONNES[k][0] for k in OBLIGATOIRES if k not in index]
        if manquantes:
            raise ErreurExport(
                f"Fichier « {nom} » : colonne(s) introuvable(s) : "
                + ", ".join(f"« {m} »" for m in manquantes)
                + ". Utilisez le rapport « Traite – Production journalière par vache » "
                  "ou « Traite – Données de traites » d'Horizon, exporté en CSV.")
        sortie = []
        for ligne in lignes[i + 1:]:
            if not ligne or index["vache"] >= len(ligne) or not ligne[index["vache"]].strip():
                continue
            if ligne[index["vache"]].strip().upper() in ("AVG", "SUM", "MOY", "SOM", "TOTAL"):
                continue
            sortie.append({k: (ligne[j].strip() if j < len(ligne) else "") for k, j in index.items()})
        if not historique:
            vues = [_vache(r["vache"]) for r in sortie]
            if len(vues) != len(set(vues)):
                raise ErreurExport(
                    f"Fichier « {nom} » : plusieurs lignes pour une même vache, sans colonne "
                    "« Date de production ». Ajoutez cette colonne au rapport dans Horizon, "
                    "ou exportez le rapport standard, qui donne une ligne par vache.")
        return {"nom": nom, "lignes": sortie, "colonnes": set(index), "historique": historique,
                "conc_reel": libelles.get("conc") == CONC_REEL}
    raise ErreurExport(f"Fichier « {nom} » : colonne « N° d'animal » introuvable. Vérifiez qu'il "
                       "s'agit d'un export CSV de Lely Horizon (rapport « Traite – Production "
                       "journalière par vache » ou « Traite – Données de traites »).")


def _nombre(v):
    v = (v or "").replace(",", ".").replace(" ", "").replace(" ", "").strip()
    try:
        return float(v) if v else None
    except ValueError:
        return None


def _date(v):
    v = (v or "").strip()[:10]
    for f in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y"):
        try:
            return datetime.strptime(v, f).date()
        except ValueError:
            pass
    return None


def _date_du_nom(nom):
    """Date d'export lue dans le nom de fichier d'Horizon (…-14_10_2026_12_06_28.csv)."""
    m = re.search(r"(\d{1,2})[-_. ](\d{1,2})[-_. ](\d{4})", nom or "")
    if m:
        try:
            return date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        except ValueError:
            return None
    return None


def _vache(v):
    try:
        return str(int(float(v)))
    except ValueError:
        return v.strip()


def _moy(vals):
    vals = [v for v in vals if v is not None]
    return sum(vals) / len(vals) if vals else None


def _pond(paires):
    """Moyenne de valeurs pondérée par le lait : [(valeur, lait), ...]."""
    paires = [(v, l) for v, l in paires if v is not None and l]
    tot = sum(l for _, l in paires)
    return sum(v * l for v, l in paires) / tot if tot else None


def _r(v, n=1):
    return None if v is None else round(v, n)


def _assembler(exports):
    """Choisit et fusionne les exports : (parvache {vache: {jour: ligne}}, colonnes, infos)."""
    hist = [e for e in exports if e["historique"]]
    if hist:
        retenus = hist[:1]                       # l'historique se suffit à lui-même
        e = retenus[0]
        parvache = {}
        for r in e["lignes"]:
            d = _date(r["date"])
            if d is None:
                continue
            parvache.setdefault(_vache(r["vache"]), {})[d] = r   # un doublon : la dernière ligne l'emporte
        return parvache, set(e["colonnes"]), {
            "mode": "historique", "retenus": [e["nom"]], "conc_reel": e["conc_reel"],
            "ignores": [x["nom"] for x in exports if x is not e], "date_photo": None}

    # Photo du jour : fusion par numéro d'animal, le fichier le plus complet d'abord.
    exports = sorted(exports, key=lambda e: -len(e["colonnes"]))
    fusion, colonnes = {}, set()
    for e in exports:
        colonnes |= e["colonnes"]
        for r in e["lignes"]:
            f = fusion.setdefault(_vache(r["vache"]), {})
            for k, v in r.items():
                if v and not f.get(k):
                    f[k] = v
    # Concentré : un export qui donne la quantité programmée l'emporte.
    prog = next((e for e in exports if "conc" in e["colonnes"] and not e["conc_reel"]), None)
    if prog:
        for r in prog["lignes"]:
            fusion[_vache(r["vache"])]["conc"] = r["conc"]
    jour = next((d for d in (_date_du_nom(e["nom"]) for e in exports) if d), None)
    cle = jour or date.min
    parvache = {v: {cle: r} for v, r in fusion.items()}
    return parvache, colonnes, {
        "mode": "photo", "retenus": [e["nom"] for e in exports], "ignores": [],
        "conc_reel": not prog and any("conc" in e["colonnes"] for e in exports), "date_photo": jour}


def bilan_fichiers(fichiers, parametres=None):
    """fichiers : [{"nom": ..., "texte": ...}, ...] ; un ou plusieurs exports."""
    p = dict(PARAMETRES)
    p.update({k: v for k, v in (parametres or {}).items() if v is not None})
    if not fichiers:
        raise ErreurExport("Aucun fichier déposé.")
    exports = [_lire(f.get("texte", ""), f.get("nom", "")) for f in fichiers]
    parvache, colonnes, infos = _assembler(exports)

    if not parvache:
        raise ErreurExport("L'export ne contient aucune ligne exploitable.")
    dates = sorted({d for jours in parvache.values() for d in jours})
    jour_j = dates[-1]

    vaches = []
    for v, jours in parvache.items():
        if jour_j not in jours:
            continue                      # vache sortie ou tarie avant le dernier jour
        dern = jours[jour_j]
        serie = [jours[d] for d in sorted(jours)]
        m = lambda k, s=serie: _moy([_nombre(x.get(k)) for x in s]) if k in colonnes else None
        # TB et TP : jours de colostrum et de lait de transition écartés
        apres = [x for x in serie
                 if _nombre(x.get("jel")) is None or _nombre(x.get("jel")) >= p["taux_jel_min"]]
        f = {"vache": v, "jel": _nombre(dern["jel"]), "rang": _nombre(dern.get("rang")),
             "etat": dern.get("etat", ""), "jours": len(serie),
             "lait": m("lait"), "mg": m("mg", apres), "mp": m("mp", apres), "cell": m("cell"), "conc": m("conc"),
             "rum": m("rum"), "ing": m("ing"), "traites": m("traites"), "refus": m("refus"),
             "echecs": m("echecs")}
        pesees = [(d, _nombre(jours[d].get("poids"))) for d in sorted(jours)] if "poids" in colonnes else []
        pesees = [(d, x) for d, x in pesees if x]
        f["poids_var"] = (pesees[-1][1] - pesees[0][1]) if len(pesees) >= 2 else None
        cells = [_nombre(x.get("cell")) for x in serie] if "cell" in colonnes else []
        cells = [c for c in cells if c is not None]
        f["cell_dern"] = cells[-1] if cells else None   # dernière indication : une hausse récente
        f["tb"] = f["mg"] * 10 if f["mg"] else None      # % -> g/kg
        f["tp"] = f["mp"] * 10 if f["mp"] else None
        f["ratio"] = f["tb"] / f["tp"] if f["tb"] and f["tp"] else None
        f["lait_conc"] = f["lait"] / f["conc"] if f["lait"] and f["conc"] else None
        alertes = []
        if f["ratio"] is not None and f["jel"] is not None:
            if f["jel"] <= p["cetose_jel"] and f["ratio"] > p["cetose_ratio"]:
                alertes.append("cetose")
            if f["ratio"] < p["acidose_ratio"]:
                alertes.append("acidose")
        if any(c is not None and c > p["cellules_infectee"] for c in (f["cell"], f["cell_dern"])):
            alertes.append("cellules")
        f["alertes"] = alertes
        vaches.append(f)
    if not vaches:
        raise ErreurExport("Aucune vache présente le dernier jour de l'export.")

    col = lambda k: [x[k] for x in vaches]

    def groupe(vs):
        if not vs:
            return None
        tb = _pond([(x["tb"], x["lait"]) for x in vs])
        tp = _pond([(x["tp"], x["lait"]) for x in vs])
        return {
            "n": len(vs),
            "lait": _r(_moy([x["lait"] for x in vs])),
            "tb": _r(tb), "tp": _r(tp),
            "ecart": _r(tb - tp) if tb and tp else None,
            "ratio": _r(tb / tp, 2) if tb and tp else None,
            "cell": _r(_pond([(x["cell"], x["lait"]) for x in vs]), 0),
            "rum": _r(_moy([x["rum"] for x in vs]), 0),
            "ing": _r(_moy([x["ing"] for x in vs]), 0),
            "lait_conc": _r(_moy([x["lait_conc"] for x in vs]), 2),
            "poids_var": _r(_moy([x["poids_var"] for x in vs])),
            "poids_n": sum(1 for x in vs if x["poids_var"] is not None),
        }

    b1, b2 = p["stades"]
    stade = lambda x: None if x["jel"] is None else (0 if x["jel"] <= b1 else 1 if x["jel"] <= b2 else 2)
    stades = [groupe([x for x in vaches if stade(x) == s]) for s in range(3)]
    jeunes = [x for x in vaches if x["jel"] is not None and x["jel"] <= b1]
    debut = {"primi": groupe([x for x in jeunes if x["rang"] == 1]),
             "multi": groupe([x for x in jeunes if x["rang"] and x["rang"] >= 2])}

    avec_cell = [x for x in vaches if x["cell"] is not None]
    rangs = [x["rang"] for x in vaches if x["rang"]]
    troupeau = groupe(vaches)
    troupeau.update({
        "lait_total": _r(sum(x["lait"] for x in vaches if x["lait"]), 0),
        "niveau_estime": _r(_moy([_projection(x["lait"], x["jel"], x["rang"] or 1, p) for x in vaches]), 0),
        "jel": _r(_moy(col("jel")), 0),
        "rang": _r(_moy(rangs)),
        "primipares_pct": _r(100 * sum(1 for r in rangs if r == 1) / len(rangs), 0) if rangs else None,
        "traites": _r(_moy(col("traites"))),
        "refus": _r(_moy(col("refus"))),
        "echecs": _r(_moy(col("echecs")), 2),
        "cell_n": len(avec_cell),
        "cell_saine_pct": _r(100 * sum(1 for x in avec_cell if x["cell"] < p["cellules_saine"]) / len(avec_cell), 0) if avec_cell else None,
        "cell_infectee_pct": _r(100 * sum(1 for x in avec_cell if x["cell"] > p["cellules_infectee"]) / len(avec_cell), 0) if avec_cell else None,
        "taux_n": sum(1 for x in vaches if x["ratio"] is not None),
    })

    def cle(x):
        try:
            return (0, int(x["vache"]))
        except ValueError:
            return (1, x["vache"])
    vaches.sort(key=cle)
    for x in vaches:
        for k in ("lait", "tb", "tp", "conc", "poids_var"):
            x[k] = _r(x[k])
        for k in ("cell", "cell_dern", "rum", "ing"):
            x[k] = _r(x[k], 0)
        for k in ("ratio", "lait_conc", "traites", "refus", "echecs"):
            x[k] = _r(x[k], 2)
        x.pop("mg"), x.pop("mp")

    # Ce qu'un rapport standard de plus apporterait au bilan.
    conseils = []
    if infos["mode"] == "photo":
        if not {"mg", "mp", "cell"} & colonnes:
            conseils.append("Ajoutez l'export « Traite – Production journalière par vache » "
                            "pour les taux et les cellules.")
        if not {"traites", "refus", "echecs"} & colonnes:
            conseils.append("Ajoutez l'export « Traite – Données de traites » pour les traites, "
                            "refus et échecs du robot.")

    photo = infos["mode"] == "photo"
    iso = lambda d: None if d is None or d == date.min else d.isoformat()
    return {
        "mode": infos["mode"],
        "debut": iso(dates[0]), "fin": iso(jour_j), "nb_jours": None if photo else len(dates),
        "fichiers": infos["retenus"], "ignores": infos["ignores"], "conseils": conseils,
        "concentre": "consommé" if infos["conc_reel"] else "programmé",
        "colonnes": sorted(colonnes), "parametres": p,
        "troupeau": troupeau, "stades": stades, "debut_lactation": debut,
        "alertes": {k: [x["vache"] for x in vaches if k in x["alertes"]] for k in ("cetose", "acidose", "cellules")},
        "vaches": vaches,
    }


def bilan(texte, parametres=None):
    """Un seul export (compatibilité)."""
    return bilan_fichiers([{"nom": "", "texte": texte}], parametres)


def _json(fn):
    try:
        return json.dumps(fn())
    except ErreurExport as e:
        return json.dumps({"erreur": str(e)})


def bilan_json(texte, parametres_json):
    """Point d'entrée historique de l'outil en ligne : un seul fichier."""
    return _json(lambda: bilan(texte or "", json.loads(parametres_json or "{}")))


def bilan_fichiers_json(fichiers_json, parametres_json):
    """Point d'entrée de l'outil en ligne : [{"nom", "texte"}, ...] en JSON."""
    return _json(lambda: bilan_fichiers(json.loads(fichiers_json or "[]"),
                                        json.loads(parametres_json or "{}")))
