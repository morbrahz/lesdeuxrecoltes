+++
title = "Outil en ligne : compteur de renouvellement du troupeau laitier, depuis Lely Horizon"
seoTitle = "Outil : compteur de renouvellement du troupeau laitier"
date = 2026-10-14
lastmod = 2026-10-14
draft = false
weight = 6
summary = "Assez de génisses pour renouveler le troupeau ? Femelles nées et attendues sur 12 mois face au besoin, depuis Lely Horizon. Calcul dans le navigateur."
+++

Cet outil répond à une question simple : les gestations en cours et les vêlages de l'année donneront-ils assez de femelles pour renouveler le troupeau ? Il additionne, sur 12 mois glissants, les femelles déjà nées et celles qu'on peut attendre selon la semence utilisée, compare le total au besoin du troupeau, et traduit l'écart en nombre d'inséminations à passer en viande ou, au contraire, à ajouter.

**Vos données restent dans votre navigateur.** Le calcul s'exécute sur votre appareil ; rien n'est envoyé, ni sur ce site ni ailleurs. Pour que vous retrouviez vos saisies d'une visite à l'autre, l'outil les garde dans la mémoire de ce navigateur, et vous pouvez en enregistrer une copie sur votre ordinateur.

*Dernière mise à jour : 14 octobre 2026.*

## 1. L'export à préparer

Un seul fichier : le rapport standard **17 - Planning - Aperçu troupeau** de Lely Horizon, exporté au format CSV. Il liste tout le troupeau, génisses comprises, et apporte à la fois les gestantes avec leur date de vêlage attendue et les jours de lactation des vaches, qui servent à repérer les vêlages.

Colonnes utilisées : N° d'animal, Etat de reproduction, Date de vêlage attendue, N°. lac. (vide pour une génisse) et Jours de lactation ; Etat de production, s'il est présent, sert seulement à distinguer les vaches en lactation des taries. L'outil reconnaît les colonnes par leur nom, sans tenir compte des accents ni des majuscules. Quelques précautions :

- **La date de l'export** sert à dater les vêlages : date de l'export − jours de lactation. L'outil la lit dans le nom du fichier, qu'Horizon compose avec la date au format `jj_mm_aaaa` ; si le fichier a été renommé, saisissez-la dans le champ prévu.
- **Les vêlages sont repérés d'un import à l'autre** : une gestante qui n'est plus gestante dans le nouvel export, et dont la vache a vêlé à moins de 40 jours de la date prévue, passe en vêlage. Une gestante qui disparaît sans vêlage est seulement signalée.
- **Refaire l'import après chaque diagnostic de gestation** tient la fenêtre à jour. L'outil fusionne : les gestations déjà connues gardent leur type de semence, seules les nouvelles sont ajoutées.

L'outil accepte aussi deux listes importées ensemble, **Planning génisse et taries** (génisses et taries gestantes, avec leur date de vêlage attendue) et **VL en lactation** (vaches gestantes, datées par les jours depuis l'insémination + 282 jours). Sans Lely Horizon, tout peut se saisir à la main, gestation par gestation.

## 2. L'outil

Au premier affichage, l'outil montre un **élevage fictif** de 60 vaches, calé sur la date du jour. Pour passer à vos données, cliquez sur **Importer mon export Horizon** (ou ouvrez l'onglet « Import et sauvegarde ») et choisissez le fichier CSV : l'exemple s'efface au premier import, comme à la première saisie.

{{< outil-renouvellement >}}

**Conseiller d'élevage, organisme de contrôle laitier, concessionnaire ?** Si vous souhaitez utiliser cet outil pour les élevages que vous suivez, écrivez à [contact@lesdeuxrecoltes.fr](mailto:contact@lesdeuxrecoltes.fr).

## 3. La fenêtre de 12 mois et le calcul

**La fenêtre** se termine à la date de vêlage prévue de la dernière gestante confirmée et commence un an plus tôt, les deux dates comprises. Elle avance donc avec chaque nouvelle gestation confirmée.

**Les femelles nées** : chaque vêlage de la fenêtre qui a donné une femelle, issue de semence sexée ou conventionnelle, compte pour 1. Des jumeaux se saisissent comme deux vêlages.

**Les femelles attendues** : chaque gestation de la fenêtre compte selon la probabilité d'obtenir une femelle avec sa semence.

