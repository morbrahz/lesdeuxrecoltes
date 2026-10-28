+++
title = "Quand arrêter d'inséminer une vache laitière"
date = 2026-10-28
lastmod = 2026-10-28
draft = false
weight = 7
summary = "Arrêter d'inséminer une vache laitière : seuil de production par rang de lactation, même stade, même jour, délai de 300 jours, sans plafond d'IA."
+++

Une vache vide qui revient en chaleur pose toujours la même question : la
réinséminer, ou la laisser finir sa lactation et partir à la réforme ?
Continuer garde une vache adulte dans le troupeau, mais allonge son
intervalle entre vêlages et la fait traire longtemps en fin de lactation.
Arrêter la remplace par une génisse, qui produira nettement moins pendant sa
première lactation. On tranche souvent à l'œil, sur le lait du jour ou sur
le nombre d'inséminations déjà passées, et on se trompe dans les deux sens.

Cette page décrit une règle écrite : une vache n'est plus inséminée quand sa
production, comparée à celle des vaches **de son rang, au même stade et le
même jour**, tombe sous un seuil ; et plus aucune vache n'est inséminée après
300 jours de lactation. Le calcul se fait à partir des données du robot de
traite, avec l'[outil en ligne](/elevage/outil-reinsemination/).

*Dernière mise à jour : 28 octobre 2026.*

## 1. La règle

| Rang de lactation | La vache est comparée à… | Seuil |
|---|---|---|
| Primipare (1re lactation) | la courbe des primipares, même stade, même jour | **90 %** |
| Rang 2 | la courbe des vaches de rang 2, même stade, même jour | **80 %** |
| Rang 3 et plus | la courbe des vaches de rang 3 et plus, même stade, même jour | **80 %** |

Sous son seuil, une vache n'est plus inséminée, une fois écartée une cause
passagère (§ 4). Deux règles complètent le tableau :

- **plus d'insémination après 300 jours de lactation**, quelle que soit la
  production ;
- **pas de nombre maximum d'inséminations** : une bonne vache se réinsémine
  tant qu'elle reste dans le délai. Passer en semence croisée après deux IA
  reste possible, mais c'est une règle de semence (voir le [compteur de
  renouvellement](/elevage/outil-renouvellement/)), pas une règle d'arrêt.

## 2. Mesurer la production d'une vache : contre son rang, au même stade, le même jour

La règle tient sur la façon de mesurer. Comparer une vache à **la moyenne
brute du troupeau du jour** la fausse de trois façons.

- **Le stade de lactation.** Une vache à 200 jours produit moins qu'une
  vache au pic, sans être moins bonne. Comparée à la moyenne du jour, qui
  mélange tous les stades, une vache en fin de lactation paraît toujours
  faible.
- **Le rang.** Une primipare produit nettement moins qu'une adulte, et une
  vache de rang 2 moins qu'une vache de rang 3 et plus (cas observé, § 6).
  Mélanger les rangs condamne les jeunes vaches : une vache de rang 2
  parfaitement moyenne se retrouve vers 86 % de la moyenne des multipares,
  sous un seuil de 85 % à quelques kilos près.
- **La date.** Saison, changement de ration, autre cause accidentelle :
  tout le troupeau monte ou baisse ensemble. Une vache ne doit pas être jugée sur
  un mois où toutes ont baissé.

D'où la mesure retenue : pour chaque rang (primipares, rangs 2, rangs 3 et
plus), une **courbe de lactation** est tirée du troupeau lui-même, jour de
lactation par jour de lactation, en retirant l'effet de chaque date. La
**position** d'une vache est sa production rapportée à cette courbe, au même
jour de lactation et à la même date, puis **moyennée sur toute sa lactation
en cours**. Une position de 85 % veut dire : sur cette lactation, la vache a
produit en moyenne 15 % de moins que les vaches de son rang au même stade,
les mêmes jours.

La moyenne sur la lactation évite de décider sur une mauvaise semaine. Elle
porte sur les jours entre 7 et 305 de lactation : avant, le lait de
transition ; après, des vaches qui devraient être taries.

## 3. Les vaches concernées, et quand décider

- **Toutes les vaches non gestantes** : à inséminer, en chaleur, inséminées
  sans diagnostic, déclarées non gestantes, ou sans statut. Seules les
  gestantes et celles déjà marquées « ne pas inséminer » sont laissées de
  côté.
- **Pas de décision avant 60 jours de lactation**, ni avec moins de **30 jours
  de données** dans la lactation : la vache n'a pas encore passé son pic, et
  sa position bouge trop.
- **Après 300 jours de lactation**, la question ne se pose plus : pas de
  nouvelle insémination, et une vache inséminée qui revient en chaleur n'est
  pas reprise.

## 4. Sous le seuil : écarter d'abord une cause passagère

Une vache sous le seuil n'est pas forcément une vache faible. Avant de
décider, on regarde ses 14 derniers jours :

| Ce qu'on vérifie | Signe d'une cause passagère |
|---|---|
| Traites par jour | moins de 2 |
| Indication de cellules du robot | au-dessus de 300 000 |
| Mammite, boiterie | récente, notée dans le carnet sanitaire |

S'il y a une cause passagère, on attend qu'elle soit levée et on refait le
calcul. Sinon, la vache passe en « ne plus inséminer » dans le logiciel du
robot. C'est une décision de l'éleveur : la règle dit où regarder, elle ne
décide pas à sa place.

