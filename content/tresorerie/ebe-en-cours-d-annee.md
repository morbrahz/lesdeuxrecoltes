+++
title = "Calculer l'EBE de son exploitation agricole en cours d'année"
seoTitle = "Calculer l'EBE de son exploitation agricole en cours d'année"
date = 2026-10-03
lastmod = 2026-10-14
draft = false
weight = 4
summary = "Calculer l'EBE de l'exploitation agricole en cours d'année : à date ou sur 12 mois glissants, annuités au prorata, marge sur coût alimentaire du lait, bénéfice brut estimé."
+++

Le dossier de gestion arrive plusieurs mois après la clôture, quand les décisions de l'exercice sont prises depuis longtemps. Pourtant, la comptabilité tenue au fil de l'eau contient déjà presque tout : une balance ou un grand livre sortis en cours d'année suffisent à savoir si l'exercice se présente mieux ou moins bien que le précédent. Cette page décrit comment en tirer un EBE de gestion, à date ou sur 12 mois glissants, comment passer au bénéfice brut, et comment lire ces chiffres sans leur faire dire ce qu'ils ne disent pas. Un [outil en ligne](/tresorerie/outil-ebe-en-cours-d-annee/) fait le calcul à partir de vos propres fichiers.

*Dernière mise à jour : 14 octobre 2026.*

## 1. Ce que l'on cherche : une température, pas un résultat

Le but n'est pas d'anticiper le bilan à l'euro près. Il est de répondre à trois questions, assez tôt pour agir :

1. **L'exercice va-t-il mieux ou moins bien que le précédent, à la même date ?**
2. **Ce qui a été dégagé couvre-t-il les annuités et les prélèvements des mois écoulés ?**
3. **Où se trouve l'écart** : dans un prix, dans un volume, dans un poste de charges ?

Les réponses servent à décider d'un achat, d'un prélèvement, d'une DEP ou d'un rendez-vous avec la banque avant la clôture, et non après. Elles servent aussi à dimensionner la réserve décrite dans [Combien de trésorerie garder sur une exploitation agricole](/tresorerie/combien-garder/) : un exercice qui s'annonce faible appelle une réserve plus épaisse.

## 2. La matière première : la balance à date ou le grand livre

Il faut une **balance générale** arrêtée à une date de l'exercice en cours, avec, si possible, les colonnes de comparaison : le solde de chaque compte à la même date un an et deux ans plus tôt. Le comptable la sort en quelques minutes ; certains logiciels la proposent directement à l'exploitant.

En option, une **balance analytique** par année : les mêmes comptes, ventilés par code activité (blé, maïs ensilage, vaches laitières, lait…), avec les quantités. Elle donne les marges par atelier et le prix du lait au litre.

Deux précautions :

- **Toujours comparer à la même date.** Une balance au 1er octobre se compare à la balance au 1er octobre de l'année précédente, jamais à un exercice clos.
- **Sortir la balance après la saisie des dernières factures** : une balance arrêtée avant la saisie d'un mois de factures fausse la comparaison bien plus que tout le reste.

**Mieux encore : le grand livre analytique.** Une balance ne donne qu'un total arrêté à une date. Le grand livre donne chaque écriture avec sa date, son code activité et ses quantités : on y calcule n'importe quelle période, mois par mois, sans attendre la même date l'année suivante. Il suffit d'un export par exercice, limité aux comptes 6 et 7 : quelques centaines de kilo-octets pour une année. Un seul export par exercice remplace toute la série de balances, et l'exercice en cours se remet à jour en exportant à nouveau son seul fichier.

## 3. L'EBE de gestion

L'excédent brut d'exploitation mesure ce que l'activité dégage avant le financement, les amortissements et la rémunération de l'exploitant. Tiré d'une balance en cours d'année, il se calcule ainsi :

| Composante | Comptes | Traitement |
|-|-|-|
| Produits d'exploitation | 70 à 75 | retenus, sauf 757 (cessions d'immobilisations) |
| Charges d'exploitation | 60 à 65 | retenues, sauf la rémunération du travail et les cotisations sociales personnelles de l'exploitant |
| Variations de stocks | 603 et 71 | écartées : elles ne sont passées qu'à la clôture |
| Financier | 66 et 76 | écartés : ils relèvent du financement |
| Exceptionnel, amortissements, reprises | 67, 68, 77, 78, 79 | écartés |

On l'appelle ici **EBE de gestion** pour le distinguer de celui du bilan, parce que trois choses lui manquent :