| Semence | Femelles attendues par gestation | Repère |
|---|---|---|
| Sexée | 0,9 | 89 % de femelles en Prim'Holstein et Montbéliarde sur plus de 4 500 naissances (Institut de l'élevage) ; 91 % sur génisses et 89,3 % sur vaches aux États-Unis |
| Conventionnelle | 0,5 | 51 % de femelles sur génisses et 48 % sur vaches dans la même étude américaine |
| Viande | 0 | Le veau n'est pas destiné au renouvellement |

Les deux premiers coefficients se règlent dans l'onglet « Réglages ». Un vêlage dont le sexe n'est pas encore saisi compte, lui aussi, au coefficient de sa semence. Une gestation dont la semence n'est pas indiquée n'est pas comptée : l'outil le signale.

**Le besoin** est le nombre de vaches (en lactation et taries) multiplié par le taux de renouvellement visé, plus une marge de sécurité. Avec les valeurs par défaut, sur l'élevage fictif : 60 vaches × 30 % = 18 femelles, plus 3 de marge, soit **21 femelles sur 12 mois**.

## 4. Les règles de saisie

- **Le type de semence est toujours choisi par l'éleveur.** Une gestante importée arrive en « semence à saisir » ; un vêlage reprend la semence de sa gestation.
- **Le sexe du veau n'est jamais déduit.** Il est saisi par l'éleveur et reste « à saisir » jusque-là.
- **En semence viande, le sexe n'est pas suivi** : aucun bouton femelle ou mâle, rien n'est demandé, et le vêlage compte 0.
- **Le bouton « Vêlée »**, sur une gestation, enregistre le vêlage : on indique la date, puis Femelle ou Mâle (ou « Enregistrer » en semence viande).
- **Rien n'est supprimé automatiquement.** Une gestation qui disparaît d'Horizon sans vêlage correspondant est marquée « absente du dernier import » : c'est à l'éleveur de vérifier (avortement, réforme) et de la supprimer.

## 5. Lire le résultat

- **Le verdict** : *Suffisant* si le total atteint le besoin, marge comprise ; *Marge entamée* s'il se situe entre le besoin sans marge et le besoin avec marge ; *Insuffisant* en dessous du besoin sans marge. Des pastilles rappellent le nombre de semences et de sexes encore à saisir.
- **Le pilotage** traduit l'écart en inséminations. Un excédent de 2 femelles, par exemple, autorise 4 IA conventionnelles (2 ÷ 0,5) ou 2 IA sexées (2 ÷ 0,9, arrondi à l'unité inférieure) à passer en viande sans descendre sous le besoin. Un déficit indique combien de gestations en sexée ou en conventionnelle il faudrait ajouter.
- **La vue par trimestre** montre quand naissent les femelles : nées, attendues en sexée, attendues en conventionnelle, face au quart du besoin annuel. Les trimestres coupés par la fenêtre sont marqués « partiel ».
- **L'historique** garde une photo du bilan par jour de mise à jour, pendant un an : on y voit si le total tient face au besoin au fil des diagnostics et des vêlages.

## 6. Les limites

- **C'est une estimation.** Le résultat dépend du type de semence saisi, et le sexe d'un veau à naître reste une probabilité.
- **L'outil suppose que les gestations confirmées vont à terme.** Les avortements tardifs et la mortalité des veaux ne sont pas comptés : c'est le rôle de la marge de sécurité.
- **Le stock de génisses n'est pas géré, volontairement.** Seul compte le nombre de femelles nées ou attendues sur la fenêtre de 12 mois, pas l'âge ni le nombre des génisses déjà présentes.
- **Les données ne suivent pas d'un appareil à l'autre.** Elles restent dans le navigateur où elles ont été saisies et disparaissent si l'on efface les données du site : enregistrez régulièrement une copie (onglet « Import et sauvegarde ») pour la restaurer ailleurs ou plus tard.

*Sources des coefficients : semence sexée en France, Institut de l'élevage, cité par [Réussir Lait](https://www.reussir.fr/lait/la-semence-sexee-le-vent-en-poupe) (janvier 2012) ; semences sexée et conventionnelle aux États-Unis, H. D. Norman, J. L. Hutchison et R. H. Miller, [Journal of Dairy Science, 93, p. 3880-3890](https://www.aipl.arsusda.gov/publish/jds/2010/93_3880.pdf) (2010), naissances simples.*
