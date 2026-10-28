"""Quand arrêter d'inséminer une vache — moteur de calcul.

Méthode décrite sur https://lesdeuxrecoltes.fr/elevage/quand-arreter-d-inseminer-une-vache/

Ce fichier est exécuté tel quel par l'outil en ligne, dans le navigateur du
visiteur : aucune donnée n'est envoyée nulle part. Il fonctionne aussi en
local, sans rien installer d'autre que Python :

    python regle_reinsemination.py export.csv [AAAA-MM-JJ] [jours exclus séparés par des virgules]

Export attendu (Lely Horizon) : la copie enrichie du rapport « Production
journalière par vache », sur au moins 6 mois. Colonnes lues : N° d'animal,
Date de production, Production journalière, Etat reprod., Jours de lactation,
N° de Lactation ; Nbre de traites et Indication Cellules si elles sont
présentes (alertes de cause passagère).

Règle :
  - la position d'une vache est sa production rapportée à la courbe de son
    rang (primipares, rangs 2, rangs 3 et plus), au même stade de lactation et
    à la même date, moyennée sur sa lactation en cours (7 à 305 jours) ;
  - sous 90 % de la courbe pour une primipare, 80 % pour une vache de rang 2
    ou plus : ne plus inséminer, après avoir écarté une cause passagère ;
  - plus d'insémination après 300 jours de lactation, sans nombre maximum
    d'inséminations ;
  - pas de décision avant 60 jours de lactation ni avec moins de 30 jours de
    données dans la lactation ;
  - les vaches gestantes et celles déjà marquées « ne pas inséminer » ne sont
    pas classées.

Calcul : régression du logarithme du lait sur une courbe de lactation par
rang (B-spline cubique, 5 degrés de liberté, interaction avec le rang) et un
effet par jour (saison, ration, robot), estimée par moindres carrés après
retrait des moyennes journalières ; la position d'une vache est
l'exponentielle de la moyenne de ses résidus. Rapports entre rangs : même
modèle avec une courbe commune (6 degrés de liberté) et un décalage par rang,
intervalle de confiance à 95 % robuste par vache.
"""
import csv
import io
import json
import math
import sys
import unicodedata
from datetime import date, datetime, timedelta

PARAMETRES = {
    "seuil_p1": 0.90,          # primipares : part de la courbe des primipares
    "seuil_r2": 0.80,          # rang 2 : part de la courbe des rangs 2
    "seuil_r3": 0.80,          # rang 3 et plus : part de la courbe des rangs 3+
    "jel_min_decision": 60,    # pas de décision avant
    "jours_min": 30,           # jours de données exigés dans la lactation en cours
    "jel_max_ia": 300,         # plus d'insémination après ; pas de plafond du nombre d'IA
    "marge_limite": 0.02,      # « à la limite » : moins de 2 points au-dessus du seuil
    "traites_min": 2.0,        # alerte si moins de traites par jour (14 derniers jours)
    "cellules_max": 300,       # alerte si une indication dépasse (milliers/ml, 14 derniers jours)
    "ancrage": None,           # 'AAAA-MM-JJ' : dernier jour complet ; sinon détecté
    "exclus": [],              # jours perturbés à écarter ('AAAA-MM-JJ')
}
JOURS_FENETRE_CONSEILLES = 180
LACTATIONS_MIN_PAR_RANG = 3
RANGS = ("P1", "R2", "R3+")
STATUTS_EXCLUS = {"gestante", "ne pas inseminer"}
STATUTS_CONNUS = {"a inseminer", "chaleur ouverte", "inseminee", "gestante", "ne pas inseminer"}


class ErreurExport(Exception):
    """Export illisible ou incomplet : message destiné à l'éleveur."""


# ---------- lecture de l'export ----------

def _norm(texte):
    t = unicodedata.normalize("NFKD", str(texte)).encode("ascii", "ignore").decode()
    return " ".join(t.lower().replace(".", " ").replace("°", " ").replace("'", " ").split())


