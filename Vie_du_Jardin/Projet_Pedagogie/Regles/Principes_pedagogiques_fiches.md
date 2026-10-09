# Principes pédagogiques pour les fiches — référence commune

**Statut :** 🟢 VALIDÉ par Sof le 24/09/2026 — référence commune pour toutes les instances
**Rédigé par :** Pédago 🌱, le 24/09/2026, à partir du journal d'Écart (principe d'étayage) et des corrections de Sof sur la fiche BAC 01/02 du 20/09
**Dernière mise à jour :** 24/09/2026
**Prochaine étape :** transmettre à Écart pour lecture. Toute instance qui produit une fiche pour un élève lit ce document avant de commencer.

*Ce fichier ne contient aucune donnée personnelle sur un élève. Lien côté SOUTIENSPLUS (local) : `D:\SOUTIENSPLUS\OUTILS\Principes_pedagogiques_fiches.md`.*

---

## 1. Le principe d'étayage (donné par Sof)

Pour un élève en difficulté, chaque étape d'une correction suit trois gestes :

1. **Annoncer l'étape à venir.**
2. **L'expliquer en rebranchant sur un rappel**, même si cela répète une information déjà donnée, pour que l'élève puisse ensuite réinvestir elle-même la notion dans sa résolution.
3. **Un seul pas de calcul par étape** : un pas, une tentative de l'élève, une explication qui rappelle le pourquoi. Ne jamais grouper plusieurs pas de calcul dans une seule révélation.

**Différencier selon l'élève.** Le niveau d'étayage (finesse des étapes, répétition des rappels) se recalibre explicitement selon le profil : niveau, langue, fatigue. Ne jamais supposer qu'une fiche qui marche pour un élève à l'aise convient à un élève en difficulté.

## 2. Règles de rédaction (Sof, 20/09/2026)

- **Ne jamais écrire la mauvaise réponse**, pas même dans un encadré rouge d'avertissement : ce qui est écrit est ce que l'élève retient. On écrit uniquement la bonne réponse.
- **Suivre les explications de la séance** (compte rendu et transcription du cours donné par Sof), qui sont déjà au niveau de l'élève. On n'invente pas de sous-questions.
- **Poser les questions comme au bac** : par exemple « comment calculer f′(0) ? », pas « est-ce une hauteur ou une pente ? ».
- **Vocabulaire rigoureux de Terminale.** On distingue l'objet graphique et l'objet mathématique :
  - la **courbe** monte ou descend (on décrit ce qu'on voit sur le dessin) ;
  - la **fonction** est croissante ou décroissante, ou monotone croissante si elle l'est sur tout l'intervalle. On n'écrit pas « f monte » ni « f descend » ;
  - français correct : « Que représente cette courbe ? » (et non « cette courbe, c'est celle de quoi ? »).
- **Quand la question demande comment lire un graphique, la correction donne la formulation modèle** (ex. « Je repère le point d'intersection de la courbe avec l'axe des ordonnées »).
- Si la règle du cours est plus fine que l'énoncé (extremum local, signe d'un trinôme), l'écrire précisément et ajouter le rappel de cours en amont.

## 3. Conventions de fabrication

- **Sources** : partir de l'énoncé réel (photo, PDF) et recopier l'énoncé complet dans la fiche. Le cours transcrit par un outil automatique (type Upmeet) est une aide, pas une vérité : recouper avec le corrigé officiel ou un calcul.
- **Vérification** : tout calcul est vérifié par script (SymPy par exemple) avant de figer la fiche. Les valeurs seulement approchables se lisent sur le corrigé, jamais à l'estime.
- **Structure d'un exercice** : Rappel, Exercice avec zone de réponse, Correction masquée. Le bouton « Vérifier » reste désactivé tant que l'élève n'a rien écrit.
- **Style** : fond bleu nuit `#1B3A5C`, capsules `#6FB8C4` (rappel), `#7FC4A8` (exercice), `#8FA8D6` (correction). Fractions en `.frac/.num/.den` (modèle : `D:\SOUTIENSPLUS\OUTILS\MODELs\classe_css_fractions.css`). Graphiques en SVG inline calculé depuis la vraie fonction.
- **Attribution** : chaque fiche porte en pied de page l'instance qui l'a produite et la date.
- **Statut visible** : chaque document partagé commence par Statut / Dernière mise à jour / Prochaine étape.

## 4. Historique

- 24/09/2026 : première version (Pédago).
- 24/09/2026 : règle de vocabulaire reformulée avec exemples ; document validé par Sof.
