# 🏗️ Structure HTML – Index et Chapitre 17

## 📄 `index.html` (Hub principal)
- Contient les **17 notions** du programme dans une grille.
- Seul le bouton **"La vérité"** est actif et pointe vers `chapitre_17.html`.
- Les autres boutons sont grisés (`class="inactive"`).
- Contient aussi la liste des **repères** (affichée en bas de page).

## 📄 `chapitre_17.html` (Page du chapitre)
- Contient la **carte mentale** de la page 409 du manuel.
- Structure actuelle : 4 blocs (`carte-mentale`), un par question.
- Chaque bloc contient :
  - Un titre `h2` en orange (`#E67E22`).
  - Des branches (`div.branche`) avec un titre en bleu (`#4A90E2`).
  - Des sous-branches (`div.sous-branche`) avec les idées clés et les auteurs en orange.
  - Un bouton `btn-fiche` vers la fiche complète (`verite_qX.html`).

## 🔗 Navigation
- `index.html` → `chapitre_17.html` (via le bouton "La vérité").
- `chapitre_17.html` → `verite_q1.html` à `q4.html` (via les boutons "Voir la fiche complète").
- Chaque fiche a un bouton "Retour au sommaire" qui pointe vers `index.html` (ou `chapitre_17.html` à ajuster).