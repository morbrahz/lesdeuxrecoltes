+++
title = "Outil en ligne : bilan du troupeau laitier depuis les exports Lely Horizon"
seoTitle = "Outil : bilan du troupeau laitier depuis Lely Horizon"
date = 2026-09-27
lastmod = 2026-09-27
draft = false
weight = 5
summary = "Bilan du troupeau laitier depuis l'export Lely Horizon : production, taux, cellules et vaches à regarder entre deux contrôles. Calcul dans le navigateur."
+++

Cet outil établit, à partir d'un seul export du robot, le tableau de bord décrit dans [Suivre son troupeau entre deux contrôles laitiers avec les données du robot de traite](/elevage/suivre-son-troupeau-entre-deux-controles/) : production, taux, cellules, stades de lactation, fréquentation du robot, et la liste des vaches à regarder, par numéro.

**Votre fichier ne quitte pas votre ordinateur.** Le calcul s'exécute dans votre navigateur ; rien n'est envoyé ni conservé. Au premier calcul, le navigateur télécharge le moteur de calcul depuis ce site (une douzaine de Mo, gardés ensuite en mémoire).

*Dernière mise à jour : 27 septembre 2026.*

## 1. L'export à préparer

Un seul fichier : le rapport **Production journalière par vache** de Lely Horizon, exporté au format CSV sur **les 3 à 5 derniers jours**. C'est le même rapport que pour l'[outil des vaches à pousser](/elevage/outil-vaches-a-pousser/) ; sa création est décrite dans [Créer un rapport de production journalière par vache dans Lely Horizon](/elevage/rapport-production-journaliere-lely-horizon/).

Quatre colonnes sont indispensables : N° d'animal, Date de production, Production journalière, Jours de lactation. Les autres enrichissent le bilan quand elles sont présentes — taux, cellules, rang de lactation, rumination, ingestion, concentré, poids, traites, refus, échecs. Une rubrique dont les colonnes manquent s'affiche vide, sans erreur.

## 2. L'outil

{{< outil-bilan-troupeau >}}

## 3. Lire le bilan

- **Les moyennes portent sur toute la période exportée**, vache par vache, cases vides ignorées. Le troupeau étudié est celui qui est au robot le dernier jour.
- **TB, TP et cellules sont des indications du robot.** Elles servent à suivre des tendances et à repérer des vaches ; les chiffres officiels restent ceux du contrôle laitier.
- **« Vaches à regarder »** liste, par numéro, les vaches qui dépassent un seuil : rapport TB/TP élevé en début de lactation, TB inférieur au TP, cellules élevées en moyenne ou à la dernière indication. Ce sont des signaux, pas des diagnostics.
- **Le bouton d'impression** produit une version papier ou PDF du bilan, sans le reste de la page.

Les seuils se modifient dans le bloc « Seuils ». Leurs valeurs par défaut et leurs sources sont données dans la [page méthode](/elevage/suivre-son-troupeau-entre-deux-controles/).

Le **niveau d'étable estimé** est une projection de la production du moment sur une lactation de 305 jours, corrigée du stade et du rang de lactation. C'est un ordre de grandeur pour suivre le troupeau d'un mois sur l'autre, pas le niveau d'étable du contrôle laitier ; son calcul est détaillé dans la [page méthode](/elevage/suivre-son-troupeau-entre-deux-controles/#5-le-niveau-détable-estimé).

*Le calcul s'exécute avec [Pyodide](https://pyodide.org), distribué sous licence MPL 2.0 et hébergé sur ce site. [Code source du calcul](/outils/bilan-troupeau/bilan_troupeau.py).*