- **les variations de stocks** : les ventes enregistrées à date portent souvent sur la récolte précédente, quand les charges portent sur la campagne en cours ;
- **les amortissements**, qui ne décaissent rien et n'entrent pas dans l'EBE de toute façon, mais qui manquent pour passer au résultat ;
- **les écritures de clôture** : fermage provisionné, rémunération de l'exploitant, régularisations de fin d'exercice.

C'est pour cela qu'il se compare **d'une année sur l'autre à la même date**, où les mêmes manques jouent à peu près de la même façon, et jamais au bilan.

> **Cas observé.** Deux balances arrêtées au même jour, à un an d'écart, donnaient un EBE de gestion allant de 1 à 3,5. L'écart ne venait pas de l'exploitation : une échéance de fermage tombait juste avant la date de la balance une année, juste après l'autre, et la paie d'un mois de lait n'était pas encore comptabilisée. Avant de conclure sur un écart, il faut lire le détail par poste.

## 4. Ramener les annuités et les prélèvements aux mois écoulés

Un EBE de gestion de neuf mois ne se compare pas à des annuités annuelles. On ramène les deux au même nombre de mois :

- **mois couverts** = mois écoulés depuis le début de l'exercice jusqu'à la date de la balance ;
- **annuités à date** = annuités annuelles × mois couverts ÷ 12 ;
- **disponible après annuités** = EBE de gestion − annuités à date ;
- **après prélèvements** = disponible après annuités − prélèvements privés à date.

> **Exemple chiffré (fictif).** Exercice commencé en janvier, balance au 1er octobre : neuf mois couverts. EBE de gestion à date : 60 000 €. Annuités : 40 000 € par an, soit 30 000 € sur neuf mois. Prélèvements privés : 24 000 € par an, soit 18 000 € sur neuf mois. Disponible après annuités : 30 000 € ; après prélèvements : 12 000 €. Les annuités absorbent la moitié de l'EBE, et l'exercice dégage encore de la trésorerie, sans marge pour un dernier trimestre difficile.

Le prorata suppose des annuités et des prélèvements réguliers. Une annuité annuelle unique, ou un prélèvement exceptionnel, se traite à part.

## 5. Les 12 mois glissants

Le cumul de l'exercice a un défaut : en début d'exercice, il porte sur peu de mois, et une seule échéance suffit à le déformer. Les **12 mois glissants** additionnent les douze derniers mois, quelle que soit la date de clôture, et se comparent aux douze mois précédents.

- **Les saisons se compensent** : chaque période contient un fermage, une moisson, un hiver.
- **Le chiffre se compare directement aux annuités et aux prélèvements annuels**, sans prorata.
- **Il se recalcule chaque mois** : à la fin de chaque mois, la courbe des 12 mois glissants montre si la tendance se redresse ou continue de se dégrader.

Sa limite : la période contient une clôture, avec ses écritures (fermage provisionné, régularisations). Le stock de clôture et sa reprise au premier jour de l'exercice suivant tombent tous deux dans la période et s'annulent ; le chiffre revient donc à supposer des stocks stables.

Il faut un grand livre pour le calculer : une balance à date ne dit rien des mois de l'exercice précédent qui ont suivi la même date.

## 6. Le lait : prix et marge sur coût alimentaire

Avec la balance analytique, les ventes de lait (compte 7020) et leurs quantités en litres donnent le **prix du lait perçu**, ramené à 1 000 litres. Deux coûts alimentaires s'en déduisent :

- **le coût alimentaire acheté** : aliments, matières premières, minéraux et fourrages achetés, imputés au troupeau laitier ; l'aliment des veaux et des génisses en est écarté ;
- **le coût des fourrages produits** : les charges des cultures fourragères (semences, engrais, produits de défense, travaux, récolte).

La **marge sur coût alimentaire acheté** est celle que suivent la plupart des références. La **marge sur coût total**, fourrages produits compris, est plus complète, mais deux limites la rendent moins précise en cours d'année : les fourrages nourrissent tout le troupeau, génisses comprises, et une partie des charges engagées au printemps nourrira l'hiver suivant.

**Le décalage de la paie de lait.** La paie d'un mois arrive souvent le mois suivant. Selon la date de la balance, il peut manquer un mois de lait : quelques milliers d'euros d'EBE en moins et un prix au litre faussé. On corrige en ajoutant le lait livré et non encore facturé, montant et litres, à la seule balance concernée.

## 7. Les ateliers

La balance analytique range chaque code activité dans un atelier : cultures de vente, élevage, activités annexes, structure. Une règle de méthode : **les cultures fourragères vont dans l'élevage**, qui les consomme. Laissées à part, elles forment un atelier toujours déficitaire, et la marge de l'élevage paraît meilleure qu'elle n'est.

Côté cultures de vente, la marge à date dit où en est la trésorerie, pas ce que rapporte la campagne : les ventes de l'année portent souvent sur la récolte précédente.

