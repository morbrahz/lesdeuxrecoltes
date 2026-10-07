+++
title = "Outil en ligne : la liste des vaches à pousser au robot, depuis les exports Lely Horizon"
seoTitle = "Outil : les vaches à pousser au robot, depuis Lely Horizon"
date = 2026-09-27
lastmod = 2026-09-27
draft = false
weight = 2
summary = "Déposez vos exports Lely Horizon et obtenez, numéro par numéro, les vaches à pousser à la prochaine tournée. Calcul dans le navigateur, aucun envoi."
+++

Cet outil applique la méthode décrite dans [Quelles vaches pousser au robot de traite](/elevage/quelles-vaches-pousser-au-robot/) à vos propres exports, et donne la liste des vaches à aller chercher, avec leur numéro d'animal.

**Vos fichiers ne quittent pas votre ordinateur.** Le calcul s'exécute dans votre navigateur ; rien n'est envoyé ni conservé, ni sur ce site ni ailleurs. Au premier calcul, le navigateur télécharge le moteur de calcul depuis ce site (une douzaine de Mo, gardés ensuite en mémoire).

*Dernière mise à jour : 27 septembre 2026.*

## 1. Les exports à préparer

Trois rapports du logiciel Lely Horizon, exportés au format CSV. Le premier est une copie personnalisée du rapport standard, dont la création est décrite pas à pas dans [Créer un rapport de production journalière par vache dans Lely Horizon](/elevage/rapport-production-journaliere-lely-horizon/).

| Rapport | Utilité | Colonnes indispensables |
|---|---|---|
| **Production journalière par vache** | Le classement : autonome ou à pousser | N° d'animal, Date de production, Production journalière, Nbre de traites, Nbre de refus, Jours de lactation |
| **Liste des traites** (recommandé) | Le correctif du passage spontané : un tiers de vaches à pousser en moins dans le cas observé | N° d'animal, Date et heure de visite |
| **Vaches en retard** | La liste de la tournée | N° d'animal |

Le premier est obligatoire, le deuxième **fortement recommandé**. Sans la liste des traites, l'outil ne voit pas les vaches qui passent seules au robot en dehors des tournées, et les laisse dans la liste à pousser : dans le cas qui a servi à construire l'outil, l'ajouter a réduit cette liste d'un tiers. Le troisième est facultatif : sans les vaches en retard, l'outil donne le classement, à croiser soi-même avec la liste du robot.

Précautions :

- si une colonne manque, l'outil la nomme : il suffit de l'ajouter à la copie du rapport, comme décrit dans la [page dédiée](/elevage/rapport-production-journaliere-lely-horizon/) ;
- la production journalière et la liste des traites doivent couvrir, idéalement, **les 3 à 5 derniers jours**. Le classement porte sur deux jours consécutifs, et le passage spontané se compte sur trois ; quelques jours de plus donnent une marge si le dernier jour exporté est incomplet ou si une journée manque. Au-delà de cinq jours, l'export s'alourdit sans rien apporter au calcul ;
- sur une période plus courte, l'outil le signale. Il compte alors moins de passages spontanés, et laisse donc des vaches à pousser plutôt que l'inverse.

## 2. L'outil

{{< outil-vaches-a-pousser >}}

## 3. Lire le résultat

- **À pousser maintenant** : les vaches en retard selon le robot et non autonomes selon le classement. C'est la liste de la tournée.
- **Classées à pousser** : toutes les vaches sans refus sur deux jours, moins celles qui passent seules au robot. Elles ne se poussent que lorsqu'elles sont en retard.
- **Autonomes** : au moins un refus sur deux jours, ou passage spontané régulier. Elles ne se poussent pas, même en retard.
- **Hors classement** : fraîches vêlées et vaches sans données suffisantes. La liste de la tournée les inclut quand elles sont en retard ; la décision reste à l'éleveur.

Le classement porte sur le dernier jour présent dans l'export de production et la veille. Exporter après la fin de la journée donne donc le classement le plus à jour.

## 4. Le calcul et ses réglages

Le calcul applique exactement la règle décrite dans [Quelles vaches pousser au robot de traite](/elevage/quelles-vaches-pousser-au-robot/), sans rien y ajouter. Il s'exécute dans votre navigateur : aucun fichier n'est envoyé.

Les réglages de l'outil reprennent ceux de la méthode : 12 kg par traite, 7 jours de lactation, passage spontané exigé 2 jours sur 3, dans le bloc « Réglages ». Ils ont été arrêtés sur un seul troupeau, et gagnent à être ajustés sur le sien.

Les **plages de poussée** sont à renseigner d'abord : ce sont elles qui distinguent une vache venue seule d'une vache poussée. Les valeurs proposées, de 7 h à 12 h et de 16 h à 21 h, correspondent à deux tournées, matin et soir, avec le temps de passage des vaches poussées. Une plage trop courte ferait compter comme spontanées des vaches venues après avoir été poussées ; une plage trop large ne fait que retenir des vaches à pousser. Dans le doute, mieux vaut élargir.

L'outil a été construit sur les exports d'une version française de Lely Horizon. Si vos rapports ont d'autres intitulés de colonnes, le message d'erreur l'indique.

*Le calcul s'exécute avec [Pyodide](https://pyodide.org), distribué sous licence MPL 2.0 et hébergé sur ce site. [Code source du calcul](/outils/vaches-a-pousser/regle_pousser.py).*
