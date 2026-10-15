+++
title = "Outil en ligne : bilan du troupeau laitier depuis les exports Lely Horizon"
seoTitle = "Outil : bilan du troupeau laitier depuis Lely Horizon"
date = 2026-09-27
lastmod = 2026-10-14
draft = false
weight = 5
summary = "Bilan du troupeau laitier depuis les rapports standard de Lely Horizon : production, taux, cellules et vaches à regarder entre deux contrôles. Calcul dans le navigateur."
+++

Cet outil établit, à partir des rapports standard de Lely Horizon, le tableau de bord décrit dans [Suivre son troupeau entre deux contrôles laitiers avec les données du robot de traite](/elevage/suivre-son-troupeau-entre-deux-controles/) : production, taux, cellules, stades de lactation, fréquentation du robot, et la liste des vaches à regarder, par numéro.

**Vos fichiers ne quittent pas votre ordinateur.** Le calcul s'exécute dans votre navigateur ; rien n'est envoyé ni conservé. Au premier calcul, le navigateur télécharge le moteur de calcul depuis ce site (une douzaine de Mo, gardés ensuite en mémoire).

*Dernière mise à jour : 14 octobre 2026.*

## 1. Les exports à préparer

Deux rapports **standard** d'Horizon, tels que Lely les livre, sans rien y ajouter. Tous deux portent le mot-clé *Traite* et s'exportent au format CSV :

| Rapport standard | Ce qu'il apporte au bilan |
|---|---|
| **Traite – Production journalière par vache** | Lait, jours et rang de lactation, TB, TP, cellules, concentré |
| **Traite – Données de traites** | Traites, refus et échecs par vache, concentré |

On dépose les deux fichiers ensemble (sélection multiple). Un seul suffit pour obtenir un bilan : le premier donne tout sauf la rubrique Robot, le second tout sauf les taux et les cellules. L'outil indique ce qu'apporterait le rapport manquant.

Ces rapports sont une **photo du jour** : une ligne par vache, avec les chiffres calculés par Horizon au moment de l'export. L'outil les reprend tels quels. La date du bilan est lue dans le nom du fichier exporté ; mieux vaut donc ne pas le renommer.

### Pour la liste des vaches à regarder : la moyenne sur plusieurs jours

La photo du jour suffit pour **le bilan du troupeau** : sur un même troupeau, production, taux, cellules et fréquentation du robot sortent à quelques dixièmes près de ceux d'une moyenne sur cinq jours.

Elle ne suffit pas pour **repérer les vaches**, surtout pour les cellules. Une indication de robot varie fortement d'un jour à l'autre : sur un seul jour, une vache passée au-dessus d'un million de cellules la veille peut ne pas apparaître, et une autre être signalée sur une seule mesure haute. Dès qu'on se sert de la liste par vache, **la copie enrichie du rapport de production journalière, exportée sur les 3 à 5 derniers jours, est recommandée**. Elle ajoute aussi la rumination, l'ingestion et le poids.

Sa création, qui ne se fait qu'une fois, est décrite dans [Créer un rapport de production journalière par vache dans Lely Horizon](/elevage/rapport-production-journaliere-lely-horizon/). C'est aussi le rapport de l'[outil des vaches à pousser](/elevage/outil-vaches-a-pousser/). L'outil reconnaît cette copie à sa colonne « Date de production » et l'utilise alors seule.

Dans tous les cas, trois colonnes sont indispensables : N° d'animal, Production journalière, Jours de lactation. Une rubrique dont les colonnes manquent s'affiche vide, sans erreur.

## 2. L'outil

{{< outil-bilan-troupeau >}}

**Conseiller d'élevage, organisme de contrôle laitier, concessionnaire ?** Si vous souhaitez utiliser cet outil pour les élevages que vous suivez, écrivez à [contact@lesdeuxrecoltes.fr](mailto:contact@lesdeuxrecoltes.fr).

## 3. Lire le bilan

- **Avec les rapports standard**, chaque chiffre d'une vache est celui du jour d'export. **Avec la copie enrichie**, c'est sa moyenne sur la période exportée, cases vides ignorées, et le troupeau étudié est celui qui est au robot le dernier jour.
- **TB, TP et cellules sont des indications du robot.** Elles servent à suivre des tendances et à repérer des vaches ; les chiffres officiels restent ceux du contrôle laitier.
- **Le concentré** est la quantité programmée au robot, comme dans la [page méthode](/elevage/suivre-son-troupeau-entre-deux-controles/), pour que l'indicateur reste comparable d'un bilan à l'autre. Avec le seul rapport « Données de traites », qui ne donne que la quantité consommée, l'outil prend celle-ci et le signale.
- **TB et TP des premiers jours de lactation ne sont pas comptés** (5 jours par défaut, modifiable dans les seuils) : le colostrum et le lait de transition donnent des taux qui déclencheraient de fausses alertes.
- **« Vaches à regarder »** liste, par numéro, les vaches qui dépassent un seuil : rapport TB/TP élevé en début de lactation, TB inférieur au TP, cellules élevées (en moyenne ou à la dernière indication, avec la copie enrichie). Ce sont des signaux, pas des diagnostics.
- **Le bouton d'impression** produit une version papier ou PDF du bilan, sans le reste de la page.

Les seuils se modifient dans le bloc « Seuils ». Leurs valeurs par défaut et leurs sources sont données dans la [page méthode](/elevage/suivre-son-troupeau-entre-deux-controles/).

Le **niveau d'étable estimé** est une projection de la production du moment sur une lactation de 305 jours, corrigée du stade et du rang de lactation. C'est un ordre de grandeur pour suivre le troupeau d'un mois sur l'autre, pas le niveau d'étable du contrôle laitier ; son calcul est détaillé dans la [page méthode](/elevage/suivre-son-troupeau-entre-deux-controles/#5-le-niveau-détable-estimé).

*Le calcul s'exécute avec [Pyodide](https://pyodide.org), distribué sous licence MPL 2.0 et hébergé sur ce site. [Code source du calcul](/outils/bilan-troupeau/bilan_troupeau.py).*