Les autres critères restent des **vetos séparés**, décidés vache par vache :
un problème de reproduction (métrite, kystes) traité selon le protocole
établi avec son vétérinaire, une vache difficile au robot, des membres ou
une mamelle qui ne passeront pas une lactation de plus. La règle de
production ne les remplace pas.

## 5. Pourquoi ces seuils

Les seuils ont été choisis par **simulation d'un troupeau** sur 25 ans,
répétée 60 fois, calée sur les résultats de l'élevage : rang moyen à la
réforme proche de 3, intervalle entre vêlages proche de 385 jours, lait par
place. Chaque règle candidate y est appliquée, et on compare la marge par
place et par an. Deux hypothèses pèsent sur le résultat :

- **l'offre de génisses** : de l'ordre de 36 % de l'effectif par an ;
- **le prix** : une génisse vendue rapporte 300 € de moins qu'une vache de
  réforme. Arrêter d'inséminer, c'est vendre une vache de réforme et garder
  une génisse qui aurait été vendue.

Résultats, en euros par place et par an :

| Règle comparée | Écart |
|---|---|
| Règle de la page (90 / 80 / 80, 300 jours, sans plafond) contre l'ancienne règle (85 % de la moyenne brute du troupeau, arrêt à 200 jours) | **+55 €** |
| Même comparaison, offre de génisses à 32 % ou à 40 % | +41 € à +70 € |
| Délai fixé entre 250 et 400 jours au lieu de 300 | équivalent |
| Délai fixé à 200 jours | −69 € |
| Plafond de 5 inséminations, contre aucun plafond | −34 € |
| Plafond de 3 inséminations, contre aucun plafond | −208 € |

Ce que le tableau dit : **le plafond du nombre d'inséminations est la règle
la plus coûteuse**. Il réforme des vaches qui produisent bien, simplement
parce qu'elles ont mis du temps à reprendre, et les remplace par des
primipares qui produisent moins. Le délai, lui, compte peu entre 250 et
400 jours ; il devient coûteux s'il est trop court.

Avec la règle de la page, la simulation prévoit des arrêts d'insémination
pour environ **16 % des vaches par an**, un renouvellement d'environ **34 %**
et un intervalle entre vêlages d'environ **394 jours**.

**Ces seuils sont ceux d'un troupeau.** La méthode de mesure (§ 2) se
transpose telle quelle ; les seuils dépendent de l'offre de génisses et du
rapport de prix entre génisse et vache de réforme. Sur un autre élevage, ils
sont un point de départ, à corriger avec le suivi du § 7.

## 6. Cas observé

Sur l'élevage, sur un export de près de dix mois de production
(octobre 2026) :

- une **primipare** produit en moyenne **69 %** du lait d'une vache de rang 3
  et plus, au même stade et le même jour ;
- une vache de **rang 2** en produit **81 %**.

L'écart entre rangs est donc large, et c'est lui qui rend la moyenne brute
inutilisable : une jeune vache ordinaire s'y retrouve sous le seuil. Comparée
à la courbe de son rang, elle se situe autour de 100 %, comme n'importe
quelle vache moyenne.

## 7. Suivre la règle : les génisses vendues

Un seul indicateur dit si les seuils sont bien placés : **le nombre de
génisses vendues par an**, comparé à la marge de sécurité du
renouvellement.

- S'il reste des génisses à vendre au-delà de la marge, les seuils sont
  **trop bas** : on garde des vaches qu'on pourrait remplacer.
- Si des vaches vides attendent une génisse pour être remplacées, les seuils
  sont **trop hauts**.

La règle se relit au moins une fois par an sur un nouvel export, ou plus tôt si l'un
de ses appuis bouge : l'écart de production entre rangs (§ 6) change
nettement, le prix d'une génisse dépasse celui d'une vache de réforme, ou
l'on peut mesurer la réussite des inséminations par rang d'IA, que la
simulation a dû supposer.

## 8. Les données

La position d'une vache se calcule sur **sa lactation en cours**, et les
courbes de chaque rang sur tout le troupeau. Il faut donc un export qui
couvre **au moins 6 mois**, idéalement depuis le début de l'année : la copie
enrichie du rapport de production journalière par vache de Lely Horizon,
décrite dans [Créer un rapport de production journalière par vache dans Lely
Horizon](/elevage/rapport-production-journaliere-lely-horizon/). Un export de
quelques jours, suffisant pour les [vaches à
pousser](/elevage/quelles-vaches-pousser-au-robot/), ne l'est pas ici.

Deux précautions :

- **garder une copie de chaque export brut** : les animaux sortis peuvent
  disparaître des exports suivants, et avec eux une partie des courbes ;
- **écarter les jours perturbés** (panne du robot, coupure de courant) : ils
  déplacent la courbe du jour pour tout le troupeau.

L'[outil en ligne](/elevage/outil-reinsemination/) fait le calcul dans le
navigateur, sans envoyer les données, et sort la liste des vaches qui
appellent une décision.

## À retenir

- Une vache se compare à **son rang, au même stade et le même jour**, jamais à
  la moyenne brute du troupeau.
- Seuils : **90 %** pour une primipare, **80 %** à partir du rang 2, sur la
  moyenne de la lactation en cours.
- **Plus d'insémination après 300 jours** de lactation, **sans plafond** du
  nombre d'IA.
- Pas de décision avant 60 jours de lactation ; sous le seuil, écarter
  d'abord une cause passagère.
- Les seuils se vérifient par les **génisses vendues** chaque année.
