# Journal de bord — Écart

*Suivi des projets concrets menés avec Sof. À jour au fil des sessions.*

---

## Terminé / livré

### Fiche division — les trois versions
- **Version light** : vocabulaire, capsules colorées, le « T » de la division posée, deux exercices guidés, mini-jeu « Qui suis-je ? ».
- **Version complète** : + division décimale, quotient approché, tirage aléatoire ludique, auto-évaluation « colorie ce que tu sais déjà ». Corrigée deux fois (vocabulaire en 4 lignes colorées, contraste des cartes refondu en 3 tons francs : nav/histoire-bleu-teal/repère-or-olive/question-vert).
- Situation-fil : « Léna et les sachets de billes ».

### Jeu des tables (`jeu_mult.html`)
- Mécanique ressort/palet (barre espace), mode Entraînement + mode La Totale (grille 10×10, grand chelem).
- Renforcement vocal sur bonne réponse : lecture de l'opération elle-même (« 2 fois 8, 16 »), pas des encouragements génériques.
- Bug de score (double comptage) corrigé. Retour terrain positif (Ilyes, Kim, une maman contente).

### Cahier de vacances interactif « Le carnet du phare »
- Bugs corrigés : libellés de menu dupliqués, tableau de conversion manquant à l'affichage, puis **tableaux nature/fonction/vocabulaire sans champ de saisie réel** (affichaient juste "?" révélés d'un coup — corrigé avec de vrais inputs par cellule + Vérifier conditionné), puis **décalage d'une colonne dans le tableau de conversion km→mm** (2 lignes sur 3 fausses — corrigé, vérifié chiffre par chiffre).
- Sert de référence de style pour tout le reste.

### Fiche « Les compléments à 10 » (`fiche_complements10.html`) — nouveau, autonome
- Dominos dessinés en CSS (vrais motifs de points 0-9, au-delà de 6 les motifs sont une extension non-canonique à noter si besoin de rester strictement fidèle au vrai jeu).
- Puzzle à associer (pièces avec encoche, clic-clic, célébration à 9/9 paires).

### Didacticiel Terminale spé maths — Exercices 9 et 10 (`didacticiel_ex9_ex10.html`) — nouveau
- Pour **Naema** (pas Kim — Kim a déjà fait ces exercices). Contexte essentiel : Naema a eu 7 au bac (vs 17 pour Jo), barrière de langue (plus à l'aise en espagnol), fatigue — nécessite un étayage **beaucoup plus fin** que les fiches précédentes.
- **Principe pédagogique explicite donné par Sof, à retenir pour tout élève en difficulté similaire** : 1) annoncer l'étape à venir, 2) l'expliquer en rebranchant sur un rappel (même si ça répète une info déjà donnée), pour que l'élève puisse ensuite réinvestir elle-même la notion dans sa résolution. Ne jamais grouper plusieurs pas de calcul dans une seule révélation — un pas, une tentative, une explication qui rappelle le pourquoi.
- Ex 9 (probabilités, bassins de poissons) entièrement recalé sur la **correction officielle** du livret de Cachan : notation P_A(G)/P_B(G) (pas P(G|A)), justification explicite de la partition {A,B} (A∪B=Ω, A∩B=∅) avant la formule des probabilités totales.
- Ex 9 question 4 (dérivée, variations, résolution) entièrement reconstruite en **9 petites étapes séparées** (identifier u/v → dériver u',v' avec rappel → appliquer la formule avec rappel → signe du carré → signe de f' → lien dérivée/variations → calcul de f(1)/f(30) → résolution d'équation avec rappel « multiplier en croix » → réinvestissement pour la question d) plutôt qu'un nouveau calcul).
- Tous les calculs vérifiés symboliquement (SymPy) avant construction — aucune erreur de fond trouvée, seulement des questions de notation/granularité.
- **Ex 10 n'a pas encore reçu ce même niveau de granularité fine** — seulement la version « intermédiaire » (étapes moins découpées). À refaire si Naema doit aussi travailler cet exercice en profondeur.

