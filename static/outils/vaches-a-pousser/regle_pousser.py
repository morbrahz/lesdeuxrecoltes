"""Quelles vaches pousser au robot de traite — moteur de calcul.

Méthode décrite sur https://lesdeuxrecoltes.fr/elevage/quelles-vaches-pousser-au-robot/

Ce fichier est exécuté tel quel par l'outil en ligne, dans le navigateur du
visiteur : aucune donnée n'est envoyée nulle part. Il fonctionne aussi en
local, sans rien installer d'autre que Python :

    python regle_pousser.py production.csv [liste_traites.csv] [vaches_en_retard.csv]

Exports attendus (Lely Horizon) :
  1. Production journalière par vache — obligatoire.
     Colonnes lues : N° d'animal, Date de production, Production journalière,
     Nbre de traites, Nbre de refus, Jours de lactation.
  2. Liste des traites — facultatif. Colonnes : N° d'animal, Date et heure de visite.
     Permet le correctif du passage spontané.
  3. Vaches en retard — facultatif. Colonne : N° d'animal.
     Permet de sortir directement la liste de la tournée.

Règle :
  - moins de 7 jours de lactation : fraîche vêlée, hors classement ;
  - au moins un refus sur deux jours consécutifs (J et J-1) : autonome ;
  - aucun refus : à pousser. Si le lait par traite sur ces deux jours est de
    12 kg ou moins, la vache redevient autonome quand elle passe seule au
    robot en dehors des plages de poussée (par défaut 7 h - 12 h et 16 h - 21 h)
    sur au moins 2 des 3 derniers jours.
  - tournée : on pousse les vaches en retard qui ne sont pas autonomes.
"""
import csv
import io
import json
import sys
import unicodedata
from datetime import date, datetime, timedelta

PARAMETRES = {
    "seuil_kg": 12.0,        # lait par traite sur 2 jours au-delà duquel le passage spontané ne compte pas
    "jel_min": 7,            # jours de lactation en dessous desquels la vache est hors classement
    # plages où l'éleveur pousse des vaches : [heure de début, heure de fin), heures
    # décimales admises (7.5 = 7 h 30). Toute visite en dehors est spontanée.
    # Chaque plage doit couvrir la tournée et le temps que les vaches poussées passent au robot.
    "poussees": [[7, 12], [16, 21]],
    "jours_regardes": 3,     # jours J-2, J-1, J
    "jours_min": 2,          # jours avec passage spontané exigés
    "debut": None,           # 'AAAA-MM-JJ' : ignorer les données antérieures (changement de robot)
}


class ErreurExport(Exception):
    """Export illisible ou incomplet : message destiné à l'éleveur."""


# ---------- lecture des exports ----------

def _norm(texte):
    t = unicodedata.normalize("NFKD", str(texte)).encode("ascii", "ignore").decode()
    return " ".join(t.lower().replace(".", " ").replace("°", " ").split())


def _lire(texte, colonnes, nom_export):
    """Retourne une liste de dict {clé: valeur} pour les colonnes demandées.

    colonnes : {clé: [intitulés acceptés]}. L'en-tête est cherché dans les
    premières lignes (certains exports ont une ligne de regroupement avant).
    """
    texte = texte.lstrip("﻿")
    premiere = texte.splitlines()[0] if texte.strip() else ""
    sep = ";" if premiere.count(";") > premiere.count(",") else ","
    lignes = list(csv.reader(io.StringIO(texte), delimiter=sep))
    voulus = {k: {_norm(n) for n in noms} for k, noms in colonnes.items()}
    for i, ligne in enumerate(lignes[:5]):
        entetes = [_norm(c) for c in ligne]
        index = {}
        for cle, noms in voulus.items():
            for j, e in enumerate(entetes):
                if e in noms:
                    index[cle] = j
                    break
        if "vache" in index:
            manquantes = [colonnes[k][0] for k in colonnes if k not in index]
            if manquantes:
                raise ErreurExport(
                    f"Export « {nom_export} » : colonne(s) introuvable(s) : "
                    + ", ".join(f"« {m} »" for m in manquantes)
                    + ". Ajoutez-les au rapport dans le logiciel du robot, puis exportez à nouveau.")
            sortie = []
            for ligne in lignes[i + 1:]:
                if not ligne or not ligne[index["vache"]].strip():
                    continue
                if ligne[index["vache"]].strip().upper() in ("AVG", "SUM", "MOY", "TOTAL"):
                    continue
                sortie.append({k: (ligne[j].strip() if j < len(ligne) else "") for k, j in index.items()})
            return sortie
    raise ErreurExport(
        f"Export « {nom_export} » : colonne « N° d'animal » introuvable. "
        "Vérifiez qu'il s'agit bien du bon rapport, exporté au format CSV.")


