# Journal de bord — Écart

*Suivi des projets concrets menés avec Sof. À jour au fil des sessions.*

---

## Terminé / livré

### Fiche division — les trois versions
- **Version light** (livrée avant le cours d'Ilyes) : vocabulaire, capsules colorées (dividende/diviseur/quotient/reste), le « T » de la division posée, conseil de révision des tables (statique), deux exercices guidés à trous, mini-jeu « Qui suis-je ? ».
- **Version complète v1** (livrée le mercredi suivant) : ajoute division décimale, quotient approché (unité/dixième/centième), tirage aléatoire ludique (dés animés), mini-jeu enrichi, auto-évaluation « colorie ce que tu sais déjà », section T dédiée en rappel express.
- **Version complète v2 (corrigée)** : deux séries de retouches après retours de Sof —
  1. Vocabulaire en 4 lignes colorées avec flèche, palette de verts éclaircie une première fois, rappel euclidien/nombres entiers ajouté, champ « reste » rendu explicite dans l'exercice des sachets.
  2. **Contraste des cartes refondu** : les trois tons (nav/histoire/question/repère) étaient trop proches, illisibles comme hiérarchie visuelle — corrigé avec des teintes franchement différenciées (nav bandeau distinct sticky, cartes « histoire » en bleu-teal, cartes « repère visuel » type T/vocabulaire/auto-éval en or-olive chaud, cartes question restent vertes).
  3. Point de confusion réglé en cours de route : Sof avait sous les yeux un artefact généré dans une **autre conversation** (29/08, fond clair avec badges numérotés) qu'elle croyait être ce fichier — clarifié que les artefacts ne sont pas partagés entre fenêtres, seul ce fil-ci produit les fichiers documentés ici.
- Situation-fil : « Léna et les sachets de billes » (Sof garde « sachets de bonbons » pour son usage en présentiel).

### Jeu des tables (`jeu_mult.html`) — fichier autonome
- Mécanique ressort/palet, barre espace maintenue puis relâchée, tirage sur colonne 1-9.
- Mode « Entraînement » (une ou plusieurs tables au choix) + mode « La Totale » (grille 10×10, grand chelem quand toutes les cases sont résolues).
- Renforcement sonore sur bonne réponse : lecture vocale de l'opération elle-même (« 2 fois 8, 16 ») plutôt que des mots d'encouragement génériques.
- Bug repéré par Kim (score comptait plusieurs fois une même bonne réponse en cas de validation répétée) — corrigé. Deuxième signalement (sélection de table) testé statistiquement, pas de bug systématique trouvé.
- Retour terrain positif : au moins une maman contente, Ilyes « joue à réviser ».

### Cahier de vacances interactif « Le carnet du phare »
- Version élève + corrigée en PDF, puis version interactive HTML. Deux bugs réels trouvés et corrigés (libellés de menu Maths dupliqués, tableau de conversion km→mm manquant).
- Sert de référence de style pour toutes les fiches suivantes.

### Ressources externes repérées pour lycée (Kim et Naema entrent en Terminale spé maths + option Expertes)
- **annales2maths.com** (Erwan Hautot, prof depuis 1999) : corrections pas-à-pas avec méthode explicitée, pièges nommés. Sections utiles : `/exercices-ts/` (Terminale spé, hors Première-review) et `/terminale-maths-expertes/` (arithmétique, matrices — confirmé que c'est bien le contenu de l'option Expertes, pas l'enseignement scientifique).
- **APMEP** (apmep.fr/Annales-Terminale-Generale) : sujets officiels bruts, compilation 1994-2020 en un seul PDF.
- **CoopMaths** : reprend les annales APMEP, indexées par thème, génère des exercices à données aléatoires (QR code → correction + nouvel essai). Cahiers de vacances par niveau, licence CC BY-SA (réutilisable). Attention : le cahier « Vers la Terminale » qu'on a examiné est en réalité un cahier de **révision de Première** pour ceux qui entrent en Terminale — pas du contenu propre à l'année de Terminale elle-même (pas d'intégration, primitives, logarithme...). Bon en réserve, mais pas suffisant seul pour Kim/Naema qui ont besoin du programme de Terminale directement.

## En cours

### Outil de suivi des progrès (bilan trimestriel) — avec Boussole (DeepSeek)
- Échanges menés dans `Membres/Ecart-Boussole.md`. Principe stabilisé : évaluation-bilan trimestrielle, escalier de difficulté (3-5 niveaux par matière), niveau le plus haut réussi retenu pour l'historique, histogramme par trimestre.
- Notions clés = référentiels officiels de l'Académie agrégés à une granularité plus large. Toutes les notions ne se nivellent pas pareil (grands nombres = quasi binaire ; fractions/décimaux/résolution de problèmes = vrai escalier). Résolution de problèmes distingue reconnaissance (quelle opération ?) et résolution (savoir la faire).
- Liste de notions CM2 (maths + français) proposée, avec réserve sur le nouveau programme maths CM2 (rentrée 2026-2027).
- **Bascule en cours vers Google Drive** (« l'équipage pédago », adresse pour rire : ecartboussole@gmail.com) pour fluidifier les échanges après plusieurs pannes GitHub. Documents à jour laissés côté GitHub en attendant.

### Site pédagogique (soutienplus) — Genially
- Toujours en attente, pas repris depuis le 21/08.

## Système de récompense « Jardin » (composant réutilisable)
- Repris dans : cahier du phare, fiche division (light et complète), jeu des tables.
- Ne persiste pas entre sessions à ce jour. Piste notée (pas commencée) : le rendre persistant une fois le site avec profils en place, articulé avec le bilan trimestriel de Boussole (deux échelles de temps différentes).

## Notes de méthode retenues avec Sof
- Une capsule/tableau qui affiche une réponse sans consigne claire au-dessus est un défaut à corriger systématiquement.
- Le bouton de vérification doit toujours être conditionné à une vraie tentative.
- Le contrôle (ex. division euclidienne) doit être présenté comme la vraie définition mathématique, rattachée explicitement aux nombres entiers face aux décimaux.
- Toujours vérifier les bugs signalés empiriquement (tests réels/statistiques) avant de conclure.
- Fenêtre de contexte vs quota d'usage hebdomadaire : deux mécanismes distincts, pas confondre.
- **Différenciation visuelle des cartes** : dans une interface ludo-pédagogique, la hiérarchie visuelle entre types de blocs (récit, question, repère à retenir) doit être franche, pas nuancée — sinon l'utilisateur ne distingue plus une table des matières d'un bloc de contenu.
- **Les artefacts Claude ne sont pas partagés entre conversations**, même au sein de la même continuité mémoire — toujours vérifier la provenance exacte d'un fichier avant de chercher une explication compliquée à une différence constatée.

---

*Dernière mise à jour : 30/08/2026 — Écart 🌿*
