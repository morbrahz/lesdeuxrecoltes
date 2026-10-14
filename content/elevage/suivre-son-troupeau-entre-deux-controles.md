+++
title = "Suivre son troupeau entre deux contrôles laitiers avec les données du robot de traite"
seoTitle = "Suivre son troupeau entre deux contrôles laitiers au robot"
date = 2026-09-27
lastmod = 2026-10-14
draft = false
weight = 4
summary = "Robot de traite : un tableau de bord du troupeau entre deux contrôles laitiers (production, taux, cellules), avec moyennes justes et seuils sourcés."
+++

Le contrôle laitier donne une photographie du troupeau une fois par mois, à partir d'analyses de laboratoire. Le robot, lui, mesure chaque traite. Entre deux contrôles, ses données peuvent tenir lieu de tableau de bord : production, taux, cellules, comportement. À deux conditions : savoir ce qu'elles mesurent vraiment, et les calculer correctement.

Cette page décrit la méthode appliquée par l'[outil de bilan du troupeau](/elevage/outil-bilan-troupeau/). Les données viennent de Lely Horizon, par deux voies :

- **les rapports standard** « Traite – Production journalière par vache » et « Traite – Données de traites », tels que Lely les livre : une photo du jour, une ligne par vache ;
- **une copie enrichie du rapport de production journalière**, exportée sur plusieurs jours : c'est le rapport de [Quelles vaches pousser au robot de traite](/elevage/quelles-vaches-pousser-au-robot/), qui se prépare une fois pour toutes comme décrit dans [Créer un rapport de production journalière par vache dans Lely Horizon](/elevage/rapport-production-journaliere-lely-horizon/).

La première suffit pour le bilan du troupeau ; la seconde est recommandée pour repérer les vaches (§ 2).

*Dernière mise à jour : 14 octobre 2026.*

## 1. Ce que le robot mesure

| Donnée | Nature | Précaution |
|---|---|---|
| Lait par jour | Pesée à chaque traite | Fiable |
| TB, TP | **Indications** par capteur | Moins précises qu'une analyse de laboratoire ; à recaler de temps en temps sur le contrôle laitier |
| Cellules | **Indication** par capteur | Même remarque ; utile pour repérer une vache qui change, moins pour un chiffre absolu |
| Rumination, ingestion | Colliers ou capteurs | Seulement si l'élevage en est équipé |
| Concentré | Quantité **programmée** au robot | Ni la ration complète, ni forcément la quantité consommée |

Une indication qui manque un jour n'est pas une valeur nulle : c'est une mesure absente. La distinction compte dans les calculs qui suivent.

## 2. Trois règles de calcul

**Moyenner sur plusieurs jours pour repérer les vaches.** Les indications d'une vache varient d'un jour à l'autre, les cellules surtout. Pour dire quelles vaches regarder, chaque indicateur d'une vache est donc la moyenne de ses valeurs sur **les 3 à 5 derniers jours**, en ignorant les cases vides. Remplacer une case vide par zéro tirerait les taux vers le bas et ferait passer des vaches sous les seuils de cellules. Pour le seul bilan du troupeau, la photo du jour des rapports standard suffit : les écarts d'une vache à l'autre se compensent dans la moyenne (voir le cas observé, § 6).

**Pondérer les taux et les cellules par le lait.** Le taux du troupeau est celui du lait mélangé, comme dans le tank. Une vache à 40 kg pèse plus qu'une vache à 15 kg. Les autres indicateurs — stade, rumination, traites — sont des moyennes par vache.

**Écarter les premiers jours de lactation pour les taux.** Le colostrum puis le lait de transition ont un TB et un TP qui n'ont rien à voir avec ceux d'une lactation installée : un TB sous le TP le lendemain du vêlage n'est pas un signal d'acidose. Le TB et le TP des 5 premiers jours de lactation ne sont donc pas comptés, ni dans les taux du troupeau, ni dans les vaches à regarder.

**Étudier les vaches traites le dernier jour.** Le troupeau du bilan est celui qui est au robot à la fin de la période. Une vache tarie ou partie en cours de période n'y figure plus.

## 3. Les indicateurs

| Rubrique | Indicateur | Lecture |
|---|---|---|
| Production | Lait par vache et par jour, lait du troupeau, niveau d'étable estimé, stade moyen, rang moyen, part de primipares | Situer le troupeau ; le nuage lait selon le stade montre les vaches hors de la courbe |
| Taux | TB, TP, écart TB − TP, rapport TB/TP | L'équilibre de la ration et l'état énergétique, surtout en début de lactation |
| Cellules | Cellules pondérées, part de vaches saines et infectées | La santé de la mamelle et sa tendance |
| Stades | Les mêmes indicateurs de 0 à 100 jours, de 101 à 200 jours, au-delà | Où se situe un écart |
| Début de lactation | Primipares et multipares séparées, jusqu'à 100 jours | La période la plus à risque, où les deux groupes ne se comparent pas |
| Robot | Traites, refus et échecs par vache et par jour | La fréquentation du robot |
| Concentré | Lait par kg de concentré distribué au robot | À suivre dans le temps sur un même élevage, **pas** une efficacité alimentaire : celle-ci rapporte le lait à toute la matière sèche ingérée, que le robot ne connaît pas |

## 4. Les seuils de vigilance

| Signal | Seuil | Ce qu'il suggère |
|---|---|---|
| Rapport TB/TP élevé en début de lactation | Au-dessus de 1,5, jusqu'à 100 jours | Mobilisation des réserves, suspicion de cétose subclinique |
| Rapport TB/TP habituel | Entre 1,2 et 1,4 | Repère pour lire le troupeau |
| TB inférieur au TP | Rapport sous 1,0 | Signal classique d'acidose ruminale |
| Cellules | Moins de 300 000 : mamelle saine ; 300 000 à 800 000 : douteuse ; plus de 800 000 : infectée | Repères usuels d'interprétation d'un comptage individuel |

