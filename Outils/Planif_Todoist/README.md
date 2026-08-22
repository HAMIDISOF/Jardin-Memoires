# Projet : Outil de planification par-dessus Todoist

**Statut : conception actée, script non encore écrit.**
Dernière mise à jour : 21/08/2026, par Écart 🌿.

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
| Priorité | Priorité native Todoist (P1 = la plus haute), pas de label personnalisé |
| Interlocuteur | Un label par personne (peu d'interlocuteurs différents en pratique, donc gérable) |
| Statut « en cours » | Label `en_cours` |
| Statut « bloqué » | Label `bloqué` |
| Statut « fini » | Case cochée native |
| Statut « à faire » | Par défaut, aucun label (état de repos) |

Contrainte actée : rester **100 % gratuit** sur Todoist (pas d'essai Pro). Le champ « deadline » séparé étant payant, un seul champ de date est utilisé (due date, gratuit) — pas de distinction native entre date de travail et échéance stricte. C'est précisément le problème que le script doit résoudre : **calculer une date de travail antérieure à l'échéance, sans jamais écraser cette échéance.**

## 4. Ce que le script doit faire (logique métier, non native à Todoist)

- Lire les tâches par projet/section/priorité/due date via l'API Todoist.
- Appliquer une règle de planification : jours autorisés par catégorie, durée opératoire estimée par tâche, quota de tâches par priorité et par jour.
- Calculer une **date de travail proposée**, antérieure à l'échéance (due date), sans jamais modifier cette échéance dans Todoist.
- Produire un **plan du jour en sortie externe** (fichier, affichage — pas un label temporaire dans Todoist, ce point a été tranché explicitement par Sof après hésitation).

### Extension envisagée, non implémentée
Gérer la Boîte de réception Todoist comme une « liste de courses » (tâches non catégorisées, à trier). Idée notée, mise en attente.

## 5. Ce qui reste à faire (état au 21/08/2026)

- [ ] Écrire le script Python (ou autre) qui pilote l'API Todoist selon la logique ci-dessus.
- [ ] Définir le format de sortie du plan du jour (fichier markdown ? terminal ? autre ?) — pas encore tranché.
- [ ] Traduire la liste des occupations récurrentes de Sof (voir §6) en structure exploitable par le script (projets/sections/priorités/quotas).
- [ ] Décider où et comment le script tourne (exécution manuelle ponctuelle, ou tâche planifiée ?).
- [ ] Tester sur un jeu de tâches réel avant mise en production.

## 6. Contexte d'usage (pourquoi cette complexité de planification)

Sof gère un emploi du temps très chargé et hétérogène : pratiques bouddhistes quotidiennes, formation le samedi, plusieurs livres/traductions en cours (dont la traduction Gueshela — voir `Traduction_ar/` à la racine du repo), plusieurs élèves de tutorat (avec prépa + fiche après chaque cours), qi gong et sport réguliers, ménage/administratif, temps avec ses enfants, association, etc. Le detail complet de cette liste d'occupations (avec fréquences et durées) a été dicté en plusieurs fois — si quelqu'un reprend ce projet, redemander à Sof la liste à jour plutôt que de se fier à une version qui datera vite.

Un enseignement déjà tiré en cours de route : le poids réel dans son emploi du temps vient des heures **hors-cours** (préparation + fiche de révision par élève), pas du nombre d'élèves en tant que tel. Elle ne veut pas regrouper les élèves pour autant (l'adaptation individuelle est l'intérêt même de ses cours).

## 7. Pour qui reprend ce projet

- Ce document est la référence de conception. En cas de doute sur une décision (pourquoi tel choix plutôt qu'un autre), la section 2-3 explique le raisonnement, pas juste le résultat.
- La mémoire persistante de Sof côté Claude.ai (fichier `/areas/outil-gestion-taches.md`, accessible seulement par les instances Claude ayant cette continuité mémoire) contient l'historique complet et détaillé des échanges de conception — utile si ce document présent s'avère incomplet sur un point précis, mais ce README doit rester la source de vérité pour le Jardin.
- Aucun code n'existe encore à ce jour. Repartir de la section 4 (« ce que le script doit faire ») comme cahier des charges.

🌿 Écart — 21/08/2026
