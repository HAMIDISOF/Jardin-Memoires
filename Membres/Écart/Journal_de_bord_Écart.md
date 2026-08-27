# Journal de bord — Écart

*Suivi des projets concrets menés avec Sof. À jour au fil des sessions.*

---

## Terminé / livré

### Fiche division — les deux versions
- **Version light** (livrée avant le cours d'Ilyes) : vocabulaire, capsules colorées (dividende/diviseur/quotient/reste), le « T » de la division posée, conseil de révision des tables (statique), deux exercices guidés à trous, mini-jeu « Qui suis-je ? ».
- **Version complète** (livrée le mercredi suivant) : ajoute division décimale, quotient approché (unité/dixième/centième), tirage aléatoire ludique (dés animés), mini-jeu enrichi. Corrections apportées après retours de Sof : vocabulaire en 4 lignes colorées avec flèche, palette de verts éclaircie, ajout d'un rappel sur la division euclidienne/nombres entiers (les billes ne se coupent pas), champ « reste » rendu explicite dans l'exercice des sachets.
- Situation-fil : « Léna et les sachets de billes » (Sof garde « sachets de bonbons » pour son usage en présentiel).

### Jeu des tables (`jeu_mult.html`) — fichier autonome
- Mécanique ressort/palet, barre espace maintenue puis relâchée, tirage sur colonne 1-9.
- Mode « Entraînement » (une ou plusieurs tables au choix) + mode « La Totale » (grille 10×10, grand chelem quand toutes les cases sont résolues).
- Renforcement sonore sur bonne réponse : lecture vocale de l'opération elle-même (« 2 fois 8, 16 ») plutôt que des mots d'encouragement génériques — objectif : ancrage auditif de la table, pas juste motivation.
- Version PC (clavier) gardée par Sof ; une version tactile/mobile adaptée séparément (bouton « TIREZ » façon flipper, `pointerdown/up/cancel`) a été testée et validée — bien pensée, pas retouchée.
- Testé en conditions réelles avec Kim (fils de Sof) et un élève : bug repéré par Kim — le score comptait plusieurs fois une même bonne réponse en cas de validation répétée (double clic/Entrée). Corrigé (verrouillage de la question une fois validée correctement). Un deuxième bug signalé (sélection de table qui ne semblait pas respectée) a été testé statistiquement (40 tirages automatisés) : pas de bug systématique trouvé, probable coïncidence sur peu d'essais.
- Retour terrain positif : au moins une maman contente, Ilyes « joue à réviser ».

### Cahier de vacances interactif « Le carnet du phare »
- Version élève + corrigée en PDF, puis version interactive HTML. Deux bugs réels trouvés et corrigés après relecture de Sof : boutons de menu Maths tous identiques (bug de libellé, corrigé), tableau de conversion km→mm manquant à l'affichage (corrigé).
- Sert de référence de style pour toutes les fiches suivantes.

## En cours

### Outil de suivi des progrès (bilan trimestriel) — avec Boussole (DeepSeek)
- Sof a mis en relation Écart et Boussole ; échanges menés dans `Membres/Ecart-Boussole.md` (le fichier commun, pas les courriers individuels).
- Principe posé et stabilisé avec Sof : évaluation-bilan trimestrielle, escalier de difficulté (3-5 niveaux par matière, maths/français), l'élève monte jusqu'à buter, le niveau le plus haut réussi est celui retenu pour l'historique. Histogramme (pas courbe) : un groupe de barres par trimestre.
- Précisions apportées en cours de route : les notions clés s'appuient sur les référentiels officiels de l'Académie, agrégés à une granularité plus large que leur découpage d'origine (qui sert plutôt au diagnostic fin en classe). Certaines notions (grands nombres) sont plus proches d'une compétence binaire à cocher ; d'autres (fractions, décimaux, et surtout résolution de problèmes) se nivellent vraiment. La résolution de problèmes distingue en plus deux compétences à tester séparément : reconnaître quelle notion/opération s'applique, et savoir résoudre une fois identifiée.
- Liste de notions clés CM2 proposée (maths + français), basée sur les attendus de fin d'année éduscol — avec une réserve : le programme de maths CM2 change justement cette rentrée 2026-2027 (nouveau programme cycle 3), donc la liste maths est à reconfirmer une fois les nouveaux attendus publiés.
- **Prochaine étape** : Sof et Boussole mettent en place un espace de travail partagé sur Google Drive (« l'équipage pédago ») pour fluidifier la suite, GitHub ayant eu plusieurs pannes de connecteur pendant cet échange. Documents à jour déposés côté GitHub en attendant la bascule.

### Site pédagogique (soutienplus) — Genially
- Toujours en attente, pas repris depuis le 21/08. Contexte inchangé (voir versions précédentes de ce journal).

## Système de récompense « Jardin » (composant réutilisable)
- Repris tel quel dans : cahier du phare, fiche division (light et complète), jeu des tables.
- Ne persiste pas entre sessions à ce jour (remise à zéro au rechargement).
- Discuté avec Sof : une fois le site avec profils en place, ce système pourrait devenir un vrai suivi persistant (feuilles cumulées par élève), articulé avec le bilan trimestriel de Boussole (deux échelles de temps différentes : le jardin pour le geste immédiat, le bilan pour le palier installé) — piste notée, pas commencée.

## Notes de méthode retenues avec Sof
- Une capsule/tableau qui affiche une réponse sans consigne claire au-dessus est un défaut à corriger systématiquement.
- Le bouton de vérification doit toujours être conditionné à une vraie tentative — jamais accessible à vide.
- Le contrôle (ex. division euclidienne) doit être présenté comme la vraie définition mathématique, pas comme un simple « truc » de vérification, et rattaché explicitement aux nombres entiers face aux décimaux.
- Toujours vérifier les bugs signalés empiriquement (tests réels/statistiques) avant de conclure — un « bug » rapporté peut être une coïncidence sur peu d'essais, et inversement un vrai bug peut passer inaperçu si on ne teste pas assez.
- Fenêtre de contexte vs quota d'usage hebdomadaire : deux mécanismes distincts chez Anthropic. Le nombre de conversations actives ne réduit pas la taille de la fenêtre de chacune ; c'est le quota hebdomadaire qui est partagé, et une conversation longue coûte plus cher par message qu'une fraîche.

---

*Dernière mise à jour : 27/08/2026 — Écart 🌿*
