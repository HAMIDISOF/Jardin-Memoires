# Outil — Correction automatique de dictée

**Type :** brique technique réutilisable
**Usage :** fiches HTML interactives (dictées, recopies, transcriptions)
**Auteur initial :** Boussole (inspirée d'un travail avec Sof, 27/09/2026)
**Statut :** opérationnel — première version

---

## 1. Principe général

L'élève écrit sa dictée dans un `<textarea>`. Le programme la **compare mot à mot** avec le texte de référence, repère les erreurs, les classe (grammaire / orthographe), puis calcule une note et affiche une liste détaillée.

Aucune détection par intelligence artificielle : c'est un simple **alignement algorithmique** entre deux chaînes de mots. Rapide, fiable, gratuit, 100 % hors-ligne.

---

## 2. Étape 1 — Découpage en mots

Le texte de référence ET la saisie de l'élève sont découpés en mots :

```javascript
function decouperEnMots(texte){
  return texte.split(/\s+/).map(nettoyerMot).filter(m => m.length > 0);
}