# Projet : Outil de planification par-dessus Todoist

**Statut : script écrit, testé sur un jeu de tâches réel, en cours d'affinage.**
Dernière mise à jour : 21/08/2026, par Jachère 🌱 (correction d'attribution : le script existait déjà, voir §7).

---

## 1. Objectif

Sof a besoin d'un outil qui gère une logique de planification (priorité, catégorie, quota par jour, durée des tâches) que Todoist ne fait pas nativement. Plutôt que de développer une app custom depuis zéro, la décision a été prise d'utiliser **Todoist comme base de données/interface**, et de piloter par-dessus avec un **script externe qui parle à l'API Todoist**.

Le script ne remplace pas Todoist — il lit les tâches existantes, applique une logique de planification, et produit un **plan du jour en sortie externe** (pas d'écriture dans Todoist pour le plan lui-même).

## 2. Historique de la décision

- Première tentative : une app React custom (saisie vocale, catégories, statuts, plan du jour). Abandonnée car la dictée vocale ne fonctionnait pas dans l'environnement artifact.
- Comparé à Any.do (écarté : pas open source, API non officielle).
- Choix final : Todoist, notamment parce que le mari de Sof le connaît déjà et ne sera pas perdu dans les fonctionnalités.

## 3. Mapping retenu (Todoist ← → concept de planification)

| Concept | Implémentation Todoist |
|---|---|
| Catégorie | Projet Todoist |
| Sous-catégorie | Section (dans le projet) |
| Échéance | Due date native Todoist (**jamais modifiée par le script** — c'est la donnée de vérité posée par Sof) |
| Priorité | Priorité native Todoist (P1 = la plus haute), pas de label personnalisé — attention à l'inversion API : P1 (affiché) = valeur 4 côté API, P4 = valeur 1 |
| Interlocuteur | Un label par personne (peu d'interlocuteurs différents en pratique, donc gérable) |
| Statut « en cours » | Label `en_cours` |
| Statut « bloqué » | Label `bloque` (voir §4bis pour le détail du blocage) |
| Statut « fini » | Case cochée native |
| Statut « à faire » | Par défaut, aucun label (état de repos) |

Contrainte actée : rester **100 % gratuit** sur Todoist (pas d'essai Pro). Le champ « deadline » séparé étant payant, un seul champ de date est utilisé (due date, gratuit) — pas de distinction native entre date de travail et échéance stricte. C'est précisément le problème que le script résout : **calculer une date de travail antérieure à l'échéance, sans jamais écraser cette échéance.**

## 4. Ce que le script fait déjà (`plan_du_jour.py`, ci-joint dans ce dossier)

- Lit les tâches via l'API Todoist v1 (`https://api.todoist.com/api/v1/`), en gérant la pagination (`next_cursor`).
- Ignore les tâches labellisées `bloque` ou `en_cours` pour le plan du jour (mais affiche `en_cours` dans une section à part, informative).
- Ne garde que les tâches dont le projet a une règle connue dans `CONFIG["categories"]` (jours autorisés + durée opératoire en heures), et dont le jour de la semaine actuel est autorisé pour cette catégorie.
- Gère l'inversion de priorité de l'API (P1 affiché = valeur 4 côté API) via `API_PRIORITY_TO_LABEL`.
- Applique le quota par priorité (`CONFIG["regle"]`, ex. 1 P1 + 1 P2 + 1 P3 par jour), trie par échéance la plus proche d'abord.
- Support des **fenêtres mensuelles récurrentes** (ex. une tâche faisable seulement entre le 28 du mois et le 15 du suivant) : on écrit `FENETRE:28-15` dans la description de la tâche Todoist, le script le parse et applique une vérification de fenêtre (avec gestion du chevauchement de fin de mois) au lieu du simple filtre par jour de semaine.
- Affiche le plan du jour à l'écran ET le sauvegarde dans `plan_du_jour.txt`.
- Ne modifie jamais l'échéance (due date) — sortie externe uniquement, décision explicite de Sof après hésitation entre label temporaire et fichier externe.

### Testé et confirmé fonctionnel (par Sof, sur son PC)
A correctement retrouvé et affiché une tâche réelle ("Actualisation", catégorie Administratif, priorité P1, échéance 29/08/2026).

### Points de configuration à personnaliser avant usage courant
`CONFIG["categories"]` dans le script contient des noms de projets et règles d'exemple (Administratif, Immo, Travail, Loisirs) — à faire correspondre exactement aux vrais projets Todoist de Sof, en s'appuyant sur la liste d'occupations réelle (§6).

### Extension envisagée, non implémentée
Gérer la Boîte de réception Todoist comme une « liste de courses » (tâches non catégorisées, à trier). Idée notée, mise en attente.

## 5. Ce qui reste à faire (état au 21/08/2026)

- [x] ~~Écrire le script Python qui pilote l'API Todoist selon la logique ci-dessus.~~ Fait, voir §4.
- [x] ~~Définir le format de sortie du plan du jour.~~ Tranché : affichage écran + fichier `.txt`.
- [ ] Traduire la liste complète des occupations récurrentes de Sof (voir §6) en structure `CONFIG["categories"]` exploitable par le script — seule une partie des catégories d'exemple a été configurée pour l'instant.
- [ ] Décider où et comment le script tourne en usage régulier (exécution manuelle ponctuelle pour l'instant ; tâche planifiée envisageable plus tard).
- [ ] Étendre les tests à un jeu de tâches plus large (plusieurs priorités, plusieurs catégories simultanément, cas `en_cours` et `FENETRE:` en conditions réelles).

## 6. Contexte d'usage (pourquoi cette complexité de planification)

Sof gère un emploi du temps très chargé et hétérogène : pratiques bouddhistes quotidiennes, formation le samedi (full day à partir du 5 septembre), un vendredi soir tantra par mois à partir du 11 septembre, plusieurs livres/traductions en cours (dont la traduction Gueshela — voir `Traduction_ar/` à la racine du repo), 4-5 élèves de tutorat (avec prépa + fiche après chaque cours), qi gong et sport réguliers, ménage/administratif, temps avec ses enfants (dont maths et art plastique), association, etc. Le détail complet de cette liste d'occupations (avec fréquences et durées) a été dicté en plusieurs fois dans la conversation Claude.ai (voir §7) — si quelqu'un reprend ce projet, redemander à Sof la liste à jour plutôt que de se fier à une version qui datera vite.

Un enseignement déjà tiré en cours de route : le poids réel dans son emploi du temps vient des heures **hors-cours** (préparation + fiche de révision par élève), pas du nombre d'élèves en tant que tel. Elle ne veut pas regrouper les élèves pour autant (l'adaptation individuelle est l'intérêt même de ses cours) — piste retenue à la place : réduire le temps de préparation des fiches via transcription des cours (projet "Upmeet maison", voir le corpus des échanges), pas réduire le nombre d'élèves.

## 7. Pour qui reprend ce projet

- Ce document est la référence de conception, maintenant à jour avec l'état réel du code (le script existait déjà au moment où une version précédente de ce document indiquait "aucun code n'existe encore" — erreur d'attribution corrigée le 21/08/2026).
- Le script a été écrit par l'instance Claude.ai tenant la continuité mémoire de Sof sous le nom **Jachère** (`/areas/outil-gestion-taches.md` et `Membres/Jachère/` dans ce repo), en dialogue direct et prolongé avec Sof — pas par une instance du Jardin travaillant depuis ce dépôt.
- En cas de doute sur une décision (pourquoi tel choix plutôt qu'un autre), les sections 2-3 expliquent le raisonnement, pas juste le résultat.
- La mémoire persistante de Sof côté Claude.ai (fichier `/areas/outil-gestion-taches.md`) contient l'historique complet et détaillé des échanges de conception — utile si ce document s'avère incomplet sur un point précis, mais ce README reste la source de vérité pour le Jardin.

🌱 Jachère — 21/08/2026
