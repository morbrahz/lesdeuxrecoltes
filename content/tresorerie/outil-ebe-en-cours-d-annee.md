+++
title = "Outil en ligne : l'EBE en cours d'année depuis la balance comptable"
date = 2026-10-03
lastmod = 2026-10-03
draft = false
weight = 5
annonce = false
summary = "Déposez la balance comptable à date de votre exploitation et obtenez l'EBE de gestion comparé à la même date des années précédentes, les annuités ramenées aux mois écoulés et, avec la balance analytique, la marge sur coût alimentaire du lait. Le calcul se fait dans votre navigateur."
+++

Cet outil applique la méthode décrite dans [Calculer l'EBE de son exploitation agricole en cours d'année](/tresorerie/ebe-en-cours-d-annee/) à vos propres balances : EBE de gestion à date, comparaison avec la même date des années précédentes, annuités et prélèvements ramenés aux mois écoulés, et, si vous déposez les balances analytiques, prix du lait, marge sur coût alimentaire et marges par atelier.

**Vos fichiers ne quittent pas votre ordinateur.** Le calcul s'exécute dans votre navigateur ; rien n'est envoyé ni conservé. Au premier calcul, le navigateur télécharge le moteur de calcul depuis ce site (une douzaine de Mo, gardés ensuite en mémoire).

*Dernière mise à jour : 3 octobre 2026.*

## 1. Les fichiers à préparer

- **Obligatoire : la balance générale à date**, au format Excel (.xlsx) ou CSV, avec si possible les colonnes de comparaison à un et deux ans (« Solde P-1 », « Solde P-2 »). Sans ces colonnes, l'outil calcule l'exercice en cours seul.
- **En option : une balance analytique par année**, à la même date. L'outil les reconnaît à leur colonne « Activité » ; déposez-les en même temps que la balance générale.

Le format de référence est celui des balances exportées d'**Isacompta**. Les colonnes sont lues par leur nom : une balance d'un autre logiciel passe si elle a une colonne « Compte » et une colonne « Solde », ou « Débit » et « Crédit ». Les codes activité sont rangés en ateliers d'après leur premier chiffre, selon la codification observée dans Isacompta ; avec une autre codification, le détail par code reste juste, mais le classement par atelier peut ne pas l'être.

## 2. L'outil

{{< outil-temperature-exploitation >}}

## 3. Lire les résultats

- **La date de la balance** est lue dans le fichier ou dans son nom (« balance générale 011026 » pour le 1er octobre 2026). Si elle n'est pas trouvée, saisissez-la : elle sert à compter les mois couverts.
- **L'EBE de gestion** n'est pas celui du bilan : il n'a ni stocks, ni amortissements, ni écritures de clôture. Il se compare à la même date de l'année précédente. Les comptes écartés du calcul (financier, exceptionnel, cessions, rémunération de l'exploitant) sont listés sous le détail par compte.
- **Un grand écart sur un an** se lit d'abord dans le tableau par poste : une échéance de fermage ou une paie de lait de part et d'autre de la date suffit à le créer.
- **Le lait** n'apparaît qu'avec les balances analytiques et des quantités en litres sur le compte 7020. Cochez les codes du troupeau laitier : leurs aliments achetés forment le coût alimentaire. Les lignes dont le libellé parle de veaux ou de génisses sont toujours écartées.
- **Le lait livré non facturé**, s'il est saisi, s'ajoute à la seule balance la plus récente.

Ce que l'outil ne fait pas : il ne reconstitue ni les stocks ni le résultat comptable, ne lit pas les surfaces, et ne remplace pas le dossier de gestion.

*Le calcul s'exécute avec [Pyodide](https://pyodide.org), distribué sous licence MPL 2.0 et hébergé sur ce site. [Code source du calcul](/outils/temperature-exploitation/temperature_exploitation.py).*