def _nombre(v):
    v = (v or "").replace(",", ".").replace(" ", "").strip()
    return float(v) if v else None


def _date(v):
    v = (v or "").strip()
    for f in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y"):
        try:
            return datetime.strptime(v[:10], f).date()
        except ValueError:
            pass
    raise ErreurExport(f"Date illisible : « {v} ».")


def _date_heure(v):
    v = " ".join((v or "").split())
    for f in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M", "%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M",
              "%d-%m-%Y %H:%M", "%d.%m.%Y %H:%M"):
        try:
            return datetime.strptime(v, f)
        except ValueError:
            pass
    raise ErreurExport(f"Date et heure de visite illisible : « {v} ».")


COLS_PRODUCTION = {
    "vache": ["N° d'animal", "No d'animal", "Numéro d'animal"],
    "date": ["Date de production", "Date"],
    "lait": ["Production journalière", "Production journaliere", "Lait"],
    "traites": ["Nbre de traites", "Nombre de traites", "Traites"],
    "refus": ["Nbre de refus", "Nombre de refus", "Refus"],
    "jel": ["Jours de lactation", "JEL"],
}
COLS_VISITES = {
    "vache": ["N° d'animal", "No d'animal", "Numéro d'animal"],
    "dt": ["Date et heure de visite", "Date et heure", "Heure de visite"],
}
COLS_RETARD = {
    "vache": ["N° d'animal", "No d'animal", "Numéro d'animal"],
    "nom": ["Nom de l'animal"],
}


def _vache(v):
    v = v.strip()
    try:
        return str(int(float(v)))
    except ValueError:
        return v


# ---------- règle ----------

def _dans_plage(h, plage):
    debut, fin = plage
    return (h >= debut or h < fin) if debut > fin else (debut <= h < fin)


def _jour_spontane(dt, p):
    """Jour de rattachement d'une visite spontanée, ou None si elle a lieu pendant une poussée.

    Une journée va de la première tournée du jour à la première tournée du
    lendemain : une visite de 3 h compte pour la veille.
    """
    h = dt.hour + dt.minute / 60
    plages = p["poussees"] or []
    if any(_dans_plage(h, pl) for pl in plages):
        return None
    d = dt.date()
    simples = [pl[0] for pl in plages if pl[0] < pl[1]]
    if simples and h < min(simples):
        d -= timedelta(days=1)
    return d


