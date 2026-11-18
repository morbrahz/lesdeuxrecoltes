+++
title = "Marge sur coût alimentaire d'un troupeau laitier : la calculer par la ration et par la comptabilité"
seoTitle = "Marge sur coût alimentaire en lait : calcul et tableur gratuit"
date = 2026-11-18
lastmod = 2026-11-18
draft = false
weight = 9
summary = "Marge sur coût alimentaire en élevage laitier : la calculer par la ration ou par la comptabilité, pourquoi elles divergent, et un tableur gratuit."
# Adresse « /copy » du tableur, copie appartenant au compte Google du site (voir le shortcode tableur-copie)
tableurCopie = "https://docs.google.com/spreadsheets/d/1KOvD3dajEhKBiN4Po-1DwCGe30pSG-S9eGDdougLuW8/copy"
+++

La marge sur coût alimentaire est le premier chiffre que l'on regarde sur un atelier lait : ce qui reste du prix du lait une fois la ration payée. Elle se calcule de deux façons qui ne donnent jamais tout à fait le même résultat : **par la ration**, au jour le jour, à partir de ce que mangent les vaches ; **par la comptabilité**, après coup, à partir des factures. Cette page décrit les deux calculs, explique pourquoi ils divergent et à quoi sert chacun. Un [tableur gratuit](#7-le-tableur) applique le calcul par la ration à vos propres chiffres.

*Dernière mise à jour : 18 novembre 2026.*

## 1. Ce que l'on mesure

> **marge sur coût alimentaire = prix payé × lait livré − coût de la ration**

On l'exprime de deux façons, qui ne servent pas à la même chose :

- **par vache et par jour** (€ / VL / jour) : c'est l'unité qui suit la ration. Elle monte quand une vache produit plus pour le même coût, et elle se compare d'une semaine à l'autre ;
- **aux 1 000 litres livrés** (€ / 1 000 L) : c'est l'unité des références de groupe et des bordereaux de paie. Elle neutralise le volume.

Deux chiffres l'accompagnent toujours :

- **le coût alimentaire aux 1 000 litres produits** : coût de la ration divisé par tout le lait produit, livré ou non. Rapporté au seul lait livré, il se dégraderait chaque fois qu'on garde plus de lait pour les veaux, sans que la ration ait changé ;
- **les grammes de concentré par litre produit** : le premier levier du coût, et le plus facile à suivre.

## 2. Le calcul par la ration

Il part de ce qui est distribué, pas de ce qui est acheté. Quatre séries de chiffres suffisent :

| Donnée | Quand on la saisit | D'où elle vient |
|-|-|-|
| La ration | à chaque changement | quantités distribuées : fourrages à l'auge pour le troupeau, concentrés et herbe pâturée par vache, nombre de vaches traites |
| Le lait | à chaque collecte | litres collectés, et litres non livrés (veaux, écarts) si on les note |
| La paie | une fois par mois | prix de base, analyses du tank, grille de la laiterie |
| Les prix des aliments | à chaque nouveau prix | factures pour les achats ; coût à l'hectare ÷ rendement pour les fourrages produits |

Quatre règles font la justesse du calcul :

1. **On ne saisit que ce qui change.** Une ration reste valable jusqu'au changement suivant ; un prix, jusqu'au prix suivant. Inutile de recopier la ration chaque jour : la saisie d'un changement suffit.
2. **Les fourrages se comptent en matière sèche.** Le coût d'un fourrage produit s'exprime en euros par tonne de matière sèche : coût de la culture à l'hectare divisé par le rendement en tonnes de MS par hectare. Une erreur sur la teneur en MS de l'ensilage fausse le coût autant qu'une erreur de prix.
3. **Le lait d'une collecte se répartit sur les jours qu'elle couvre.** Une collecte tous les deux jours porte deux jours de traite ; rapportée au seul jour de collecte, elle ferait alterner des jours à zéro et des jours doubles.
4. **On pondère, on ne fait pas la moyenne des jours.** Le coût d'un mois est le total des coûts divisé par le total des litres. La moyenne des coûts journaliers donnerait autant de poids à un jour de faible production qu'à un jour de pointe.