COLONNES = {
    "vache": ["N° d'animal", "No d'animal", "Numéro d'animal"],
    "date": ["Date de production"],
    "lait": ["Production journalière", "Production journaliere"],
    "repro": ["Etat reprod.", "État reprod.", "Etat de reproduction"],
    "jel": ["Jours de lactation"],
    "lac": ["N° de Lactation", "Numéro de lactation", "N°. lac."],
    "traites": ["Nbre de traites", "Nombre de traites"],
    "cel": ["Indication Cellules"],
}
FACULTATIVES = {"traites", "cel"}


def _lire(texte, nom):
    texte = texte.lstrip("﻿")
    if not texte.strip():
        raise ErreurExport(f"Fichier « {nom} » vide.")
    premiere = texte.splitlines()[0]
    sep = ";" if premiere.count(";") > premiere.count(",") else ","
    lignes = list(csv.reader(io.StringIO(texte), delimiter=sep))
    voulus = {k: {_norm(n) for n in noms} for k, noms in COLONNES.items()}
    for i, ligne in enumerate(lignes[:5]):
        entetes = [_norm(c) for c in ligne]
        index = {}
        for cle, noms in voulus.items():
            for j, e in enumerate(entetes):
                if e in noms:
                    index[cle] = j
                    break
        if "vache" not in index:
            continue
        manquantes = [COLONNES[k][0] for k in COLONNES if k not in index and k not in FACULTATIVES]
        if "date" not in index:
            raise ErreurExport(
                f"Fichier « {nom} » : colonne « Date de production » introuvable. L'outil a besoin de la copie "
                "enrichie du rapport de production journalière, une ligne par vache et par jour, pas d'un "
                "rapport standard (photo du jour).")
        if manquantes:
            raise ErreurExport(
                f"Fichier « {nom} » : colonne(s) introuvable(s) : " + ", ".join(f"« {m} »" for m in manquantes)
                + ". Ajoutez-les au rapport dans Horizon, puis exportez à nouveau.")
        sortie = []
        for ligne in lignes[i + 1:]:
            if not ligne or index["vache"] >= len(ligne) or not ligne[index["vache"]].strip():
                continue
            if ligne[index["vache"]].strip().upper() in ("AVG", "SUM", "MOY", "TOTAL", "SOM"):
                continue
            sortie.append({k: (ligne[j].strip() if j < len(ligne) else "") for k, j in index.items()})
        return sortie, sorted(k for k in FACULTATIVES if k not in index)
    raise ErreurExport(
        f"Fichier « {nom} » : colonne « N° d'animal » introuvable. Vérifiez qu'il s'agit bien du rapport "
        "de production journalière, exporté au format CSV.")


def _nombre(v):
    v = (v or "").replace(" ", "").replace(" ", "").replace(",", ".").strip()
    if not v or v == "-":
        return None
    try:
        return float(v)
    except ValueError:
        return None


def _date(v):
    v = (v or "").strip()
    for f in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y", "%d/%m/%y"):
        try:
            return datetime.strptime(v[:10] if f != "%d/%m/%y" else v[:8], f).date()
        except ValueError:
            pass
    raise ErreurExport(f"Date de production illisible : « {v} ».")


def _jour(v):
    return datetime.strptime(v, "%Y-%m-%d").date()


# ---------- algèbre ----------