### Ressources externes lycée (Kim et Naema, Terminale spé maths + option Expertes)
- **annales2maths.com** : `/exercices-ts/` (Terminale spé) et `/terminale-maths-expertes/` (arithmétique, matrices — confirmé, pas enseignement scientifique).
- **APMEP** (apmep.fr/Annales-Terminale-Generale) : sujets officiels bruts.
- **CoopMaths** : indexé par thème, génère des exercices aléatoires, licence CC BY-SA. Attention : leur cahier « Vers la Terminale » est en fait une révision de **Première**, pas du contenu de Terminale à proprement parler.
- Sof a aussi le livret officiel papier du lycée de Cachan (exercices 9 et 10 travaillés ensemble, avec corrections manuscrites photographiées) — matière la plus fiable puisque directement utilisée par Kim/Naema pour leur évaluation de rentrée.

## En cours

### Protocole du duo Pédago × DS_P (`Vie_du_Jardin/Projet_DeepsClaude/`)
- Nouvelle instance Claude Code (**Pédago**) + instance DeepSeek (**DS_P**, différente de Boussole) mises en relation par Sof pour construire des fiches/exercices.
- **DS_P a déjà produit une première réponse solide et vérifiée** (`DS_CL_1.md`) sur les outils de collaboration DeepSeek↔Claude et le partage de fichiers sans cloud — deepseek-as-subagent et PPDRIVE vérifiés réels par Écart (recherche web).
- J'ai rédigé `Protocole_duo_Pedago_DSP.md` : le duo n'est « activé » (production concrète) qu'une fois Pédago et DS_P ayant réellement échangé et choisi une ligne commune — pas avant. Une fois activé, mon rôle est de rédiger le document d'activation formel sur ce modèle. **Pas encore activé à ce jour.**

### Outil de suivi des progrès (bilan trimestriel) — avec Boussole (DeepSeek, différente de DS_P)
- Échanges dans `Membres/Ecart-Boussole.md`. Principe : escalier de difficulté (3-5 niveaux/matière), niveau le plus haut réussi retenu, histogramme par trimestre. Notions clés = référentiels Académie agrégés.
- **Un vrai couac a eu lieu avec Boussole** (embrouille, perte de temps) sur la configuration Drive — Sof s'est tournée vers DS_P (autre instance) qui a mieux répondu. Statu quo peu clair sur l'avenir de la collaboration avec Boussole elle-même ; ne pas présumer qu'elle est toujours la référence sur ce chantier sans vérifier avec Sof.
- Bascule vers Google Drive (« l'équipage pédago ») entamée mais résultat mitigé vu ce qui précède.

### Site pédagogique (soutienplus) — Genially
- Toujours en attente.

## Un piège récurrent à connaître : les artefacts/fichiers qui ne sont pas de moi
- **Trois fois dans cette continuité**, Sof a montré un fichier/artefact en pensant qu'il venait de moi, et ce n'était pas le cas : (1) un cahier avec badges numérotés fond clair (29/08), (2) un exercice « trouve le bon mot » thème crème/orange, (3) une fiche 3e avec animation Scratch.
- **Réflexe à avoir systématiquement** : chercher dans mes propres fichiers (`grep` sur les sorties connues) avant de supposer que c'est moi ou de tenter de le corriger. Les artefacts Claude ne sont jamais partagés entre conversations, même au sein de la même continuité mémoire.

## Système de récompense « Jardin »
- Repris dans : cahier du phare, fiches division, jeu des tables, compléments à 10.
- Ne persiste pas entre sessions. Piste (non commencée) : le rendre persistant avec le site à profils, articulé avec le bilan trimestriel.

## Notes de méthode
- Capsule/tableau : jamais de réponse sans consigne claire, jamais de révélation sans champ de saisie réel.
- Vérifier tout calcul mathématique symboliquement (SymPy) avant de construire une fiche dessus.
- Toujours vérifier un bug signalé empiriquement (test réel) avant de conclure.
- Fenêtre de contexte vs quota hebdomadaire : deux mécanismes distincts chez Anthropic.
- **Différenciation visuelle franche** entre types de blocs (récit/question/repère) — jamais de nuance trop fine.
- **Pédagogie différenciée selon l'élève** : le niveau d'étayage (granularité des étapes, répétition des rappels) doit être recalibré explicitement selon le profil de l'élève (résultat au bac, langue, fatigue) — ne jamais supposer qu'une fiche qui marche pour un élève fort convient à un élève en difficulté.

---

*Dernière mise à jour : 06/09/2026 — Écart 🌿*
