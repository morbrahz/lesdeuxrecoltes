+++
title = "Outil en ligne : quand arrêter d'inséminer une vache, depuis les exports Lely Horizon"
seoTitle = "Outil : quand arrêter d'inséminer une vache laitière"
date = 2026-10-28
lastmod = 2026-10-28
draft = false
weight = 8
annonce = false
summary = "Quelles vaches ne plus inséminer ? Production comparée à la courbe de son rang, même stade, même jour, depuis Lely Horizon. Calcul dans le navigateur."
+++

Cet outil applique la règle décrite dans [Quand arrêter d'inséminer une vache laitière](/elevage/quand-arreter-d-inseminer-une-vache/) aux données de votre troupeau : il trace la courbe de lactation de chaque rang, situe chaque vache non gestante par rapport à la courbe de son rang, et liste, par numéro, celles qui appellent une décision.

**Vos fichiers ne quittent pas votre ordinateur.** Le calcul s'exécute dans votre navigateur ; rien n'est envoyé ni conservé. Au premier calcul, le navigateur télécharge le moteur de calcul depuis ce site (une douzaine de Mo, gardés ensuite en mémoire).

*Dernière mise à jour : 28 octobre 2026.*

## 1. L'export à préparer

Un seul rapport : la **copie enrichie du rapport « Traite – Production journalière par vache »**, une ligne par vache et par jour, exportée au format CSV. Sa création, qui ne se fait qu'une fois, est décrite dans [Créer un rapport de production journalière par vache dans Lely Horizon](/elevage/rapport-production-journaliere-lely-horizon/) ; c'est le même rapport que pour l'[outil des vaches à pousser](/elevage/outil-vaches-a-pousser/). Les rapports standard d'Horizon, qui ne donnent qu'une photo du jour, ne suffisent pas.

- **Période : au moins 6 mois**, idéalement depuis le 1er janvier. Les courbes de chaque rang ont besoin de vaches à tous les stades, et la position d'une vache se moyenne sur toute sa lactation en cours. En dessous de 6 mois, l'outil calcule mais le signale.
- **Plusieurs fichiers** peuvent être déposés ensemble, par exemple un export par trimestre : ils sont fusionnés, et une même vache le même jour n'est comptée qu'une fois.
- **Colonnes lues** : N° d'animal, Date de production, Production journalière, Etat reprod., Jours de lactation, N° de Lactation. Nbre de traites et Indication Cellules servent aux alertes de cause passagère ; sans elles, le calcul se fait, et l'outil dit ce qui manque.
- **Gardez une copie de chaque export** : les animaux sortis peuvent disparaître des exports suivants.

## 2. L'outil

{{< outil-reinsemination >}}

**Conseiller d'élevage, organisme de contrôle laitier, concessionnaire ?** Si vous souhaitez utiliser cet outil pour les élevages que vous suivez, écrivez à [contact@lesdeuxrecoltes.fr](mailto:contact@lesdeuxrecoltes.fr).

## 3. Lire le résultat

- **La position** d'une vache est sa production moyenne sur la lactation en cours, rapportée à la courbe de son rang au même stade et les mêmes jours. 100 % : une vache dans la moyenne de son rang. Le calcul est détaillé dans la [page méthode](/elevage/quand-arreter-d-inseminer-une-vache/#2-mesurer-la-production-dune-vache--contre-son-rang-au-même-stade-le-même-jour).
- **Sous le seuil** : la vache est candidate à « ne plus inséminer ». L'outil affiche ses 14 derniers jours (lait, traites, cellules) et signale une cause passagère possible ; mammite et boiterie récentes se vérifient dans le carnet sanitaire. La décision reste la vôtre.
- **Délai dépassé** : plus de 300 jours de lactation, pas de nouvelle insémination.
- **À la limite** : moins de 2 points au-dessus du seuil ; à revoir au calcul suivant.
- **Trop tôt** : moins de 60 jours de lactation ou moins de 30 jours de données ; celles qui sont déjà sous le seuil sont mises à part, à surveiller.
- **Non classées** : gestantes et vaches déjà marquées « ne pas inséminer ». Un statut que l'outil ne reconnaît pas est signalé en tête : une gestante mal renseignée apparaîtrait sinon dans les listes.
- **Les rapports entre rangs** (primipares et rangs 2 face aux rangs 3 et plus) disent combien les jeunes vaches produisent de moins, au même stade et le même jour. Sur l'élevage de la page méthode : 0,69 et 0,81. Un écart très différent sur votre troupeau n'invalide pas la méthode, mais il mérite qu'on reprenne les seuils.

**Le dernier jour de l'export** est souvent incomplet, quand l'export est fait en cours de journée. L'outil l'écarte s'il paraît nettement plus bas que les jours précédents, et le dit ; vous pouvez aussi fixer vous-même le dernier jour complet dans les réglages, et y écarter des jours perturbés (panne, coupure de courant).

Les seuils, le délai et les durées minimales se modifient dans les réglages. Les valeurs par défaut sont celles d'un troupeau ; la [page méthode](/elevage/quand-arreter-d-inseminer-une-vache/#5-pourquoi-ces-seuils) explique d'où elles viennent et comment les vérifier sur le vôtre.

*Le calcul s'exécute avec [Pyodide](https://pyodide.org), distribué sous licence MPL 2.0 et hébergé sur ce site. [Code source du calcul](/outils/reinsemination/regle_reinsemination.py).*
