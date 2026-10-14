+++
title = "Outil en ligne : l'EBE en cours d'année depuis la comptabilité"
seoTitle = "Outil : l'EBE en cours d'année depuis le grand livre ou la balance"
date = 2026-10-03
lastmod = 2026-10-14
draft = false
weight = 5
annonce = false
summary = "Déposez le grand livre ou la balance de l'exploitation : EBE à date ou sur 12 mois glissants, mois par mois, bénéfice brut estimé, marge sur coût alimentaire. Calcul dans le navigateur."
+++

Cet outil applique la méthode décrite dans [Calculer l'EBE de son exploitation agricole en cours d'année](/tresorerie/ebe-en-cours-d-annee/) à vos propres fichiers : EBE de gestion à date ou sur 12 mois glissants, comparaison avec les années précédentes, annuités et prélèvements ramenés aux mois écoulés, prix du lait, marge sur coût alimentaire et marges par atelier. Avec les grands livres, il ajoute l'évolution mois par mois et le bénéfice brut.

**Vos fichiers ne quittent pas votre ordinateur.** Le calcul s'exécute dans votre navigateur ; rien n'est envoyé ni conservé. Au premier calcul, le navigateur télécharge le moteur de calcul depuis ce site (une douzaine de Mo, gardés ensuite en mémoire).

*Dernière mise à jour : 14 octobre 2026.*

## 1. Les fichiers à préparer

Deux façons de faire, au choix :

- **Les grands livres analytiques (conseillé)** : un export par exercice, limité aux comptes 6 et 7, au format CSV ou Excel, avec la date, le code activité et les quantités de chaque écriture. Déposez l'exercice en cours et les deux précédents. Nommez-les avec leurs dates (« GLA010225-310126 » pour un exercice du 1er février 2025 au 31 janvier 2026) : l'outil y lit le début de l'exercice. Pour mettre à jour, il suffit de réexporter l'exercice en cours.
- **Les balances** : la balance générale à date, obligatoire, avec si possible les colonnes de comparaison à un et deux ans (« Solde P-1 », « Solde P-2 ») ; en option, une balance analytique par année, à la même date. L'outil les reconnaît à leur colonne « Activité ».

Ne mélangez pas les deux dans un même calcul.

Le format de référence est celui des exports d'**Isacompta**. Les colonnes sont lues par leur nom : un grand livre d'un autre logiciel passe s'il a les colonnes « N° de compte », « Date de pièce », « Débit » et « Crédit » ; une balance, s'il a une colonne « Compte » et une colonne « Solde », ou « Débit » et « Crédit ». Les codes activité sont rangés en ateliers d'après leur premier chiffre, selon la codification observée dans Isacompta ; avec une autre codification, le détail par code reste juste, mais le classement par atelier peut ne pas l'être.

## 2. L'outil

{{< outil-temperature-exploitation >}}

## 3. Lire les résultats

- **Avec les grands livres**, choisissez la lecture (cumul de l'exercice ou 12 mois glissants) et la date d'arrêté : la dernière écriture saisie, ou une fin de mois.
- **Avec une balance**, sa date est lue dans le fichier ou dans son nom (« balance générale 011026 » pour le 1er octobre 2026). Si elle n'est pas trouvée, saisissez-la : elle sert à compter les mois couverts.
- **L'EBE de gestion** n'est pas celui du bilan : il n'a ni stocks, ni amortissements, ni écritures de clôture. Il se compare à la même date de l'année précédente. Les comptes écartés du calcul (financier, exceptionnel, amortissements, cessions, rémunération de l'exploitant) sont listés sous le détail par compte.
- **Un grand écart sur un an** se lit d'abord dans le tableau par poste : une échéance de fermage ou une paie de lait de part et d'autre de la date suffit à le créer.
- **Le lait** n'apparaît qu'avec les balances analytiques et des quantités en litres sur le compte 7020. Cochez les codes du troupeau laitier : leurs aliments achetés forment le coût alimentaire. Les lignes dont le libellé parle de veaux ou de génisses sont toujours écartées.
- **Le lait livré non facturé**, s'il est saisi, s'ajoute à la seule période la plus récente.
- **Le bénéfice brut** (grands livres seulement) est exact pour les exercices clos et sur 12 mois glissants ; en cumul de l'exercice, c'est une estimation. Saisissez les amortissements de l'exercice, lus dans le tableau des immobilisations du comptable ; à défaut, l'outil reprend ceux du dernier exercice clos. Les stocks sont supposés stables jusqu'à la clôture.

Ce que l'outil ne fait pas : il ne reconstitue pas les stocks de fin d'exercice, ne calcule ni l'impôt ni les cotisations, ne lit pas les surfaces, et ne remplace pas le dossier de gestion.

*Le calcul s'exécute avec [Pyodide](https://pyodide.org), distribué sous licence MPL 2.0 et hébergé sur ce site. [Code source du calcul](/outils/temperature-exploitation/temperature_exploitation.py).*
