+++
title = "Quelles vaches pousser au robot de traite"
date = 2026-09-27
lastmod = 2026-09-27
draft = false
weight = 1
summary = "Robot de traite : quelles vaches aller chercher à chaque tournée et lesquelles laisser venir seules, selon les refus, le lait par traite et les retards."
+++

À chaque tournée, la même question : quelles vaches aller chercher ? Les
pousser toutes coûte du temps et du calme dans le bâtiment. N'en pousser
aucune laisse des vaches dépasser leur intervalle de traite, avec ce que cela
coûte en lait et en santé de la mamelle. Entre les deux, on pousse souvent
« celles qu'on connaît », et on se trompe dans les deux sens.

Cette page décrit une règle en deux temps. D'abord un classement, vache par
vache, à partir de deux indicateurs déjà présents dans le logiciel du robot :
qui vient seule, qui a besoin d'être poussée. Ensuite, à la tournée, un
croisement avec la liste des vaches en retard. Elle sert en routine, et
plus encore dans les semaines qui suivent une mise en route ou un changement
de robot, quand le troupeau réapprend à venir seul.

*Dernière mise à jour : 27 septembre 2026.*

## 1. Deux indicateurs suffisent

**Le refus.** Un refus est une visite au robot sans autorisation de traite :
la vache est venue trop tôt, et le robot l'a renvoyée. Un refus prouve donc
une chose simple, **la vache vient d'elle-même**. Une vache qui cumule des
refus n'a pas besoin qu'on aille la chercher.

**Le lait par traite.** Une vache qui vient peu souvent arrive avec
beaucoup de lait. Le lait par traite est donc une mesure indirecte de
l'intervalle entre deux traites : au-delà d'un certain niveau, la vache vient,
mais **pas assez souvent pour sa production**.

Les deux se lisent ensemble. Zéro refus dit que la vache ne vient pas en
avance ; le lait par traite dit si elle est en retard.

## 2. Le classement : qui peut avoir besoin d'être poussée

Les indicateurs se calculent sur **deux jours consécutifs** (la veille et le
jour même), pas sur un seul : une journée isolée est trop bruitée, entre un
refus accidentel et une traite retardée par une alarme.

| Situation sur les deux derniers jours | Classement |
|---|---|
| Au moins un refus | **Autonome** — la vache vient seule, elle ne se pousse pas |
| Aucun refus, plus de 12 kg de lait par traite | **À pousser** — elle vient trop rarement pour sa production |
| Aucun refus, 12 kg par traite ou moins | **À pousser** — sauf si elle passe seule au robot (§ 3) |
| Moins de 7 jours de lactation | Hors règle — période de colostrum, suivie à part |

Il n'y a que deux classements utiles : autonome ou à pousser. Le seuil de
12 kg ne crée pas une troisième catégorie ; il décide seulement si le
correctif du § 3 peut s'appliquer.

Le lait par traite se calcule sur les deux jours : lait total des deux jours
divisé par le nombre total de traites des deux jours.

## 3. Le correctif du passage spontané

Une vache sans refus et à faible production peut très bien venir seule : elle
ne se présente simplement pas avant d'avoir l'autorisation. Les refus ne la
voient pas. Pour la repérer, on regarde **quand** elle passe au robot.

Le principe : il existe des plages horaires où l'éleveur ne pousse jamais.
Une visite dans ces plages est forcément spontanée. Dans la pratique décrite
ici, ce sont :

- la nuit, de 21 h à 7 h ;
- le milieu de journée, de 12 h à 16 h.

Une visite compte qu'elle ait abouti ou non : une traite manquée prouve
autant que la vache est venue.

**Seuil retenu : un passage spontané sur au moins 2 des 3 derniers jours.**
Un passage isolé ne suffit pas ; il peut tenir à un hasard de circulation
dans le bâtiment. Si le seuil est atteint, la vache est classée autonome.

Ce correctif ne s'applique **pas** aux vaches à plus de 12 kg par traite.
Une vache qui vient seule la nuit mais arrive avec trop de lait n'a pas un
problème de motivation, elle a un problème de fréquence : venir ne suffit
pas, il faut venir assez souvent. Elle reste à pousser.

## 4. À la tournée : croiser avec la liste des vaches en retard

Le classement dit **qui** peut avoir besoin d'être poussée, pas **quand**.
Une vache à pousser qui vient d'être traite n'a rien à faire au robot. Le
moment est donné par un autre outil, déjà présent dans le logiciel : la
liste des vaches en retard, c'est-à-dire celles qui ont dépassé leur
intervalle de traite prévu.

La pratique décrite ici tient en une ligne : **deux tournées par jour, matin
et soir ; à chaque tournée, on pousse les vaches qui figurent à la fois dans
la liste des vaches en retard et parmi les vaches à pousser.**

Chaque filtre corrige l'autre :

- la liste des retards seule ferait pousser des vaches autonomes, en retard
  ce jour-là mais qui seraient venues d'elles-mêmes ;
- le classement seul ferait pousser des vaches qui viennent d'être traites.

Le croisement ne garde que les vaches qui sont en retard **et** qui ne
viennent pas seules.

## 5. Ce qu'il faut régler chez soi

Les valeurs ci-dessus sont des réglages, pas des constantes. Elles ont été
arrêtées sur un troupeau donné, et se transposent en les ajustant.

