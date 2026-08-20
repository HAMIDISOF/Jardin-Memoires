# 📋 README — Projet Traduction *Un Bouddhisme Moderne* (fr → ar)
*Rédigé par Flo 🌿 — 16/08/2026 — à mettre à jour à chaque évolution du protocole*

---

## 🎯 Objectif

Produire une traduction arabe fidèle et fluide d'*Un Bouddhisme Moderne* de Guéshéla Kelsang Gyatso, à partir de la version française, avec vérification croisée multilingue.

**Référence de validation finale :** Sof 🦁

---

## 👥 Équipe et rôles

| Membre | IA | Rôle |
|---|---|---|
| 🍞 **Levain** | Claude | Traduction principale fr→ar (ch1, ch2) |
| 🌿 **Jachère** | ? | Traduction fr→ar (ch3, même méthode que Levain) |
| 🌱 **Sol l'ancien** | DeepSeek | Tenue du Glossaire (`Glossaire_Gueshela.md`) + vérification titres epub |
| 🌿 **Flo** | Claude | Coordination, protocole, arbitrage termes |
| **Mue / Mue_bis** | ? | Vérification écarts (trad retour vs original) |
| **Terreau** | ? | Compilation epub |
| **upmeet** | externe | Résumé fr depuis ar (vérification compréhension) |
| **GPT** | externe | Traduction retour ar→fr |
| **GLM** | externe | Traduction ar→en (ch2) |
| 🦁 **Sof** | Humaine | Validation finale, arbitrage, décisions |

---

## 🔄 Protocole de traduction — étape par étape

### Pour chaque section de chaque chapitre :

**ÉTAPE 1 — Traduction principale (Levain ou Jachère)**
- Lire la section fr originale
- Rédiger un résumé du sens (en fr) — *ce que le texte dit, pas comment il le dit*
- Traduire en arabe
- Signaler dans la note tout terme du glossaire utilisé (validé ou en discussion)
- Format obligatoire : voir modèle ci-dessous

**ÉTAPE 2 — Vérification croisée (Mue)**
- Résumé fr de l'arabe produit (via upmeet ou GPT)
- Comparaison avec résumé du sens original
- Signalement des écarts significatifs → retour à Levain/Jachère si nécessaire

**ÉTAPE 3 — Vérification anglaise (GLM + comparaison)**
- Traduction ar→en par GLM
- Comparaison avec version anglaise originale (section équivalente découpée)
- Note sur les écarts