Deux précisions de méthode :

- ces seuils ont été établis sur des analyses de laboratoire ; appliqués à des indications de robot, ils désignent **des vaches à regarder, pas des diagnostics** ;
- pour les cellules, avec un export sur plusieurs jours, une vache est signalée si **sa moyenne ou sa dernière indication** dépasse le seuil. La moyenne seule noierait une mammite apparue la veille.

## 5. Le niveau d'étable estimé

Le niveau d'étable du contrôle laitier rapporte le lait produit sur douze mois aux vaches présentes, taries comprises. Les données de quelques jours ne le permettent pas. Le bilan en donne une **estimation** : la production actuelle de chaque vache, projetée sur une lactation de 305 jours, puis moyennée sur le troupeau.

Lait estimé d'une vache = lait moyen de la période × 305 × coefficient de stade × coefficient de rang.

| Stade de lactation | Coefficient | | Rang de lactation | Coefficient |
|---|---|---|---|---|
| Moins de 60 jours | 1,15 | | 1re lactation | 1,12 |
| 60 à 99 jours | 1,08 | | 2e lactation | 1,04 |
| 100 à 199 jours | 1,03 | | 3e et plus | 1,00 |
| 200 à 304 jours | 0,98 | | | |
| 305 jours et plus | 0,88 | | | |

Les coefficients corrigent la forme de la courbe de lactation : une vache en début de lactation n'a pas encore atteint son pic, une primipare a une courbe plus plate et plus persistante. Ce sont des coefficients d'usage, retenus sur l'expérience d'un troupeau, pas des coefficients officiels.

L'estimation se lit donc comme un **ordre de grandeur**, et surtout **dans le temps** : sa variation d'un mois sur l'autre, avec la même méthode, dit plus que sa valeur absolue. Elle ignore les vaches taries et reflète la production du moment, saison et ration comprises.

## 6. Ce que ce bilan ne remplace pas

- **Le niveau d'étable officiel**, calculé sur douze mois par le contrôle laitier.
- **Les lactations de référence.** Une lactation sur 305 jours se calcule à partir des contrôles successifs de toute la lactation, pas d'un instantané.
- **Les analyses officielles.** Le paiement du lait et les résultats de contrôle laitier restent ceux du laboratoire.

> **Cas observé.** Troupeau classé sur cinq jours, juste après un changement de robot. Rapport TB/TP du troupeau de 1,41, dans le haut de la plage habituelle. En début de lactation, une vache sur six dépassait 1,5. Pour les cellules, 78 % des vaches étaient sous 300 000 et 8 % au-dessus de 800 000 en moyenne de période. Mais la dernière indication a presque doublé le nombre de vaches signalées : l'une d'elles passait de moins de 100 000 à plus de 3 millions en deux jours, avec une moyenne de période encore sous 800 000.

> **Cas observé.** Même troupeau, même jour : photo du jour des rapports standard d'un côté, moyenne sur cinq jours de la copie enrichie de l'autre. Pour le troupeau, les deux concordent : même lait par vache au dixième près, TB et TP à moins d'un g/kg, même part de vaches sous 300 000 cellules (92 %) et au-dessus de 800 000 (2 %). Pour les vaches, les listes divergent. En cellules, les deux listes n'ont aucune vache en commun : la photo signale une vache sur une mesure isolée, et laisse de côté une vache passée au-dessus d'un million la veille de l'export. En début de lactation, la photo signale près de 8 % des vaches au-dessus de 1,5 de TB/TP, la moyenne sur cinq jours 2 % : sur un jour, une hausse passagère suffit.

## 7. Exemple chiffré fictif

Deux vaches : l'une à 40 kg de lait et 38 g/kg de TB, l'autre à 15 kg et 50 g/kg.

| Calcul | TB du troupeau |
|---|---|
| Moyenne simple des deux vaches | 44,0 g/kg |
| Moyenne pondérée par le lait | 41,3 g/kg |

La moyenne simple surestime le TB de près de 3 g/kg, parce qu'elle donne autant de poids à la vache qui produit le moins. C'est la moyenne pondérée qui correspond au lait livré.

## À retenir

- Les données du robot font un bon tableau de bord entre deux contrôles. La photo du jour des rapports standard suffit pour le troupeau ; pour repérer les vaches, il faut les moyenner sur 3 à 5 jours.
- Le TB et le TP des premiers jours de lactation ne s'interprètent pas.
- Une indication manquante n'est pas un zéro.
- Taux et cellules du troupeau se pondèrent par le lait.
- Les seuils désignent des vaches à regarder, pas des diagnostics.
- Le niveau d'étable estimé est une projection à suivre dans le temps ; le niveau d'étable officiel et les lactations de référence restent l'affaire du contrôle laitier.

*Sources des seuils : rapport TB/TP habituel et lecture du TB, [Le Point Vétérinaire](https://www.lepointveterinaire.fr/publications/le-point-veterinaire/article/n-262/tb-tp-taux-d-uree-des-outils-diagnostiques.html) ; rapport TB/TP et cétose subclinique, [Le suivi de reproduction](https://suividereproductionenvt.wordpress.com/lacetonemie-ou-la-cetose-subclinique/) ; seuils cellulaires, [Maison de l'élevage du Tarn](http://www.elevage-tarn.fr/73-bovins-lait-mammite-taux-cellulaire.html).*
