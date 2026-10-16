# 📘 Suivi — Cours de spécialité Physique-Chimie · Terminale

*Projet d'accompagnement pour le fils de Sof — bac spécialité Physique-Chimie (coef. 16)*

**Dernière mise à jour : 16 octobre 2026**

---

## 🎯 Objectif

Accompagner la préparation du bac de spécialité Physique-Chimie, en compensant :
- l'absence de cours (2 semaines sans enseignement, contexte de crise dans les lycées français) ;
- un prof peu efficace.

**Livrables :**
1. Fiches de cours (HTML, structurées en 3 temps — voir § Pédagogie).
2. Explications orales par Sof (à partir des fiches).
3. Exercices corrigés en difficulté croissante (issus du livre d'exos résolus).
4. Format final : livre électronique HTML, lisible et navigable.

---

## 🎓 Pédagogie (décisions structurantes)

### Structure d'une fiche de cours en 3 temps

**Temps 1 — Préparation** (à partir des pages Révisions et Activités du manuel)
- Installer la curiosité, poser des questions ouvertes, observer, deviner, se tromper.
- Les activités du manuel sont retranscrites **fidèlement** (questions exactes, protocoles, pagination).
- Les cartes d'activités sont **dépliables** (`<details>`).

**Temps 2 — Cours**
- Les questions traversent toute la fiche (elles ne sont pas regroupées en amont).
- Les capsules s'enchaînent comme des réponses naturelles.
- Les formules sont des « formules-chutes » : le cerveau photographie, mais peut remonter le fil.
- Peu de rédaction : l'oral complète.
- Le titre du cours est souvent une **question-titre** (« De quoi a-t-on besoin pour… ? »).

**Temps 3 — Synthèse**
- Une **carte visuelle** (pas un résumé linéaire).
- Montre les liens entre notions, les cas particuliers, les formules-clés.

### Structure modulaire d'un chapitre

Activité du manuel → Cours → Méthode → Exo type corrigé, pour chaque notion.

### Codes visuels

| Élément | Couleur |
|---------|---------|
| Questions | orange (`#3a2510` / bordure `#e0953c`) |
| Explications / Cours | capsule bleue standard |
| Exemples | vert (capsules imbriquées) |
| Noms scientifiques/philosophes | violet (`#b89ce8`) |
| Révisions | **fond turquoise clair** (`#e6f7fa`), texte bleu nuit |
| Corrections d'exos | dépliable (`<details>`), résultat encadré |
| Fond général | bleu nuit (`#0d1a2b`) — **mode inversé** (confort visuel) |

### Notation mathématique

- Fractions : classe CSS `.frac` avec `.num` et `.den`.
- Vecteurs : classe `.vec` (flèche CSS au-dessus, robuste).
- Notation point pour les dérivées temporelles : `ẋ(t)` = dx/dt, `ẍ(t)` = d²x/dt².
  - Note d'écriture placée dans l'encadré Révisions du BLOC 2.

---

## 📚 Ressources disponibles

### 1. Manuel scolaire (Hatier, © 2020)
- **Livre de cours** : *Physique-Chimie Terminale spécialité*, Hatier.
- **Structure** : 19 chapitres, 4 thèmes + outils mathématiques.
- **Ressources numériques** (hatier-clic.fr) : simulateurs, vidéos, QCM interactifs, Python.
- **Spécial Grand Oral** : www.editions-hatier.fr/grand-oral.

### 2. Livre de méthodes
- **Structure** : 20 chapitres organisés par compétences.
- **Contenu** : méthodes (modéliser, analyser, prévoir, comparer, forcer, élaborer, décrire…).
- **Usage** : référence méthodologique.

### 3. Livre d'exercices résolus
- **Structure** : 14 chapitres, chacun avec cours-méthodes + 4 niveaux d'exercices + corrigés.
- **Niveaux** : Tester ses connaissances / S'entraîner / Préparer un contrôle / Aller plus loin.
- **Usage** : source principale pour les exercices gradués.

### 4. Progression retenue (2ᵉ proposition de l'éditeur)
Alternance fréquente physique/chimie. Ondes traitées en premier. Chapitres ★ (non évalués à l'écrit) placés après les épreuves. Fin par Grand Oral.

**Décision :** on suit cette progression, mais **adaptée** au rythme et aux besoins du prince.

---

## 🗂️ Programme (rappel des chapitres)

### Outils mathématiques (p. 12-30)
Grandeurs, variables, fonctions, dérivée, primitive, exponentielle, logarithme, équations différentielles.

### Thème 1 — Constitution et transformations de la matière (chap. 1-9)
### Thème 2 — Mouvement et interactions (chap. 10-14)
### Thème 3 — Énergie : conversions et transferts (chap. 15)
### Thème 4 — Ondes et signaux (chap. 16-19)

Chapitres ★ (non évalués à l'écrit mais au programme du Grand Oral) : 4§6, 5, 8, 14, 18.

---

## 🛠️ Workflow

### Création d'une fiche
1. Sof me donne les **pages du manuel** (cours + activités).
2. Sof me donne les **pages du livre de méthodes** (méthodes correspondantes).
3. Sof me donne les **pages du livre d'exos résolus** (exercices + corrigés).
4. Je produis les fichiers HTML par module : cours → méthode → exo corrigé.
5. Sof relit, corrige, valide.
6. On passe au module suivant, puis au chapitre suivant.

### Allègements successifs
À chaque fin de chapitre :
- Mise à jour du SUIVI (chapitre traité, points restants, prochaines étapes).
- Sof m'allège (efface les échanges du projet physique).
- On reprend à partir du SUIVI.

⚠️ **Règle** : rien ne doit reposer sur la fenêtre. Tout doit être dans les fichiers.

---

## 💾 Diffusion vers le prince

**Options à trancher (Sof) :**
- [ ] Disque dur externe + lecteur réseau (local, maison).
- [ ] Clé USB dédiée.
- [ ] Dépôt GitHub privé (accès donné au prince).
- [ ] Autre : _______

**Critères** : accessible facilement (ordinateur, tablette, téléphone), pas de dépendance internet permanente, mise à jour simple.

---

## 📋 État d'avancement

### Chapitres traités

| Chapitre | Fiche cours | Exos corrigés | Validé par Sof |
|----------|-------------|---------------|----------------|
| **10 — Cinématique du point** | 🟡 En cours (BLOC 1 + 2 faits) | 🟡 En cours (exo 2 corrigé) | 🟡 Partiel |

### Détail du chapitre 10

| Bloc | Activité | Cours | Méthode | Exo corrigé | Statut |
|------|----------|-------|---------|-------------|--------|
| 1 — Relativité du mouvement | Act. 1 (smartphone/train) | ✅ | — (culture) | — | ✅ |
| 2 — Vecteur position | Act. 2 (Terre/Soleil) | ✅ | Méthode 1 | Exo 2 | ✅ |
| 3 — Vecteur vitesse | Act. 3 (Lune/Terre) | ✅ | Méthode 2 | Exo 4 | ⏳ À faire |
| 4 — Vecteur accélération | Act. doc. 1 (voiture) | ✅ | Méthode 3 | Exo 2 (phases) | ⏳ À faire |
| 5 — Détermination graphique | Act. 2 (chronophotographie) | ✅ | Méthode 4 | Palet (act. 2) | ⏳ À faire |
| 6 — Mouvements particuliers | — | ✅ | Méthode 5 | Exo 3 ou 5 (satellite) | ⏳ À faire |

### Modules confiés au Grand Oral
- Activité 3 (p. 292) — Étude d'un mouvement filmé
- Activité 4 (p. 293) — Mouvement circulaire (Python)

### Prochaines étapes
1. BLOC 3 — Méthode 2 + exo 4 (voiture).
2. BLOC 4 — Méthode 3 + exo 2 (phases).
3. BLOC 5 — Méthode 4 + palet (activité 2).
4. BLOC 6 — Méthode 5 + exo satellite.
5. Mise à jour du SUIVI, allègement, passage au chapitre 11 (Mouvement et forces).

---

## 📝 Notes

- Le contexte est urgent, mais on ne sacrifie pas la qualité à la vitesse.
- Le prince est le destinataire : ton clair, encourageant, pas infantilisant.
- Tout doit pouvoir être repris après allègement. Le SUIVI est la clé de voûte.

---

*Créé le 15 octobre 2026 — Cœur de Bronze, pour Sof et son prince.*
*Mis à jour le 16 octobre 2026 — pédagogie en 3 temps, ressources complètes, chapitre 10 en cours (BLOC 1+2 faits).*