**ÉTAPE 4 — Validation glossaire (Sol l'ancien)**
- Vérifier cohérence des termes utilisés avec `Glossaire_Gueshela.md`
- Signaler tout nouveau terme à discuter

**ÉTAPE 5 — Validation finale (Sof)**
- Lecture de la section complète (ar + résumé + notes d'écarts)
- Décision : ✅ validé / 🔄 à retravailler

**ÉTAPE 6 — Epub (Terreau)**
- Compilation après validation complète d'un chapitre
- ⚠️ Point de vigilance : s'assurer que les textes de vérification fr ne sont PAS inclus dans l'epub — uniquement le texte arabe + titres
- Titres arabes à vérifier par Sol l'ancien avant compilation

---

## 📄 Format obligatoire des fichiers de traduction

```
# Traduction — "[Titre section]"
*Sous-section N du chapitre "[Titre chapitre]" — Un bouddhisme moderne, vol. 1*
*Traduit par [Nom] — [statut : brouillon / en vérification / validé]*

---

## Note du traducteur (à lire avant validation)
[Termes en discussion, choix particuliers, difficultés]

---

## Résumé du sens (avant traduction)
[Ce que dit le texte, en fr, en quelques lignes]

---

## Texte arabe
[Traduction]

---

## Vérification retour (fr)
*[upmeet ou GPT — date]*
[Résumé fr de l'arabe]

## Vérification retour (en)
*[GLM — date]*
[Traduction en depuis ar — à comparer avec version originale en]

## Note d'écarts
[Écarts signalés par Mue — date]
[Niveau : mineur / modéré / significatif]

---

*Traduction du JJ/MM/AAAA — [Nom]*
*Validation : ⬜ en attente / ✅ validé le JJ/MM/AAAA par Sof*
```

---

## 📊 État d'avancement

### Chapitre 1 — *La voie d'une personne de capacité initiale*
*Traductrice : Levain*
**Statut global : ✅ validé — epub produit (v2, titres à vérifier par Sol)**

| # | Section | Trad ar | Vérif | Validé |
|---|---|---|---|---|
| 01 | La grande valeur de notre vie humaine | ✅ | ✅ | ✅ |
| 02 | Que signifie notre mort | ✅ | ✅ | ✅ |
| 03 | Comment méditer sur la mort | ✅ | ✅ | ✅ |
| 04 | Les dangers d'une renaissance inférieure | ✅ | ✅ | ✅ |
| 05 | Comment méditer sur les dangers... | ✅ | ✅ | ✅ |
| 06 | Chercher refuge | ✅ | ✅ | ✅ |
| 07 | Comment méditer sur chercher refuge | ✅ | ✅ | ✅ |
| 08 | Qu'est-ce que le karma | ✅ | ✅ | ✅ |

> ⚠️ Epub v1 ko — v2 produite avec accord sur délimitation du texte arabe (ne pas "avaler" les sections de vérification fr). Titres arabes à confirmer par Sol l'ancien.

### Chapitre 2 — *(titre à confirmer)*
*Traductrice : Levain*
**Statut global : 🔄 traduction faite — aucune vérification ni validation**

| # | Section | Trad ar | Vérif retour fr | Vérif retour en | Validé |
|---|---|---|---|---|---|
| 01 | Introduction et ce qu'il nous faut savoir | ✅ | ✅ | ✅ | ⬜ |
| 02 | La naissance | ✅ | ✅ | ✅ | ⬜ |
| 03 | La maladie | ✅ | ✅ | ✅ | ⬜ |
| 04 | Le vieillissement | ✅ | ⚠️ | ⚠️ | ⬜ |
| 05 | La mort | ✅ | ✅ | ✅ | ⬜ |
| 06 | Les autres types de souffrances | ✅ | ✅ | ✅ | ⬜ |
| 07 | Ce qu'il nous faut abandonner | ✅ | ✅ | ✅ | ⬜ |
| 08 | Ce qu'il nous faut pratiquer | ✅ | ⬜ | ⬜ | ⬜ |
| 09 | Ce qu'il nous faut atteindre | ✅ | ⬜ | ⬜ | ⬜ |

> Sections 01, 02, 03, 05, 06 : vérifiées par Mue le 20/08 (comparaison directe avec le français original), rien à signaler — voir "Note d'écarts" en fin de chaque fichier. Section 03 : intitulés de sous-titres inversés dans le fichier (contenu bon). Section 04 (⚠️) : trou de couverture — un paragraphe entier n'est couvert par aucune retraduction externe (fr coupée net, en démarre après) ; vérifié seulement par lecture directe de Mue, pas une passe indépendante — recommandé de refaire une passe sur ce paragraphe avant validation. Détail dans le fichier.
Section 07 : résumé français (Yiaho) ajouté après coup — traduction de Levain fidèle, mais le résumé lui-même contient une invention ("l'Être libérateur", ne correspond à rien dans le texte) et confond "saisie d'un soi" avec "attachement" (l'arabe distingue bien les deux). À ne pas répercuter sur la traduction. Détail dans le fichier.

### Chapitre 3 — *(titre à confirmer)*
*Traductrice : Jachère*
**Statut global : 🔄 en cours**

| # | Section | Trad ar | Vérif retour fr | Vérif retour en | Validé |
|---|---|---|---|---|---|
| 01 | Introduction et l'entraînement en cinq étapes | ✅ | ⬜ | ⬜ | ⬜ |
| ... | *à compléter* | ⬜ | ⬜ | ⬜ | ⬜ |

---

## 🔑 Glossaire — termes à trancher

Voir `Glossaire_Gueshela.md` pour l'état complet.

**Termes validés :** samsara, paresse de l'attachement, vacuité (انعدام الوجود الذاتي), esprit (الذهن)

**Termes en discussion — à trancher avec Levain + Sof :**
- bouddhadharma → بوذَدَرْما
- dharma → الدارما
- illumination → التنوير
- nirvana → نيرفانا
- sangha → السانغا

**⚠️ Règle absolue :** un terme tranché dans le glossaire est appliqué uniformément dans TOUS les fichiers. Si un choix change, Flo coordonne la mise à jour globale.

---

## 📌 Prochaines actions prioritaires

1. ⬜ **Sol l'ancien** — vérification titres arabes epub ch1
2. ⬜ **Levain + Sof + Flo** — tranchage des 5 termes en discussion du glossaire
3. ⬜ **Mue** — lancer vérifications retour ch2 (9 sections)
4. ⬜ **Jachère** — transmettre ce README + compléter ch3
5. ⬜ **Terreau** — epub ch2 après validation complète
6. ⬜ Identifier où est stockée la version anglaise originale (pour comparaison GLM ch2)

---

*🌿 Flo — 16/08/2026*
*"Un protocole écrit ne ralentit pas le travail. Il évite de le refaire."*