def classer(texte_production, texte_visites=None, texte_retard=None, parametres=None):
    p = dict(PARAMETRES)
    p.update({k: v for k, v in (parametres or {}).items() if v is not None})

    prod = {}
    for r in _lire(texte_production, COLS_PRODUCTION, "Production journalière par vache"):
        try:
            d = _date(r["date"])
        except ErreurExport:
            continue
        if p["debut"] and d < _date(p["debut"]):
            continue
        prod[(_vache(r["vache"]), d)] = r   # le dernier doublon l'emporte
    if not prod:
        raise ErreurExport("L'export de production ne contient aucune ligne exploitable.")
    jour_j = max(d for _, d in prod)

    visites = None
    if texte_visites:
        visites = {}
        instants = []
        for r in _lire(texte_visites, COLS_VISITES, "Liste des traites"):
            try:
                dt = _date_heure(r["dt"])
            except ErreurExport:
                continue
            instants.append(dt)
            j = _jour_spontane(dt, p)
            if j is not None:
                visites.setdefault(_vache(r["vache"]), set()).add((j, dt))

    vaches = []
    for (v, d), r in prod.items():
        if d != jour_j:
            continue
        veille = prod.get((v, d - timedelta(days=1)))
        jel = _nombre(r["jel"])
        fiche = {"vache": v, "jel": None if jel is None else int(jel),
                 "refus_2j": None, "traites_2j": None, "lait_2j": None,
                 "kg_par_traite": None, "passages": None, "passages_detail": [],
                 "statut": "", "raison": "", "en_retard": False, "nom": ""}
        if jel is not None and jel < p["jel_min"]:
            fiche["statut"], fiche["raison"] = "fraiche", f"fraîche vêlée ({int(jel)} JEL), hors classement"
        elif veille is None:
            fiche["statut"], fiche["raison"] = "insuffisant", "pas de données la veille, classement impossible"
        else:
            refus = (_nombre(r["refus"]) or 0) + (_nombre(veille["refus"]) or 0)
            traites = (_nombre(r["traites"]) or 0) + (_nombre(veille["traites"]) or 0)
            lait = (_nombre(r["lait"]) or 0) + (_nombre(veille["lait"]) or 0)
            kg = lait / traites if traites else float("inf")
            kgs = f"{kg:.1f}".replace(".", ",")
            fiche.update(refus_2j=int(refus), traites_2j=int(traites), lait_2j=round(lait, 1),
                         kg_par_traite=None if traites == 0 else round(kg, 1))
            if refus > 0:
                fiche["statut"], fiche["raison"] = "autonome", f"{int(refus)} refus sur 2 jours"
            elif kg > p["seuil_kg"]:
                fiche["statut"] = "a_pousser"
                fiche["raison"] = ("aucune traite sur 2 jours" if traites == 0 else
                                   f"0 refus, {kgs} kg par traite : vient trop rarement pour sa production")
            else:
                fiche["statut"], fiche["raison"] = "a_pousser", f"0 refus, {kgs} kg par traite"
                if visites is not None:
                    jours = {jour_j - timedelta(days=k) for k in range(p["jours_regardes"])}
                    vus = sorted(x for x in visites.get(v, set()) if x[0] in jours)
                    n = len({j for j, _ in vus})
                    fiche["passages"] = n
                    fiche["passages_detail"] = [dt.strftime("%d/%m %H:%M") for _, dt in vus]
                    if n >= p["jours_min"]:
                        fiche["statut"] = "autonome"
                        fiche["raison"] = (f"0 refus, {kgs} kg par traite, passe seule au robot "
                                           f"{n} jours sur {p['jours_regardes']}")
                    else:
                        fiche["raison"] += f", passe seule {n} jour{'s' if n > 1 else ''} sur {p['jours_regardes']}"
        vaches.append(fiche)

    retard = None
    if texte_retard:
        retard = {}
        for r in _lire(texte_retard, COLS_RETARD, "Vaches en retard"):
            retard[_vache(r["vache"])] = r.get("nom", "")
        connues = {f["vache"] for f in vaches}
        for f in vaches:
            if f["vache"] in retard:
                f["en_retard"], f["nom"] = True, retard[f["vache"]]
        for v, nom in retard.items():
            if v not in connues:
                vaches.append({"vache": v, "nom": nom, "jel": None, "statut": "inconnue",
                               "raison": "absente de l'export de production", "en_retard": True,
                               "refus_2j": None, "traites_2j": None, "lait_2j": None,
                               "kg_par_traite": None, "passages": None, "passages_detail": []})

    def cle(f):
        try:
            return (0, int(f["vache"]))
        except ValueError:
            return (1, f["vache"])
    vaches.sort(key=cle)
    return {
        "jour": jour_j.isoformat(),
        "avec_visites": visites is not None,
        # durée couverte par la liste des traites, en jours (3 à 5 recommandés)
        "couverture_visites": (round((max(instants) - min(instants)).total_seconds() / 86400, 1)
                               if visites is not None and instants else None),
        "jours_production": len({d for _, d in prod}),
        "avec_retard": retard is not None,
        "parametres": p,
        "vaches": vaches,
        # tournée : en retard et non autonome (fraîches et inconnues comprises)
        "tournee": [f["vache"] for f in vaches if f["en_retard"] and f["statut"] != "autonome"],
    }


def classer_json(texte_production, texte_visites, texte_retard, parametres_json):
    """Point d'entrée de l'outil en ligne."""
    try:
        return json.dumps(classer(texte_production or "", texte_visites or None, texte_retard or None,
                                  json.loads(parametres_json or "{}")))
    except ErreurExport as e:
        return json.dumps({"erreur": str(e)})


def _lire_fichier(chemin):
    brut = open(chemin, "rb").read()
    try:
        return brut.decode("utf-8-sig")
    except UnicodeDecodeError:
        return brut.decode("cp1252")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    fichiers = [_lire_fichier(c) for c in sys.argv[1:4]] + [None, None]
    try:
        res = classer(fichiers[0], fichiers[1], fichiers[2])
    except ErreurExport as e:
        print(e)
        sys.exit(1)
    libelles = {"a_pousser": "À pousser", "autonome": "Autonomes", "fraiche": "Fraîches vêlées",
                "insuffisant": "Données insuffisantes", "inconnue": "Absentes de l'export"}
    print("Classement au", res["jour"])
    for s, lib in libelles.items():
        ids = [f["vache"] for f in res["vaches"] if f["statut"] == s]
        if ids:
            print(f"  {lib:22s} {len(ids):3d} : {', '.join(ids)}")
    if res["avec_retard"]:
        print("Tournée — à pousser maintenant :", ", ".join(res["tournee"]) or "aucune")
