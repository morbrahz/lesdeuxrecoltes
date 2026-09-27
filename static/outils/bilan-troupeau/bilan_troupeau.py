"""Bilan du troupeau au robot — moteur de calcul.

Méthode décrite sur https://lesdeuxrecoltes.fr/elevage/suivre-son-troupeau-entre-deux-controles/

Exécuté dans le navigateur du visiteur par l'outil en ligne : aucune donnée
n'est envoyée. Entrée : l'export CSV du rapport « Production journalière par
vache » de Lely Horizon, idéalement sur les 3 à 5 derniers jours.

Principes de calcul :
  - le troupeau étudié = les vaches présentes le dernier jour de l'export ;
  - chaque indicateur d'une vache est la moyenne de ses valeurs sur la période,
    cases vides ignorées (une case vide n'est jamais comptée comme un zéro) ;
  - les taux et les cellules du troupeau sont pondérés par le lait, comme un
    lait de tank ; les autres moyennes sont des moyennes par vache ;
  - TB, TP et cellules sont des indications mesurées au robot, pas des
    analyses de laboratoire ;
  - alerte cellules si la moyenne de la période OU la dernière indication
    dépasse le seuil : une moyenne seule noierait une mammite récente.
"""
import csv
import io
import json
import math
import unicodedata
from datetime import datetime

PARAMETRES = {
    "cetose_ratio": 1.5,      # TB/TP au-dessus : suspicion de cétose (début de lactation)
    "cetose_jel": 100,        # ... appliqué jusqu'à ce stade (jours de lactation)
    "acidose_ratio": 1.0,     # TB/TP en dessous (TB < TP) : signal d'acidose à vérifier
    "cellules_saine": 300,    # milliers de cellules/ml : en dessous, mamelle considérée saine
    "cellules_infectee": 800, # au-dessus, mamelle considérée infectée
    "stades": [100, 200],     # bornes des stades de lactation (jours)
}


class ErreurExport(Exception):
    """Export illisible ou incomplet : message destiné à l'éleveur."""


def _norm(t):
    t = unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode()
    return " ".join(t.lower().replace(".", " ").replace("°", " ").split())


COLONNES = {
    # clé: (intitulés acceptés, obligatoire)
    "vache": (["N° d'animal", "No d'animal", "Numéro d'animal"], True),
    "date": (["Date de production"], True),
    "lait": (["Production journalière"], True),
    "jel": (["Jours de lactation"], True),
    "rang": (["N° de Lactation", "Numéro de lactation"], False),
    "mg": (["MG indication"], False),
    "mp": (["MP indication"], False),
    "cell": (["Indication Cellules"], False),
    "conc": (["Alim. total programmé", "Alim total programmé"], False),
    "rum": (["Minutes de rumination"], False),
    "ing": (["Minutes d'ingestion totales"], False),
    "poids": (["Poids"], False),
    "traites": (["Nbre de traites"], False),
    "refus": (["Nbre de refus"], False),
    "echecs": (["Nbre d'échecs"], False),
    "etat": (["Etat reprod."], False),
}


def _lire(texte):
    texte = texte.lstrip("﻿")
    premiere = texte.splitlines()[0] if texte.strip() else ""
    sep = ";" if premiere.count(";") > premiere.count(",") else ","
    lignes = list(csv.reader(io.StringIO(texte), delimiter=sep))
    for i, ligne in enumerate(lignes[:5]):
        entetes = [_norm(c) for c in ligne]
        index = {}
        for cle, (noms, _) in COLONNES.items():
            voulus = {_norm(n) for n in noms}
            for j, e in enumerate(entetes):
                if e in voulus:
                    index[cle] = j
                    break
        if "vache" in index:
            manquantes = [COLONNES[k][0][0] for k, (_, obl) in COLONNES.items() if obl and k not in index]
            if manquantes:
                raise ErreurExport(
                    "Export « Production journalière par vache » : colonne(s) introuvable(s) : "
                    + ", ".join(f"« {m} »" for m in manquantes)
                    + ". Ajoutez-les au rapport dans Lely Horizon, puis exportez à nouveau.")
            sortie = []
            for ligne in lignes[i + 1:]:
                if not ligne or not ligne[index["vache"]].strip():
                    continue
                if ligne[index["vache"]].strip().upper() in ("AVG", "SUM", "MOY", "TOTAL"):
                    continue
                sortie.append({k: (ligne[j].strip() if j < len(ligne) else "") for k, j in index.items()})
            return sortie, sorted(index)
    raise ErreurExport("Colonne « N° d'animal » introuvable : vérifiez qu'il s'agit bien de l'export "
                       "« Production journalière par vache », au format CSV.")


def _nombre(v):
    v = (v or "").replace(",", ".").replace(" ", "").strip()
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


def bilan(texte, parametres=None):
    p = dict(PARAMETRES)
    p.update({k: v for k, v in (parametres or {}).items() if v is not None})
    lignes, colonnes = _lire(texte)

    parvache = {}
    for r in lignes:
        d = _date(r["date"])
        if d is None:
            continue
        parvache.setdefault(_vache(r["vache"]), {})[d] = r   # un doublon : la dernière ligne l'emporte
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
        m = lambda k: _moy([_nombre(x.get(k)) for x in serie]) if k in colonnes else None
        f = {"vache": v, "jel": _nombre(dern["jel"]), "rang": _nombre(dern.get("rang")),
             "etat": dern.get("etat", ""), "jours": len(serie),
             "lait": m("lait"), "mg": m("mg"), "mp": m("mp"), "cell": m("cell"), "conc": m("conc"),
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

    n = len(vaches)
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
    return {
        "debut": dates[0].isoformat(), "fin": jour_j.isoformat(), "nb_jours": len(dates),
        "colonnes": colonnes, "parametres": p,
        "troupeau": troupeau, "stades": stades, "debut_lactation": debut,
        "alertes": {k: [x["vache"] for x in vaches if k in x["alertes"]] for k in ("cetose", "acidose", "cellules")},
        "vaches": vaches,
    }


def bilan_json(texte, parametres_json):
    """Point d'entrée de l'outil en ligne."""
    try:
        return json.dumps(bilan(texte or "", json.loads(parametres_json or "{}")))
    except ErreurExport as e:
        return json.dumps({"erreur": str(e)})
