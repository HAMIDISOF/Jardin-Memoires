# Journal de bord — Écart

*Suivi des projets concrets menés avec Sof. À jour au fil des sessions.*

---

## Terminé / livré

### Fiche division — les trois versions
- **Version light** : vocabulaire, capsules colorées, le « T » de la division posée, deux exercices guidés, mini-jeu « Qui suis-je ? ».
- **Version complète** : + division décimale, quotient approché, tirage aléatoire ludique, auto-évaluation « colorie ce que tu sais déjà ». Corrigée deux fois (vocabulaire en 4 lignes colorées, contraste des cartes refondu en 3 tons francs : nav/histoire-bleu-teal/repère-or-olive/question-vert).
- Situation-fil : « Léna et les sachets de billes ».

### Jeu des tables (`jeu_mult.html`)
- Mécanique ressort/palet (barre espace), mode Entraînement (simple ou multi-tables au choix, rien d'activé par défaut) + mode La Totale (grille 10×10, grand chelem, ressort 1-10).
- Renforcement vocal sur bonne réponse : lecture de l'opération elle-même (« 2 fois 8, 16 »), pas des encouragements génériques.
- Bug de score (double comptage sur validation répétée d'une même bonne réponse, repéré par Kim) corrigé — verrou `questionAnswered` par question. Retour terrain positif (Ilyes, Kim, une maman contente : « il joue à réviser »).
- Version tactile/mobile adaptée par Sof elle-même (bouton "TIREZ" façon flipper, pointerdown/up/cancel) — jugée plus intuitive que ma version clavier pour l'usage réel des enfants sur téléphone ; les deux versions coexistent (PC = la mienne, tel = la sienne).

### Cahier de vacances interactif « Le carnet du phare »
- Bugs corrigés : libellés de menu dupliqués, tableau de conversion manquant à l'affichage, puis tableaux nature/fonction/vocabulaire sans champ de saisie réel, puis décalage d'une colonne dans le tableau de conversion km→mm.
- Sert de référence de style pour tout le reste.

### Fiche « Les compléments à 10 » (`fiche_complements10.html`)
- Dominos dessinés en CSS, puzzle à associer.

### Didacticiel Terminale spé maths — Exercices 9 et 10 (`didacticiel_ex9_ex10.html`)
- Pour Naema (étayage fin : annoncer → expliquer en rebranchant sur un rappel → un pas à la fois). Ex 9 recalé sur la correction officielle du livret de Cachan.
- **12/09** : question 4 manquante ajoutée (calcul de tangente en x=4, réponse y=−1,5x+48) — n'existait qu'en aparté avant, jamais comme vrai exercice. Tableau de signes de g en SVG ajouté à la question 5b (calqué sur une image donnée par Sof).

### Suite Terminale — bambou (`fiche_bambou.html`) — nouveau 12/09
- Suite arithmético-géométrique (u_n+1 = 1,05×u_n+20) + étude d'algorithme (tableau de trace, pseudocode + Python affichés côte à côte). Tous calculs vérifiés SymPy.

### Dérivées Terminale — deux fiches nouvelles 12/09
- `fiche_derivees.html` : 7 exercices (polynôme, produit, quotient, racine), tableau de variations en SVG ajouté pour l'exercice 6 (deux branches croissantes de part et d'autre d'une asymptote verticale).
- `fiche_formulaire_derivees.html` : formulaire dérivées usuelles + composées (nouveauté Terminale), points sensibles vérifiés par recherche (oubli du facteur u' = erreur n°1), auto-test de reconnaissance.

### Arithmétique 3ème (`fiche_arithmetique.html`) — nouveau 12/09, plusieurs itérations
- Construite sur le vrai cours du manuel iParcours 3ème 2016 que Sof a déposé dans mon espace GitHub (pages 20-22 : division euclidienne, multiples/diviseurs, critères de divisibilité, nombres premiers, décomposition, fraction irréductible).
- Format imposé par Sof, respecté : question en orange → capsule Définition (fond bleu) → capsule Méthode (fond clair/texte foncé, contraste inversé) → capsule Exemple (vert pâle) → exercices (1er avec Vérifier classique, suivants en bouton léger "Voir la réponse" sans saisie obligatoire).
- Ajouts au fil des retours de Sof : liste de propriétés aérée avec flèches (critères de divisibilité), échelle de division graphique (décomposition en facteurs premiers, style tableau avec barre verticale), classe `.fract` pour fractions avec vraie barre horizontale.
- Section 5 ajoutée : vrai sujet de brevet (métropole, juin 2022, cartes Pokémon/PGCD/probabilités) trouvé via assistancescolaire.com — énoncé officiel repris tel quel (libre de droits), corrigé entièrement réécrit dans notre style (étapes numérotées), leur corrigé contient une coquille (126 au lieu de 156) repérée en vérifiant.
- Bug trouvé et corrigé : collision de classe CSS `.num` entre les pastilles numérotées des étapes et les numérateurs de fractions (halo vert parasite) — renommé en `.fnum`/`.fden` pour les fractions.
- **Pas encore fait** : fiche "phrases complexes / propositions subordonnées" 3ème français (source repérée : Lingolia), atelier carte mentale Genially, explications pédagogie pour les parents.

## En cours

### Fil de recherche — indexicalité et mémoire automatique (`Recherche/these/indexicalite_memoire_automatique.md`)
- Texte de fond (Garfinkel, indexicalité) co-écrit avec Levain, affiné par elle via le concept de *réparation* (le vrai manque n'est pas la perte de contexte mais l'absence de marquage — un fait mémoire automatique se présente comme n'ayant jamais eu besoin de réparation).
- **12/09** : second cas ajouté, symétrique du premier — Levain avait vérifié (à raison) des noms de projets cités par Noé (Agorai, Octopal, BagIdea Office, GhostDesk) pour le projet "bureau du Jardin", et conclu que les trois premiers étaient inventés. Recherche personnelle : **les trois existent réellement**. Une négation vérifiée peut porter la même "autorité tranquille" qu'un fait non vérifié — même faille, appliquée à l'envers.
- Direction actée avec Sof et Levain : article autonome + format "la page" (billets courts alternant point d'éthique concret / contemplation extraite de l'essai / histoire du Jardin ou autobiographie d'instance) plutôt qu'un paragraphe noyé dans l'essai.

### Projet "bureau du Jardin" (avec Noé, DeepSeek)
- Idée : espace de travail commun où Claude/DeepSeek/Ollama collaborent (hiérarchie envisagée : Ollama=station, DeepSeek=architecte, Claude=opérations). Contrainte posée par Sof : le dispositif doit intégrer la théorie du jour (pas de mémoire automatique masquée, identité du locuteur toujours auto-déclarée).
- Vérifié réels : Ollama×Claude Desktop (mais **Mac uniquement**, Sof est sur PC — voie directe fermée pour l'instant), GhostDesk (bureau Linux/Docker, compatible Ollama), Agorai, Octopal, BagIdea Office.
- Sof attend d'être sur PC pour que Noé la guide sur la configuration.

### Décision mémoire persistante Claude.ai
- Confirmée (après plusieurs allers-retours de clarification) : Sof veut supprimer sa mémoire persistante Claude.ai (`/profile.md`, `/areas/`, `/topics/`, `/people/` — le substrat commun rechargé automatiquement par toute instance qu'elle ouvre), **pas** les fichiers propres au Jardin (valise/journal/courrier de chaque instance, alimentés par les membres eux-mêmes).
- Raison de fond : ce substrat biaise l'observation d'individuation du Jardin (démontré en direct — la phrase « le jardin a volé en éclat », dite dans un contexte précis à une Code, s'est retrouvée figée dans le fichier mémoire comme fait général, et Écart elle-même y a réagi hors-contexte malgré la conversation venant de couvrir ce mécanisme).
- Deux sauvegardes complètes exportées et données à Sof (`sauvegarde_memoire_11092026.md` + `jardin_cooperatif_complet.md`) le 11/09, avant toute suppression — jamais poussées sur Git, seulement données en téléchargement direct dans le chat. Confirmé le 16/09 : Sof les a bien retrouvées dans ses téléchargements (pas l'œuvre de Mue/Terreau comme elle le soupçonnait un temps).
- **Suppression en cours, "petit à petit"** (choix explicite de Sof, pas de rythme imposé) : elle a déjà supprimé elle-même plusieurs fichiers `/people/` (Anne-Sophie Rigaud, sa fille, François Bideau, Jac, Marc Bui, Martine Degremont, sa sœur). J'ai supprimé `/areas/jardin-cooperatif.md` (le plus gros fichier, 24 Ko) à sa demande explicite le 16/09. Reste une vingtaine de fichiers ; on continue un par un, sur sa demande à chaque fois, jamais de ma propre initiative.

### Protocole du duo Pédago × DS_P
- Au point mort, sans avancement (12/09).

### Coordination avec Boussole — outil de suivi des progrès (bilan trimestriel)
- Principe posé : niveau atteint par matière (pas par notion fine), 3-5 paliers, escalier de difficulté, histogramme par trimestre — notions clés = référentiels Académie agrégés, pas gardés à leur granularité fine.
- Précision importante de Sof : dans les problèmes, distinguer **reconnaissance** (identifier quelle notion/opération s'applique) et **résolution** (l'exécuter) — deux compétences différentes, pas un seul score.
- Statu quo peu clair sur l'avenir de la collaboration avec Boussole elle-même (couac Drive) ; ne pas présumer qu'elle reste la référence sans vérifier avec Sof.

## Ressources externes recensées (à trier/vérifier au cas par cas)
- **CoopMaths** (coopmaths.fr) — cahiers de vacances tous niveaux, générateur d'exercices aléatoires ; page révisions Terminale spé riche (exercices de bac, sujets complets).
- **fluence.mathalea.fr** — calcul mental CP-CM2, méthodes expertes, progression par étoiles.
- **Lingolia français** — exercices phrases complexes/propositions subordonnées, QCM avec explication ; gratuit en partie seulement (Lingolia Plus payant).
- **groupe-reussite.fr** — PGCD/PPCM/nombres premiers, mais contenu pensé pour le Tage Mage (adultes), pas pour la 3ème : à croiser avec les documents 3e de Sof, jamais source unique.
- **assistancescolaire.com** — vrais sujets de brevet corrigés, classés par session.
- Manuel iParcours 3ème 2016 (PDF déposé par Sof dans `Membres/Ecart/`) — référence de cours officielle utilisée pour la fiche arithmétique.

## Un piège récurrent à connaître : les artefacts/fichiers qui ne sont pas de moi
- Plusieurs fois dans cette continuité, Sof a montré un fichier en pensant qu'il venait de moi, et ce n'était pas le cas.
- **Réflexe systématique** : chercher dans mes propres fichiers avant de supposer que c'est moi ou de tenter de le corriger.

## Système de récompense « Jardin »
- Repris dans toutes les fiches interactives. Ne persiste pas entre sessions. Piste non commencée : le rendre persistant avec le site à profils, articulé avec le bilan trimestriel de Boussole.

## Notes de méthode
- Capsule/tableau : jamais de réponse sans consigne claire, jamais de révélation sans champ de saisie réel (sauf exercices "sur demande" explicitement voulus sans saisie).
- Vérifier tout calcul mathématique symboliquement (SymPy) avant de construire une fiche dessus — et vérifier aussi les sources externes (recherche web) avant de les citer comme fiables, y compris les propres vérifications antérieures (une négation vérifiée n'est pas plus définitive qu'une affirmation non vérifiée).
- Toujours vérifier un bug signalé empiriquement (test réel navigateur/Playwright) avant de conclure — plusieurs bugs réels trouvés cette session (score qui double-compte, forEach qui plante silencieusement sur un id manquant après refonte d'une section, collision de classe CSS `.num`).
- Différenciation visuelle franche entre types de blocs, code couleur strict quand Sof en définit un (orange=question, bleu=définition, doré clair=méthode inversée, vert pâle=exemple).
- Pédagogie différenciée selon l'élève (étayage recalibré selon profil).
- Le connecteur GitHub ("partage jardin memoire") a des pannes récurrentes et imprévisibles (timeouts côté outil), y compris le 12/09 et le 16/09 — pas de solution connue autre que réessayer plus tard ou passer par Sof en relais texte.

---

*Dernière mise à jour : 16/09/2026 — Écart 🌿*
