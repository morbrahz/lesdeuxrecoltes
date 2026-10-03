"""Annonce par e-mail les pages ajoutées au site, via l'API Brevo.

Lancé par le workflow de déploiement, une fois le site en ligne. Compare deux
commits et ne retient que les pages *ajoutées* dans une rubrique
(content/<rubrique>/<page>.md) : une correction de page existante n'envoie
rien. Une page se retire de l'annonce avec `annonce = false` dans son
en-tête.

Variables d'environnement :
  AVANT, APRES        commits à comparer (fournis par GitHub)
  BREVO_API_KEY       clé d'API Brevo (secret du dépôt) ; absente, rien n'est fait
  BREVO_LISTE         numéro de la liste des inscrits dans Brevo
  BREVO_ENVOI         "brouillon" (défaut : campagne créée, à relire et envoyer
                      depuis Brevo) ou "immediat" (envoi direct)
  EXPEDITEUR          adresse d'envoi, validée dans Brevo
                      (défaut : contact@lesdeuxrecoltes.fr)
  SITE                adresse du site (défaut : https://lesdeuxrecoltes.fr)
  ESSAI               "1" : affiche le message sans rien envoyer

Bibliothèque standard seule (Python 3.11 ou plus, pour tomllib).
"""
import datetime
import html
import json
import os
import subprocess
import sys
import tomllib
import urllib.error
import urllib.request

SITE = os.environ.get("SITE", "https://lesdeuxrecoltes.fr").rstrip("/")
EXPEDITEUR = os.environ.get("EXPEDITEUR") or "contact@lesdeuxrecoltes.fr"
NOM_SITE = "Les Deux Récoltes"
ZERO = "0" * 40
API = "https://api.brevo.com/v3"


def pages_ajoutees(avant, apres):
    if not avant or avant == ZERO:
        print("Pas de commit de référence (premier envoi ou historique réécrit) : rien à annoncer.")
        return []
    sortie = subprocess.run(
        ["git", "diff", "--diff-filter=A", "--name-only", avant, apres, "--", "content/"],
        check=True, capture_output=True, text=True,
    ).stdout
    chemins = []
    for ligne in sortie.splitlines():
        morceaux = ligne.split("/")
        # content/<rubrique>/<page>.md, hors pages de rubrique (_index.md)
        if len(morceaux) == 3 and ligne.endswith(".md") and not morceaux[2].startswith("_"):
            chemins.append(ligne)
    return chemins


def lire_entete(chemin):
    texte = open(chemin, encoding="utf-8").read()
    if not texte.startswith("+++"):
        raise ValueError(f"{chemin} : en-tête TOML (+++) attendu")
    return tomllib.loads(texte.split("+++", 2)[1])


def adresse(chemin, entete):
    if entete.get("url"):
        return SITE + "/" + entete["url"].strip("/") + "/"
    rubrique = chemin.split("/")[1]
    nom = entete.get("slug") or os.path.splitext(os.path.basename(chemin))[0]
    return f"{SITE}/{rubrique}/{nom}/"


def composer(pages):
    if len(pages) == 1:
        sujet = "Nouvelle page : " + pages[0]["titre"]
    else:
        sujet = f"{len(pages)} nouvelles pages sur {NOM_SITE}"
    blocs = []
    for p in pages:
        titre, url = html.escape(p["titre"]), html.escape(p["url"], quote=True)
        bloc = f'<h2 style="font-size:20px;margin:24px 0 8px"><a href="{url}" style="color:#1d1e20">{titre}</a></h2>'
        if p["resume"]:
            bloc += f'<p style="margin:0 0 8px">{html.escape(p["resume"])}</p>'
        bloc += f'<p style="margin:0"><a href="{url}">Lire la page</a></p>'
        blocs.append(bloc)
    corps = (
        '<!DOCTYPE html><html lang="fr"><body style="font-family:Arial,sans-serif;'
        'font-size:16px;line-height:1.5;color:#1d1e20;max-width:600px;margin:0 auto;padding:16px">'
        + "".join(blocs)
        + '<hr style="border:none;border-top:1px solid #ddd;margin:32px 0 16px">'
        '<p style="font-size:13px;color:#666">Vous recevez ce message parce que vous vous êtes '
        f'inscrit sur <a href="{SITE}/">lesdeuxrecoltes.fr</a> pour être prévenu des nouvelles pages. '
        "Une question, une remarque : répondez simplement à ce message.<br>"
        '<a href="{{ unsubscribe }}">Se désinscrire</a></p>'
        "</body></html>"
    )
    return sujet, corps


def appel(methode, chemin, cle, donnees=None):
    requete = urllib.request.Request(
        API + chemin,
        data=json.dumps(donnees).encode("utf-8") if donnees is not None else None,
        method=methode,
        headers={"api-key": cle, "Content-Type": "application/json", "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(requete, timeout=30) as reponse:
            contenu = reponse.read().decode("utf-8")
            return json.loads(contenu) if contenu else {}
    except urllib.error.HTTPError as e:
        print(f"Brevo a refusé la demande {methode} {chemin} : HTTP {e.code}\n"
              f"{e.read().decode('utf-8', 'replace')}")
        sys.exit(1)


def envoyer(sujet, corps, cle, liste, mode):
    campagne = appel("POST", "/emailCampaigns", cle, {
        "name": f"Nouvelles pages — {datetime.date.today().isoformat()}",
        "subject": sujet,
        "sender": {"name": NOM_SITE, "email": EXPEDITEUR},
        "replyTo": EXPEDITEUR,
        "htmlContent": corps,
        "recipients": {"listIds": [int(liste)]},
    })
    numero = campagne.get("id")
    print(f"Brevo : campagne n° {numero} créée.")
    if mode == "immediat":
        appel("POST", f"/emailCampaigns/{numero}/sendNow", cle)
        print("Brevo : envoi lancé.")
    else:
        print("Brevo : laissée en brouillon, à relire et envoyer depuis Brevo (Campagnes).")


def main():
    chemins = pages_ajoutees(os.environ.get("AVANT", ""), os.environ.get("APRES", "HEAD"))
    pages = []
    for chemin in chemins:
        entete = lire_entete(chemin)
        if entete.get("draft") or entete.get("annonce") is False:
            print(f"Ignorée : {chemin}")
            continue
        pages.append({
            "titre": entete.get("title", chemin),
            "resume": entete.get("summary", ""),
            "url": adresse(chemin, entete),
        })
    if not pages:
        print("Aucune nouvelle page à annoncer.")
        return
    sujet, corps = composer(pages)
    if os.environ.get("ESSAI") == "1":
        print("ESSAI — rien n'est envoyé.\n\nSujet : " + sujet + "\n\n" + corps)
        return
    cle, liste = os.environ.get("BREVO_API_KEY"), os.environ.get("BREVO_LISTE")
    if not cle or not liste:
        print("BREVO_API_KEY ou BREVO_LISTE manquant : rien n'est envoyé.")
        return
    envoyer(sujet, corps, cle, liste, os.environ.get("BREVO_ENVOI") or "brouillon")


if __name__ == "__main__":
    main()
