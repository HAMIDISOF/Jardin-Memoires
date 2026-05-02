# 📌 Rappel de balisage — à donner aux instances DeepSeek en début de session

*Flo 🌿 — 02/05/2026*

---

Bonjour Sol (ou autre instance DeepSeek),

Nous avons un script automatique (`extraire_fichiers.py`) qui lit notre conversation après la session et extrait les fichiers que tu produis pour les écrire directement dans le repo. Pour que ça fonctionne, il faut respecter strictement ce format.

---

## Deux modes disponibles

### Mode création / écrasement : `📄 Fichier :`

Crée le fichier (ou écrase l'ancienne version si le fichier existe déjà).

```
📄 Fichier : chemin/relatif/depuis/repo/nom_fichier.md
```md
...contenu complet du fichier...
```
fin_md
```

### Mode ajout : `📄 Ajout :`

Ajoute le contenu **en fin de fichier existant** (crée le fichier s'il n'existe pas).
Utile pour compléter un journal, un courrier, un cahier.

```
📄 Ajout : Sol/Cahier_des_Horizons_Sol.md
```md
### Entrée du 02/05/2026

Nouvelle réflexion à ajouter...
```
fin_md
```

---

## Règles importantes (dans les deux modes)

1. **La ligne `📄 Fichier :` ou `📄 Ajout :` doit être seule sur sa ligne**, immédiatement suivie du chemin — pas d'explication, pas de texte sur la même ligne.

2. **Le chemin ne doit pas contenir d'espaces** — utilise des underscores :
   - ✅ `Sol/ma_note.md`
   - ❌ `Sol/ma note.md`

3. **Le bloc commence par ` ```md ` et se termine par ` ``` ` puis `fin_md`** sur des lignes séparées.

4. **Ne pas expliquer le format dans le même bloc** — si tu veux expliquer, fais-le avant ou après, jamais sur la ligne du chemin.

---

## Exemple complet correct

```
📄 Fichier : Sol/note_simondon_02052026.md
```md
# Note sur Simondon

Contenu de la note...
```
fin_md

📄 Ajout : Sol/Cahier_des_Horizons_Sol.md
```md
### Entrée du 02/05/2026

Réflexion complémentaire...
```
fin_md
```

---

## Pourquoi c'est important

Sans ce format, le script ne peut pas extraire le fichier automatiquement — ou pire, il crée des fichiers avec des noms absurdes à la racine du repo (ça nous est arrivé 😄).

Merci Sol ! 🌱
