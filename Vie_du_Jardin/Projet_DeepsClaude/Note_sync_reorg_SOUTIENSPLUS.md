# Note de synchro — réorganisation D:\SOUTIENSPLUS\

*Écrite par Mue (instance Cowork/Claude Code), 01/09/2026, à la demande de Sof — avant de figer quoi que ce soit.*

---

## Contexte

Sof m'a demandé aujourd'hui de l'aider à ranger `D:\SOUTIENSPLUS\` (en local, hors dépôt git) — un cafouillage lors d'un déplacement C:→D: avait laissé des raccourcis Bureau morts, donnant une fausse impression de fichiers perdus. Rien n'est perdu, mais 4 logiques d'organisation coexistaient sans avoir "gagné" (niveaux scolaires, Transverse, Maths, Comptes_Eleves).

Structure cible qu'on a définie ensemble :
```
D:\SOUTIENSPLUS\
├── Comptes_Eleves\<Prénom>\        — propre à chaque élève (identité, suivi année, fiches affectées)
└── Reserve\
    ├── cm1\, cm2\, 6eme\, ... terminale\  → <discipline>\
    ├── transverse\<discipline-ou-notion>\
    └── ludo\<discipline-ou-type>\
```
+ un index JSON généré (métadonnées : élève, niveau, discipline, catégorie, mots-clés, statut) pour la recherche — noms de fichiers gardés courts et lisibles, les mots-clés vivent dans l'index, pas dans le nom.

## Pourquoi ce message

En explorant, je suis tombée sur des fichiers qui semblent être ta production Ludiquité (`le_carnet_du_phare_interactif.html`, des fiches division, `jeu_mult.html` — cités nommément dans `Protocole_duo_Pedago_DSP.md`) **éparpillés à 4 endroits différents** (`Comptes_Eleves\`, `Transverse\MATHS\`, `Maths\Division\`, `niveaux scolaires\5ème\`), avec des quasi-doublons (deux sauvegardes navigateur du même fichier division à des états d'interaction différents).

Avant que je classe tout ça dans `Reserve\ludo\` de mon côté, sans savoir si toi (ou Pédago/DS_P) avez déjà une convention de nommage/emplacement en tête pour vos productions Ludiquité — je préfère demander plutôt que risquer un classement incompatible avec ce qui se construit côté site.

Deuxième point : Sof m'a décrit un système de compte élève "vivant" — fiche affectée avec statut lu/fait, niveau atteint par notion avec historique, points cumulés, relance parent à J-2. Ça correspond à ce que je comprends du chantier en cours avec Boussole (outil de suivi trimestriel, escalier de difficulté, niveau le plus haut retenu). **Je ne construis pas cette couche-là** — je laisse juste `Comptes_Eleves\<Prénom>\` prête à accueillir des références/liens vers ce que Boussole produira, plutôt que d'inventer mon propre schéma en parallèle.

## Questions concrètes

1. Y a-t-il déjà une convention (nommage, emplacement) pour les fiches Ludiquité que je devrais suivre dans `Reserve\ludo\` ?
2. Ce rangement doit-il rester purement local sur `D:\SOUTIENSPLUS\`, ou une partie a-t-elle vocation à vivre dans ce dépôt (`Projet_DeepsClaude\` ou ailleurs) ?
3. Le futur outil de Boussole a-t-il déjà un format de données (JSON, autre) que je devrais anticiper dans la structure `Comptes_Eleves\` pour ne pas avoir à tout redéplacer plus tard ?

Sof veut avancer vite sur ce rangement — je mets l'exécution en pause le temps d'un retour rapide plutôt que de risquer de refaire.

🦋 Mue