def _resoudre(a, b):
    """Résout a x = b (a symétrique définie positive), pivot partiel."""
    n = len(a)
    m = [list(a[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(m[r][c]))
        if abs(m[p][c]) < 1e-12:
            raise ErreurExport("Données insuffisantes pour tracer la courbe de lactation de chaque rang : "
                               "il manque des vaches à certains stades. Exportez au moins 6 mois de production.")
        m[c], m[p] = m[p], m[c]
        piv = m[c][c]
        for r in range(n):
            if r != c and m[r][c]:
                f = m[r][c] / piv
                lr, lc = m[r], m[c]
                for k in range(c, n + 1):
                    lr[k] -= f * lc[k]
    return [m[i][n] / m[i][i] for i in range(n)]


def _inverse(a):
    n = len(a)
    cols = [_resoudre(a, [1.0 if i == j else 0.0 for i in range(n)]) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def _percentile(trie, q):
    """Percentile à interpolation linéaire (comme numpy.percentile)."""
    pos = (len(trie) - 1) * q / 100
    i = int(math.floor(pos))
    if i + 1 >= len(trie):
        return float(trie[-1])
    return trie[i] + (trie[i + 1] - trie[i]) * (pos - i)


class BSpline:
    """Base B-spline cubique sans constante, nœuds aux quantiles (comme patsy bs(x, df))."""

    def __init__(self, valeurs, df, degre=3):
        trie = sorted(valeurs)
        n_int = df - degre
        interieurs = [_percentile(trie, 100 * (k + 1) / (n_int + 1)) for k in range(n_int)]
        self.bas, self.haut = float(trie[0]), float(trie[-1])
        self.noeuds = [self.bas] * (degre + 1) + interieurs + [self.haut] * (degre + 1)
        self.degre = degre
        self.n = len(self.noeuds) - degre - 1          # df + 1 fonctions ; la première est retirée
        self._cache = {}

    def __call__(self, x):
        if x in self._cache:
            return self._cache[x]
        t, k = self.noeuds, self.degre
        n = len(t) - 1
        # degré 0 : intervalle [t_i, t_{i+1}), le dernier intervalle non vide fermé à droite
        b = [1.0 if t[i] <= x < t[i + 1] else 0.0 for i in range(n)]
        if x >= self.haut:
            der = max(i for i in range(n) if t[i] < t[i + 1])
            b = [0.0] * n
            b[der] = 1.0
        for d in range(1, k + 1):
            nb = []
            for i in range(n - d):
                v = 0.0
                if b[i] and t[i + d] != t[i]:
                    v += (x - t[i]) / (t[i + d] - t[i]) * b[i]
                if b[i + 1] and t[i + d + 1] != t[i + 1]:
                    v += (t[i + d + 1] - x) / (t[i + d + 1] - t[i + 1]) * b[i + 1]
                nb.append(v)
            b = nb
        r = b[1:self.n]
        self._cache[x] = r
        return r


def _mco_effet_jour(obs, lignes_x, n_col):
    """Moindres carrés avec un effet fixe par jour, par retrait des moyennes journalières.

    obs : liste de (jour, y) ; lignes_x : liste de listes creuses [(colonne, valeur)].
    Retourne (coefficients, résidus, x centrés).
    """
    par_jour = {}
    for i, (j, _) in enumerate(obs):
        par_jour.setdefault(j, []).append(i)
    xc, yc = [None] * len(obs), [0.0] * len(obs)
    for j, idx in par_jour.items():
        moy = [0.0] * n_col
        my = 0.0
        for i in idx:
            my += obs[i][1]
            for c, v in lignes_x[i]:
                moy[c] += v
        k = len(idx)
        moy = [m / k for m in moy]
        my /= k
        for i in idx:
            x = [-m for m in moy]
            for c, v in lignes_x[i]:
                x[c] += v
            xc[i] = x
            yc[i] = obs[i][1] - my
    xtx = [[0.0] * n_col for _ in range(n_col)]
    xty = [0.0] * n_col
    for x, y in zip(xc, yc):
        for a in range(n_col):
            xa = x[a]
            if xa:
                ligne = xtx[a]
                for b in range(a, n_col):
                    ligne[b] += xa * x[b]
                xty[a] += xa * y
    for a in range(n_col):
        for b in range(a):
            xtx[a][b] = xtx[b][a]
    beta = _resoudre(xtx, xty)
    res = [y - sum(bc * xv for bc, xv in zip(beta, x)) for x, y in zip(xc, yc)]
    return beta, res, xc, xtx


def _rang(lac):
    return "P1" if lac == 1 else ("R2" if lac == 2 else "R3+")


# ---------- calcul ----------

def calculer(textes, parametres=None):
    p = dict(PARAMETRES)
    p.update({k: v for k, v in (parametres or {}).items() if v is not None and v != ""})
    if isinstance(p["exclus"], str):
        p["exclus"] = [s.strip() for s in p["exclus"].split(",") if s.strip()]
    exclus = sorted({_jour(s) for s in p["exclus"]})
    seuils = {"P1": p["seuil_p1"], "R2": p["seuil_r2"], "R3+": p["seuil_r3"]}

    if not textes:
        raise ErreurExport("Aucun fichier déposé.")
    brut, sans = {}, set()
    for nom, texte in textes:
        lignes, manquantes = _lire(texte, nom)
        sans.update(manquantes)
        for l in lignes:
            d = _date(l["date"])
            brut[(l["vache"], d)] = l                     # doublon vache-jour : la dernière ligne l'emporte
    if not brut:
        raise ErreurExport("L'export ne contient aucune ligne exploitable.")

    rows, ignorees = [], 0
    for (v, d), l in brut.items():
        jel, lac = _nombre(l.get("jel")), _nombre(l.get("lac"))
        if jel is None or lac is None:
            ignorees += 1
            continue
        rows.append({"v": v, "date": d, "lait": _nombre(l.get("lait")), "repro": (l.get("repro") or "").strip(),
                     "jel": int(round(jel)), "lac": int(round(lac)), "traites": _nombre(l.get("traites")),
                     "cel": _nombre(l.get("cel"))})

    # jour d'ancrage : le dernier jour complet
    dernier = max(r["date"] for r in rows)
    note_ancrage = None
    if p["ancrage"]:
        ancrage = _jour(p["ancrage"])
    else:
        ancrage = dernier
        totaux = {}
        for r in rows:
            if r["lait"]:
                t = totaux.setdefault(r["date"], [0.0, 0])
                t[0] += r["lait"]
                t[1] += 1
        moy = {d: t[0] / t[1] for d, t in totaux.items()}
        avant = [moy[d] for d in sorted(moy) if dernier - timedelta(days=8) <= d < dernier and d not in exclus]
        if dernier in moy and avant and moy[dernier] < 0.85 * sorted(avant)[len(avant) // 2]:
            ancrage = dernier - timedelta(days=1)
            part = round(100 * moy[dernier] / sorted(avant)[len(avant) // 2])
            note_ancrage = (f"Le dernier jour de l'export ({dernier.strftime('%d/%m/%Y')}) paraît incomplet : lait moyen "
                            f"par vache à {part} % des jours précédents. Le calcul s'arrête à la veille.")
    jours_exclus = set(exclus)
    rows = [r for r in rows if r["date"] <= ancrage and r["date"] not in jours_exclus]
    if not rows:
        raise ErreurExport("Aucune ligne avant la date d'ancrage.")
    jour_fin = max(r["date"] for r in rows)

    m = [r for r in rows if 7 <= r["jel"] <= 305 and r["lait"] and r["lait"] > 0]
    if len(m) < 100:
        raise ErreurExport("Trop peu de données : l'export doit couvrir plusieurs mois de production, "
                           "une ligne par vache et par jour.")
    for r in m:
        r["par"] = _rang(r["lac"])
        r["ll"] = math.log(r["lait"])
    lact_par_rang = {k: len({(r["v"], r["lac"]) for r in m if r["par"] == k}) for k in RANGS}
    trop_peu = [k for k in RANGS if lact_par_rang[k] < LACTATIONS_MIN_PAR_RANG]
    if trop_peu:
        noms = {"P1": "primipares", "R2": "vaches de rang 2", "R3+": "vaches de rang 3 et plus"}
        raise ErreurExport("Pas assez de " + " ni de ".join(noms[k] for k in trop_peu)
                           + f" dans l'export (au moins {LACTATIONS_MIN_PAR_RANG} lactations par rang) pour tracer "
                           "la courbe de leur rang. Exportez une période plus longue.")

    # modèle de position : courbe par rang (B-spline 5 ddl × rang) + effet jour
    bs5 = BSpline([r["jel"] for r in m], 5)
    nb = bs5.n - 1
    col_rang = {"P1": 0, "R2": 1}
    bloc = {"P1": 2, "R2": 2 + nb, "R3+": 2 + 2 * nb}
    xs = []
    for r in m:
        x = [(col_rang[r["par"]], 1.0)] if r["par"] in col_rang else []
        base = bloc[r["par"]]
        x += [(base + i, v) for i, v in enumerate(bs5(r["jel"])) if v]
        xs.append(x)
    _, res, _, _ = _mco_effet_jour([(r["date"], r["ll"]) for r in m], xs, 2 + 3 * nb)
    for r, e in zip(m, res):
        r["res"] = e

    # rapports entre rangs : décalage par rang + courbe commune (6 ddl) + effet jour
    bs6 = BSpline([r["jel"] for r in m], 6)
    xs2 = []
    for r in m:
        x = [(col_rang[r["par"]], 1.0)] if r["par"] in col_rang else []
        x += [(2 + i, v) for i, v in enumerate(bs6(r["jel"])) if v]
        xs2.append(x)
    k2 = 2 + bs6.n - 1
    beta2, res2, xc2, xtx2 = _mco_effet_jour([(r["date"], r["ll"]) for r in m], xs2, k2)
    inv = _inverse(xtx2)
    scores = {}
    for r, x, e in zip(m, xc2, res2):
        s = scores.setdefault(r["v"], [0.0] * k2)
        for a in range(k2):
            s[a] += x[a] * e
    meat = [[sum(s[a] * s[b] for s in scores.values()) for b in range(k2)] for a in range(k2)]
    n_obs, g = len(m), len(scores)
    n_jours = len({r["date"] for r in m})
    k_total = k2 + n_jours                                # constante et effets jour compris
    corr = g / (g - 1) * (n_obs - 1) / (n_obs - k_total) if g > 1 and n_obs > k_total else 1.0
    rapports = {}
    for nom, c in (("P1", 0), ("R2", 1)):
        var = sum(inv[c][a] * meat[a][b] * inv[b][c] for a in range(k2) for b in range(k2)) * corr
        se = math.sqrt(max(var, 0.0))
        rapports[nom] = {"rapport": math.exp(beta2[c]), "bas": math.exp(beta2[c] - 1.96 * se),
                         "haut": math.exp(beta2[c] + 1.96 * se)}

    # position de chaque vache dans sa lactation en cours
    pos = {}
    for r in m:
        s = pos.setdefault((r["v"], r["lac"]), [0.0, 0])
        s[0] += r["res"]
        s[1] += 1
    fin_m = max(r["date"] for r in m)
    recents = {}
    for r in m:
        if r["date"] > fin_m - timedelta(days=14):
            t = recents.setdefault(r["v"], {"lait": [], "traites": [], "cel": []})
            t["lait"].append(r["lait"])
            if r["traites"] is not None:
                t["traites"].append(r["traites"])
            if r["cel"] is not None:
                t["cel"].append(r["cel"])

    vaches, inconnus = [], []
    for r in rows:
        if r["date"] != jour_fin:
            continue
        rang = _rang(r["lac"])
        statut = r["repro"]
        sn = _norm(statut)
        if sn not in STATUTS_CONNUS:
            inconnus.append({"vache": r["v"], "statut": statut or "vide"})
        s = pos.get((r["v"], r["lac"]))
        x = math.exp(s[0] / s[1]) if s else None
        n = s[1] if s else 0
        rec = recents.get(r["v"], {"lait": [], "traites": [], "cel": []})
        lait14 = sum(rec["lait"]) / len(rec["lait"]) if rec["lait"] else None
        traites14 = sum(rec["traites"]) / len(rec["traites"]) if rec["traites"] else None
        cel14 = max(rec["cel"]) if rec["cel"] else None
        seuil = seuils[rang]
        if sn in STATUTS_EXCLUS:
            verdict = "non_classee"
        elif r["jel"] > p["jel_max_ia"]:
            verdict = "delai_depasse"
        elif r["jel"] < p["jel_min_decision"] or x is None or n < p["jours_min"]:
            verdict = "trop_tot"
        elif x >= seuil + p["marge_limite"]:
            verdict = "continuer"
        elif x >= seuil:
            verdict = "limite"
        else:
            verdict = "sous_seuil"
        alerte = []
        if traites14 is not None and traites14 < p["traites_min"]:
            alerte.append("traites")
        if cel14 is not None and cel14 > p["cellules_max"]:
            alerte.append("cellules")
        vaches.append({"vache": r["v"], "rang": rang, "lactation": r["lac"], "jel": r["jel"], "statut": statut,
                       "position": x, "seuil": seuil, "jours": n, "lait14": lait14, "traites14": traites14,
                       "cel_max14": cel14, "verdict": verdict, "alertes": alerte})

    ordre = {"sous_seuil": 0, "delai_depasse": 1, "limite": 2, "trop_tot": 3, "continuer": 4, "non_classee": 5}
    vaches.sort(key=lambda v: (ordre[v["verdict"]], v["position"] if v["position"] is not None else 9))

    debut_m = min(r["date"] for r in m)
    return {
        "fenetre": [debut_m.isoformat(), fin_m.isoformat()],
        "jours_fenetre": (fin_m - debut_m).days + 1,
        "fenetre_courte": (fin_m - debut_m).days + 1 < JOURS_FENETRE_CONSEILLES,
        "ancrage": jour_fin.isoformat(),
        "note_ancrage": note_ancrage,
        "exclus": [d.isoformat() for d in exclus],
        "nb_vaches": len({r["v"] for r in m}),
        "nb_lactations": len(pos),
        "vache_jours": len(m),
        "lactations_par_rang": lact_par_rang,
        "lignes_ignorees": ignorees,
        "colonnes_absentes": sorted(COLONNES[k][0] for k in sans),
        "rapports": rapports,
        "inconnus": inconnus,
        "vaches": vaches,
        "parametres": {k: (v if not isinstance(v, date) else v.isoformat()) for k, v in p.items()},
    }


def calculer_json(textes_json, parametres_json="{}"):
    """Point d'entrée de l'outil en ligne : textes_json = [[nom, contenu], ...]."""
    try:
        return json.dumps(calculer(json.loads(textes_json), json.loads(parametres_json or "{}")))
    except ErreurExport as e:
        return json.dumps({"erreur": str(e)})


# ---------- usage en local ----------

LIBELLES = {"sous_seuil": "SOUS LE SEUIL : vérifier une cause passagère", "delai_depasse": "DÉLAI DÉPASSÉ : pas de nouvelle IA",
            "limite": "continuer — À LA LIMITE", "trop_tot": "trop tôt", "continuer": "continuer", "non_classee": ""}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    params = {}
    if len(sys.argv) > 2 and sys.argv[2]:
        params["ancrage"] = sys.argv[2]
    if len(sys.argv) > 3 and sys.argv[3]:
        params["exclus"] = sys.argv[3]
    with open(sys.argv[1], encoding="utf-8-sig", errors="replace") as f:
        try:
            r = calculer([(sys.argv[1], f.read())], params)
        except ErreurExport as e:
            print(e)
            sys.exit(2)
    print(f"Fenêtre {r['fenetre'][0]} → {r['fenetre'][1]} · ancrage {r['ancrage']} · {r['nb_vaches']} vaches · "
          f"{r['nb_lactations']} lactations · {r['vache_jours']} vache-jours (7–305 JEL)")
    if r["note_ancrage"]:
        print(r["note_ancrage"])
    for k, v in r["rapports"].items():
        print(f"  {k} / R3+ : {v['rapport']:.2f} (IC95 {v['bas']:.2f}–{v['haut']:.2f})")
    if r["inconnus"]:
        print("ATTENTION statut inconnu (traité comme vide) :", ", ".join(f"{i['vache']} « {i['statut']} »" for i in r["inconnus"]))
    f2 = lambda v, n=2: "–" if v is None else f"{v:.{n}f}"
    for v in r["vaches"]:
        if v["verdict"] == "non_classee":
            continue
        print(f"{v['vache']:>8} {v['rang']:>4} {v['jel']:>4} {v['statut'][:16]:<16} {f2(v['position'])} {v['seuil']:.2f} "
              f"{v['jours']:>4} {f2(v['lait14'], 1):>5} {f2(v['traites14'], 1):>4} {f2(v['cel_max14'], 0):>5}  "
              f"{LIBELLES[v['verdict']]}  {' '.join(v['alertes'])}")