## 8. De l'EBE au bénéfice brut

Le bénéfice brut sert à anticiper ce qui en dépend : l'impôt sur le revenu et les cotisations sociales de l'exploitant. Il part de l'EBE de gestion et y ajoute ce que celui-ci écarte :

> bénéfice brut = EBE de gestion − amortissements ± variations de stocks + résultat financier + exceptionnel + reprises et transferts de charges

On le prend **avant rémunération du travail et avant cotisations personnelles de l'exploitant** : ces deux postes relèvent de l'exploitant, pas de l'exploitation. Les cotisations personnelles passées en charges sont d'ailleurs souvent réintégrées par le comptable à la clôture.

- **Sur un exercice clos**, le grand livre donne le chiffre exact, clôture comprise. Il peut encore différer du bénéfice fiscal de quelques retraitements extra-comptables, comme la DEP.
- **Sur 12 mois glissants**, le chiffre est réel lui aussi : la période contient une clôture et ses amortissements.
- **En cours d'exercice**, ce n'est qu'une estimation : on retire les amortissements de l'exercice ramenés aux mois écoulés, et l'on suppose les stocks stables jusqu'à la clôture. C'est l'hypothèse qui pèse le plus : une récolte stockée ou vendue d'ici la clôture déplace le résultat de plusieurs dizaines de milliers d'euros.

**Les amortissements de l'exercice** se lisent dans le tableau des immobilisations que le comptable établit avec chaque bilan : il donne la dotation de l'exercice suivant pour tous les biens déjà en place. On y ajoute les biens mis en service depuis, au prorata. Les annuités ne s'en approchent pas : elles remboursent le capital au rythme de la banque, quand l'amortissement suit la durée de vie du bien.

> **Exemple chiffré (fictif).** Neuf mois d'exercice écoulés. EBE de gestion à date : 60 000 €. Amortissements de l'exercice : 48 000 €, soit 36 000 € sur neuf mois. Frais financiers à date : 3 000 €. Bénéfice brut estimé : 21 000 €, avant variation de stocks de fin d'exercice.

**Pour les cotisations sociales**, l'assiette des exploitants agricoles part depuis 2026 du revenu professionnel avant déduction des cotisations, diminué d'un abattement forfaitaire de 26 %, avec un plancher et un plafond. Pour l'impôt, on part du bénéfice fiscal, après la DEP et les autres retraitements. Dans les deux cas, le bénéfice brut donne un ordre de grandeur à faire valider avec le comptable, pas un montant à déclarer.

## 9. Ce que ce suivi ne remplace pas

- **Le dossier de gestion et le bilan**, qui intègrent les stocks, les amortissements et la clôture.
- **Les références de groupe** (centre de gestion, contrôle laitier), dont les définitions de marge peuvent différer de celles retenues ici.
- **Un prévisionnel de trésorerie** : l'EBE de gestion décrit ce qui s'est passé, pas les échéances à venir.

## À retenir

- Une balance ou, mieux, un grand livre en cours d'année suffit pour prendre la température de l'exploitation.
- L'EBE de gestion se compare à la même date de l'année précédente, jamais au bilan : il n'a ni stocks, ni amortissements, ni écritures de clôture.
- Les annuités et les prélèvements se ramènent aux mois couverts par la balance ; sur 12 mois glissants, ils se comparent tels quels.
- Les 12 mois glissants effacent les saisons et se recalculent chaque mois.
- Un grand écart d'une année sur l'autre se lit d'abord dans le détail par poste : une échéance ou une paie de lait décalée suffit à le créer.
- Les cultures fourragères se rangent dans l'élevage ; la marge sur coût alimentaire se lit en coût acheté et en coût total.
- Le bénéfice brut s'estime en cours d'exercice avec les amortissements de l'exercice et des stocks supposés stables ; c'est un ordre de grandeur pour anticiper impôt et cotisations.

## Pages liées

- [Outil en ligne : l'EBE en cours d'année depuis la comptabilité](/tresorerie/outil-ebe-en-cours-d-annee/) — le calcul de cette page appliqué à vos grands livres ou à vos balances, dans votre navigateur.

- [Combien de trésorerie garder sur une exploitation agricole](/tresorerie/combien-garder/) — fixer la réserve en mois de charges, annuités comprises.

- [Suivre son troupeau entre deux contrôles laitiers avec les données du robot de traite](/elevage/suivre-son-troupeau-entre-deux-controles/) — le pendant technique du suivi économique de l'atelier lait.

---

*Cette page décrit une méthode de gestion appliquée à une exploitation. Elle ne constitue pas un conseil personnalisé.*
