+++
title = "Créer un rapport de production journalière par vache dans Lely Horizon"
date = 2026-09-27
lastmod = 2026-09-27
draft = false
weight = 3
summary = "Lely Horizon : dupliquer le rapport de production journalière par vache et y ajouter refus, traites, jours de lactation et indicateurs de suivi, pour un export CSV complet, en quelques minutes et une fois pour toutes."
+++

Les rapports standards de Lely Horizon ne contiennent pas forcément toutes les colonnes dont on a besoin. Horizon permet en revanche d'en faire une copie et d'y ajouter les champs voulus. Cette page décrit la copie du rapport de production journalière par vache utilisée par l'[outil des vaches à pousser au robot](/elevage/outil-vaches-a-pousser/), qui applique la méthode décrite dans [Quelles vaches pousser au robot de traite](/elevage/quelles-vaches-pousser-au-robot/). Elle contient plus de champs que cet outil n'en lit : les autres servent au [bilan du troupeau](/elevage/outil-bilan-troupeau/), qui utilise le même export.

La manipulation prend quelques minutes et ne se fait qu'une fois. Le rapport d'origine n'est pas modifié.

*Dernière mise à jour : 27 septembre 2026.*

## 1. Le contenu du rapport

Le numéro d'animal figure dans le rapport sans avoir à l'ajouter. Les autres champs, dans l'ordre de la liste « Champs sélectionnés » :

| Champ | Ce qu'il donne | Lu par l'outil des vaches à pousser |
|---|---|---|
| Alim. total programmé | Quantité d'aliment programmée pour la vache | |
| Etat reprod. | À inséminer, inséminée, gestante… | |
| N° de Lactation | Rang de lactation | |
| **Date de production** | Jour concerné par la ligne | **Oui** |
| **Production journalière** | Lait produit sur la journée, en kg | **Oui** |
| Indication Cellules | Indication de comptage cellulaire mesurée au robot | |
| MG indication | Indication du taux butyreux | |
| MP indication | Indication du taux protéique | |
| **Nbre de traites** | Traites réalisées dans la journée | **Oui** |
| **Nbre de refus** | Visites sans autorisation de traite | **Oui** |
| **Jours de lactation** | Jours depuis le vêlage | **Oui** |
| Minutes d'ingestion totales | Temps d'ingestion, si l'élevage a les capteurs correspondants | |
| Poids | Poids, quand il est mesuré | |
| Minutes de rumination | Temps de rumination, si l'élevage a les capteurs correspondants | |
| Moy. Echecs | Moyenne des échecs de traite calculée par Horizon | |
| Moy. Traites | Moyenne du nombre de traites calculée par Horizon | |
| Moy. Refus | Moyenne du nombre de refus calculée par Horizon | |
| Nbre d'échecs | Échecs de traite dans la journée | |

Pour le seul outil des vaches à pousser, les cinq champs en gras suffisent. Les ajouter tous évite de revenir dans le rapport plus tard.

## 2. Dupliquer le rapport standard

1. Dans la liste des rapports d'Horizon, ouvrir le rapport **« Traite – Production journalière par vache »**. Il porte le mot-clé *Traite*.
2. Cliquer sur **les trois points** du rapport, puis sur **Dupliquer**. Horizon crée une copie nommée **« Copie de Traite – Production journalière par vache »**, qui apparaît dans la liste des rapports.
3. Ouvrir la copie, cliquer sur les trois points, puis sur **Modifier**. La fenêtre *Modifier rapport* s'ouvre sur l'onglet **Champs**. Le modèle indiqué en haut à droite est *Historique de production journalière* : il n'y a pas à le changer.

## 3. Ajouter les champs

![Fenêtre « Modifier rapport » de Lely Horizon : à gauche la liste de tous les champs, avec une zone de recherche ; à droite les champs sélectionnés, que l'on réordonne par glisser-déposer.](/images/elevage/horizon-modifier-rapport.png)

La fenêtre a deux colonnes : **Tous les champs** à gauche, rangés par catégories (Aliment, Animal, Attentions, Etat, Planning, Temps…), et **Champs sélectionnés** à droite, qui sont les colonnes du rapport.

Pour chaque champ du tableau du § 1 absent de la colonne de droite :

1. taper son nom dans la zone **Rechercher ici…** ;
2. le faire glisser de la colonne de gauche vers **Champs sélectionnés**.

Trois remarques :

- **L'ordre des champs n'a pas d'importance** pour l'outil, qui lit les colonnes par leur nom. On peut les ranger à sa convenance en les faisant glisser.
- **Les cases MOY et SOM peuvent rester décochées.** Elles ajoutent une ligne de moyenne ou de somme en tête de rapport ; l'outil l'ignore de toute façon.
- **Un champ déjà présent ne s'ajoute pas deux fois.** Selon la version d'Horizon, certains champs du tableau figurent déjà dans le rapport standard.

## 4. Nommer et enregistrer

Le nom proposé, « Copie de Traite – Production journalière par vache », peut être gardé ou remplacé dans le champ **Nom**, par exemple par « Production journalière – suivi robot ». Laisser le mot-clé *Traite* permet de retrouver le rapport avec les autres rapports de traite.

Cliquer sur **Enregistrer rapport**. La copie est prête ; elle se réutilise telle quelle à chaque export.

## 5. Exporter et vérifier

Ouvrir le rapport, choisir la période — **les 3 à 5 derniers jours** pour l'outil des vaches à pousser — et l'exporter au format **CSV**. La même période vaut pour la liste des traites, exportée à côté.

Pour vérifier le rapport, le plus simple est de déposer l'export dans l'[outil en ligne](/elevage/outil-vaches-a-pousser/). S'il manque un champ, l'outil l'indique par son nom, sans rien calculer ; il suffit alors de revenir au § 3.

## À retenir

- On ne modifie pas un rapport standard : on le duplique, et on modifie la copie.
- Les champs s'ajoutent par glisser-déposer, de « Tous les champs » vers « Champs sélectionnés ».
- L'ordre des colonnes est indifférent ; seuls leurs noms comptent.
- La copie se crée une fois et sert à chaque export.