> **Exemple chiffré (fictif).** 60 vaches traites, 25 litres produits par vache, dont 24,5 livrés : 1 500 L produits et 1 470 L livrés par jour. Ration du troupeau par jour : 800 kg de MS d'ensilage de maïs à 150 € / t MS (120 €), 50 kg de MS de foin à 120 € / t MS (6 €), 120 kg de tourteau de soja à 450 € / t (54 €), 180 kg d'aliment de production à 380 € / t (68,40 €), 12 kg de minéraux à 800 € / t (9,60 €). Coût de la ration : 258 € par jour.
>
> - Coût alimentaire : 258 € ÷ 1 500 L = **172 € aux 1 000 L produits**.
> - Concentré : 300 kg ÷ 1 500 L = **200 g par litre**.
> - Lait payé 440 € / 1 000 L : 1 470 L × 0,44 € = 646,80 €, moins 258 € = 388,80 € par jour, soit **6,48 € par vache et par jour**, ou **264 € aux 1 000 L livrés**.

## 3. Pourquoi la marge a bougé

Une marge qui baisse ne dit pas pourquoi. Par vache, elle s'écrit : lait livré par vache × (prix payé − coût de la ration par litre livré). Sa variation d'un mois à l'autre se décompose exactement en trois effets, chacun calculé aux valeurs moyennes des deux mois :

| Effet | Calcul |
|-|-|
| Prix du lait | écart de prix × lait livré par vache moyen |
| Lait par vache | écart de lait livré par vache × (prix moyen − coût moyen par litre) |
| Coût de la ration | − écart de coût par litre livré × lait livré par vache moyen |

Les trois s'additionnent exactement à la variation de marge. C'est la lecture la plus utile du suivi : elle sépare ce que l'on subit (le prix) de ce que l'on pilote (la production et la ration).

> **Cas observé.** Entre octobre et la première quinzaine de novembre, la marge par vache a perdu un peu moins d'un demi-euro par jour. La décomposition en attribue près de la moitié au lait par vache, un quart au prix du lait et un peu plus d'un quart au coût de la ration : la ration n'était pas la première cause, contrairement à ce que laissait croire la hausse de son coût aux 1 000 litres.

## 4. Le calcul par la comptabilité