| Réglage | Valeur décrite ici | Ce qui le fait varier |
|---|---|---|
| Seuil de lait par traite | 12 kg | Niveau de production du troupeau, intervalle visé |
| Fenêtre de calcul | 2 jours consécutifs | Plus long = plus stable, mais réagit plus lentement |
| Plages de passage spontané | 21 h – 7 h et 12 h – 16 h | Horaires réels des tournées de l'élevage |
| Jours de passage spontané exigés | 2 sur 3 | Exigence voulue avant de cesser de pousser |
| Exclusion en début de lactation | 7 jours | Durée de la période colostrum |
| Tournées | Matin et soir | Organisation du travail ; les plages du § 3 doivent rester en dehors |

Deux interactions à garder en tête :

- **Les refus dépendent des autorisations de traite.** Avec des
  autorisations larges, une vache obtient presque toujours la traite en se
  présentant, et fait donc peu de refus. Plus les autorisations sont
  serrées, plus le refus devient un bon signal. Le seuil ne se juge qu'en
  connaissant ses propres réglages de permission.
- **Les plages horaires doivent être vraies.** Si quelqu'un pousse
  occasionnellement la nuit, le critère du passage spontané perd son sens.
  Mieux vaut des plages plus étroites mais certaines.

## 6. D'où viennent les données

Tout se lit dans le logiciel de gestion du robot (Lely Horizon dans le cas
décrit). Deux exports servent au classement :

1. **Un rapport de production journalière par vache**, qui donne pour
   chaque vache et chaque jour : lait produit, nombre de traites, nombre de
   refus, jours de lactation.
2. **La liste des traites**, qui donne l'heure de chaque visite, réussie ou
   non. C'est elle qui permet le correctif du § 3. Sans elle, la règle de
   base du § 2 s'applique seule, au prix d'une liste à pousser plus longue :
   dans le cas observé, ce correctif la réduit d'un tiers.

Les deux exports gagnent à couvrir les 3 à 5 derniers jours : deux jours
consécutifs pour le classement, trois pour le passage spontané, et une marge.

La liste des vaches en retard, elle, se consulte directement à la tournée,
sans export.

Les autres marques de robots enregistrent les mêmes informations — visites,
refus, traites, production. Les noms des rapports changent ; la règle, non.

Avec Lely Horizon, l'[outil en ligne](/elevage/outil-vaches-a-pousser/)
applique cette règle à ses propres exports et donne la liste des vaches à
pousser, numéro par numéro. Le calcul se fait dans le navigateur, sans
envoyer aucun fichier. Le rapport de production à exporter se prépare comme
décrit dans [Créer un rapport de production journalière par vache dans Lely
Horizon](/elevage/rapport-production-journaliere-lely-horizon/).
Le même export alimente l'[outil de bilan du troupeau](/elevage/outil-bilan-troupeau/),
dont la méthode est décrite dans [Suivre son troupeau entre deux contrôles
laitiers](/elevage/suivre-son-troupeau-entre-deux-controles/).

## 7. Exemple chiffré fictif

Trois vaches, sur les deux derniers jours :

| Vache | Refus | Traites | Lait | Lait par traite | Passages spontanés | Classement |
|---|---|---|---|---|---|---|
| A | 3 | 5 | 60 kg | 12,0 kg | — | Autonome (refus) |
| B | 0 | 4 | 60 kg | 15,0 kg | 2 jours sur 3 | À pousser (trop de lait par traite, le passage spontané ne compte pas) |
| C | 0 | 4 | 40 kg | 10,0 kg | 1 jour sur 3 | À pousser |
| C, deux jours plus tard | 0 | 4 | 40 kg | 10,0 kg | 2 jours sur 3 | Autonome (passage spontané) |

À la tournée du soir, la liste des vaches en retard contient A et C. On
pousse C seulement : A est en retard, mais elle vient seule. B n'est pas en
retard ce soir-là ; elle ne se pousse pas, même classée à pousser.

La vache A produit autant que la vache B. Ce qui les sépare n'est pas le
niveau de production, c'est la fréquence de visite : l'une vient en avance,
l'autre en retard.

> **Cas observé.** Changement de robot, troupeau classé chaque jour à partir
> du lendemain de la bascule.
>
> | | 2 jours après | 4 jours après |
> |---|---|---|
> | Autonomes | 56 % | 80 % |
> | À pousser | 44 % | 20 % |
>
> En deux jours, la part des vaches à pousser a été divisée par plus de
> deux. Autre constat : parmi les vaches à pousser au-delà de 12 kg par traite,
> plus des deux tiers passaient déjà seules au robot la nuit ou en milieu de
> journée. Elles venaient, mais trop rarement. Sans la distinction entre
> venir et venir assez souvent, elles auraient été laissées à tort.

## À retenir

- Un refus prouve que la vache vient seule : elle ne se pousse pas.
- Sans refus, la vache est à pousser. Au-delà du seuil de lait par traite,
  elle le reste même si elle vient parfois seule.
- Sous le seuil, une vache qui passe seule au robot, aux heures où personne
  ne pousse, 2 jours sur 3, redevient autonome.
- À la tournée, on ne pousse que les vaches à pousser qui figurent aussi
  dans la liste des vaches en retard.
- Les seuils se règlent sur son troupeau, ses autorisations de traite et
  ses horaires de tournée.
- Deux jours de données valent mieux qu'un : la règle tranche sur une
  tendance, pas sur un incident.