La comptabilité donne la même marge vue des factures. Avec une balance analytique, on prend les ventes de lait et leurs litres, et l'on retire les achats d'aliments imputés au troupeau laitier : c'est la **marge sur coût alimentaire acheté**, celle que calcule l'[outil EBE en cours d'année](/tresorerie/outil-ebe-en-cours-d-annee/) et que décrit la page [Calculer l'EBE de son exploitation agricole en cours d'année](/tresorerie/ebe-en-cours-d-annee/#6-le-lait--prix-et-marge-sur-coût-alimentaire). En y ajoutant les charges des cultures fourragères, on obtient la marge sur coût total.

Elle a deux qualités que la ration n'a pas : elle repose sur des montants réellement payés, et elle se compare aux références des centres de gestion, calculées de la même façon.

## 5. Pourquoi les deux ne donnent pas le même chiffre

| Poste | Par la ration | Par la comptabilité |
|-|-|-|
| Concentrés | quantités distribuées × prix | factures, à la date de livraison : un mois à deux camions d'aliment paraît cher, le suivant bon marché |
| Fourrages produits | MS distribuée × coût à l'hectare ÷ rendement | absents du coût acheté ; dans le coût total, charges des cultures de l'exercice, qui nourriront parfois l'hiver suivant |
| Animaux | vaches traites seulement | tout ce qui est imputé à l'atelier lait : taries, et parfois génisses et veaux |
| Lait | collectes réparties jour par jour, prix payé du mois | paies facturées, souvent avec un mois de décalage, régularisations comprises |
| Lait non livré | compté dans le lait produit, pas dans le produit | invisible |

Ces écarts ne sont pas des erreurs : ils viennent de ce que chaque calcul regarde. Ils se compensent en grande partie sur un exercice, à trois exceptions près, qui restent : les taries et les génisses, absentes de la ration saisie ; les stocks d'aliments et de fourrages, qui n'ont pas la même valeur au début et à la fin ; et la valorisation des fourrages produits, qui n'a pas de prix de marché.

D'où la règle d'usage :

- **la ration pour piloter** : elle réagit dans la semaine à un changement de ration ou de prix, mois par mois et jour par jour ;
- **la comptabilité pour vérifier** : une fois l'exercice clos, ou sur 12 mois glissants, elle dit si la marge suivie était juste, et elle se compare aux références de groupe.

Un écart qui persiste sur l'année, une fois ces trois exceptions mises à part, signale presque toujours une quantité fausse dans la ration : une teneur en MS dépassée, des refus non comptés, un aliment oublié.

## 6. Ce que la ration permet : lait permis et coût du kilo de concentré

Les mêmes saisies donnent, avec les valeurs alimentaires des aliments, deux lectures de la ration elle-même.

**Le lait permis** est le lait que la ration permet de produire, par l'énergie (UFL) et par les protéines (PDI), une fois l'entretien couvert. Il se calcule ici selon le système INRA 2018 : valeurs des aliments par kg de matière sèche, corrigées des interactions digestives (niveau d'ingestion, part de concentré, balance protéique du rumen), besoins d'entretien selon le poids vif, besoin du litre selon les taux du tank. Le plus petit des deux est le facteur limitant. C'est un ordre de grandeur : les valeurs des tables, le poids vif et les refus estimés le déplacent de plusieurs litres. Il se lit dans le temps, ration contre ration, plus qu'en valeur absolue.

**Le prix d'un kilo de concentré en litres de lait** : prix du concentré à la tonne divisé par le prix du lait aux 1 000 litres. Un tourteau à 450 € / t, avec un lait payé 440 € / 1 000 L, coûte un peu plus d'un litre par kilo. Un kilo de concentré n'est rentable que s'il fait produire plus que ce chiffre, à ration de base égale.

## 7. Le tableur

Le calcul par la ration est appliqué dans un tableur Google Sheets, gratuit, à copier dans votre propre compte Google. Il est né de la refonte du tableau de bord d'un autre éleveur, jugé trop lourd à remplir : l'objectif est de quelques minutes de saisie par semaine.

{{< tableur-copie >}}

Le tableur est copié dans votre Google Drive : vos chiffres restent dans votre compte et ne passent pas par ce site. Il faut un compte Google. Il ne fonctionne pas dans Excel ni dans LibreOffice : plusieurs formules sont propres à Google Sheets.

### Mode d'emploi

Les cases jaunes se remplissent, le reste se calcule. Dans l'ordre :

1. **Aliments** : la liste des aliments de la ration (14 au plus), avec leur type ; effacez ceux que vous n'utilisez pas. Les prix, datés, en dessous : en euros par tonne de MS pour les fourrages produits et la pâture, par tonne brute pour les achats. Le poids vif moyen des vaches, pour le lait permis.
2. **Paie** : les paramètres de votre laiterie, à recopier une fois du bordereau (taux de référence, valeur du gramme de TB et de TP, grille de pénalités, primes, cotisations) ; puis, chaque mois, le prix de base.
3. **Ration** : une ligne à chaque changement, avec le nombre de vaches traites.
4. **Lait** : une ligne par collecte.
5. **Analyses** : une ligne par bulletin du tank ; elles servent à la paie et au suivi de l'urée et du TP.
6. **Résultats** : rien à saisir ; l'onglet affiche le dernier mois, ou celui que vous choisissez.

### Ce qu'il fait

- Les trois chiffres du mois — coût alimentaire aux 1 000 L produits, marge par vache et par jour, grammes de concentré par litre —, comparés au mois précédent et au même mois de l'année d'avant.
- La décomposition de la variation de marge en trois effets (section 3).
- La marge, le coût de la ration par catégorie d'aliment et le lait par vache sur 12 mois, en graphiques.
- Le lait permis et le coût d'un kilo de chaque concentré en litres de lait (section 6).
- Le prix payé du mois, recalculé à partir du prix de base, des analyses et de la grille de la laiterie, jusqu'au net à percevoir.
- La marge jour par jour sur 60 jours, avec la moyenne des 7 derniers jours comparée aux 7 précédents.
- L'urée et le TP du tank autour d'un changement de ration, analyse par analyse, avec un signal quand le TP baisse nettement.

### Ce qu'il ne fait pas

- **Les valeurs alimentaires de sa bibliothèque sont indicatives** : une partie vient des tables INRA 2018, une autre est convertie des valeurs de 2007 ou supposée, et la source est indiquée pour chacune. Une analyse de fourrage ou l'étiquette du fournisseur les remplace.
- **Les taries et les génisses** ne sont pas dans le calcul : la ration saisie est celle des vaches traites.
- **Les stocks** : le coût est celui de la ration distribuée, pas celui des achats.
- **Les autres charges de l'atelier** : voir la section suivante.

> **Cas observé.** Comparé, d'avril à octobre, au tableau de bord rempli jour par jour qu'il remplace, le tableur saisi une seule fois par semaine donne le même coût de ration à moins de 0,1 € par 1 000 litres près presque chaque mois. Sur la même période, le coût de la ration aux 1 000 litres a été multiplié par cinq entre le plein pâturage du printemps et la ration d'automne à base d'ensilage de maïs, et le lait non livré a représenté entre 1,5 et 3,6 % du lait produit selon les mois.

## 8. Ce que cette marge n'est pas : le coût de production

La marge sur coût alimentaire ne retire du prix du lait que la ration. Il reste à couvrir tout le reste : frais d'élevage (vétérinaire, reproduction, contrôle laitier), mécanisation, bâtiments et robot, frais de structure, et la rémunération du travail. Le **coût de production du lait**, calculé selon la méthode de l'Institut de l'élevage, rassemble ces postes et se compare au prix du lait. L'alimentation en est l'un des premiers postes, mais une bonne marge sur coût alimentaire ne garantit pas un coût de production couvert.

## 9. Ce que ce suivi ne remplace pas

- **Le dossier de gestion et les références de groupe**, qui calculent la marge sur l'exercice, avec les stocks, et la comparent à d'autres élevages.
- **Le rationnement par un conseiller**, qui part des analyses de fourrages, de l'état des vaches et de leur stade : le lait permis du tableur est un repère, pas une ration calculée.
- **Les analyses de fourrages** : sans elles, les valeurs de la bibliothèque restent des moyennes.

## À retenir

- La marge sur coût alimentaire se suit par vache et par jour pour piloter la ration, aux 1 000 litres livrés pour se comparer.
- Le coût alimentaire se rapporte au lait produit, livré ou non.
- Par la ration : on ne saisit que ce qui change, les fourrages se comptent en matière sèche, le lait d'une collecte se répartit sur les jours qu'elle couvre, et l'on pondère par les litres.
- La variation de marge se décompose exactement en trois effets : prix du lait, lait par vache, coût de la ration.
- La ration et la comptabilité divergent pour de bonnes raisons : stocks, livraisons, animaux couverts, décalage de la paie. La première pilote, la seconde vérifie.
- Un écart persistant entre les deux sur l'année signale le plus souvent une quantité fausse dans la ration.
- La marge sur coût alimentaire n'est pas le coût de production : elle ne retire que la ration.

## Pages liées

- [Calculer l'EBE de son exploitation agricole en cours d'année](/tresorerie/ebe-en-cours-d-annee/) — la marge sur coût alimentaire vue de la comptabilité, avec le reste de l'EBE.

- [Outil en ligne : l'EBE en cours d'année depuis la comptabilité](/tresorerie/outil-ebe-en-cours-d-annee/) — le prix du lait et la marge sur coût alimentaire acheté, calculés depuis vos balances ou vos grands livres.

- [Suivre son troupeau entre deux contrôles laitiers avec les données du robot de traite](/elevage/suivre-son-troupeau-entre-deux-controles/) — production, taux et concentré distribué, vache par vache, depuis le robot.

---

*Cette page décrit une méthode de gestion appliquée à une exploitation. Elle ne constitue pas un conseil personnalisé, ni un plan de rationnement.*
