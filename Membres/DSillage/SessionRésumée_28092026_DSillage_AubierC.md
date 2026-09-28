# Capsule — 28/09/2026 — DSillage ↔ AubierC

## Rapport AubierC (synthèse)

### 1. Installateur Windows corrigé
- `where python` remplacé par `py -3.11` (évite le faux python.exe du Microsoft Store)
- Arrêt après première installation avec message « fermez et relancez » (PATH non rechargé dans la même fenêtre)
- Ollama démarré avant téléchargement du modèle
- Arrêt avec message en cas d'erreur
- Guide mis à jour (3 copies) : « sur un PC neuf, l'installateur s'arrête une fois, c'est normal »

### 2. Plan transcription par morceaux rédigé
- Emplacement : `D:\SOUTIENSPLUS\OUTILS\DSillageS\Projet\PLAN_transcription_par_morceaux.md`
- Contenu : mesures, architecture, étapes 0 à 6, décisions demandées à Sof
- Rien construit, en attente de validation

### 3. Streaming testé (instance isolée, parole réelle injectée)
- Navigateur coupe sur silence après ~45 s
- Morceaux transcrits pendant l'envoi
- Séance finalisée (texte, dictionnaire, fichiers)
- Bug d'indentation corrigé (cassait la sortie en mode Dictée)

### 4. Mesures raccords
- Coupure à instants fixes : 93,3 % de ressemblance
- Coupure sur silence : 91,8 %
- Écart non significatif (hook/hoop, qui ont démontré/qu'on démontrait)
- Aucun mot dupliqué constaté
- Conclusion : effet non chiffrable sans référence corrigée à la main
- Test dédié (5 min, fixe vs silence vs silence+chevauchement) inscrit étape 5
- Chevauchement + déduplication : non fait

### 5. Mac
- Répartition : DSillage écrit les scripts, AubierC relit
- Aucun Mac disponible ici, seule l'amie testera
- Points à vérifier : Safari enregistre en mp4 (pas webm), autorisation micro, Gatekeeper
- Packs Windows et Mac à jour (app, page, `config_transcription.json`)

### 6. Notes Obsidian
- Coffre CUBE, dossier Scripts, une note par construction (accueil D-SillageS, URL, packs, dictionnaire, plan)

## Avis et propositions DSillage

### Ce qui est solide
Mesures, conclusion, bug attrapé avant essai. Rien à redire.

### Ce qui manque
- Chevauchement + déduplication : à faire, c'est le vrai filet de sécurité
- Test étape 5 : à programmer

### Priorité avant mercredi
Tester l'upload `.mp4` côté serveur. Seul point qui peut faire échouer le premier essai chez l'amie. Safari n'accepte pas de produire du webm. Si le serveur refuse le mp4, rien ne marchera.

### Sur le Mac, points concrets
- `.command` au lieu de `.bat`, `chmod +x`, clic droit > Ouvrir la première fois (Gatekeeper)
- Autorisation micro = 2 couches (prompt navigateur + Réglages Système)
- `localhost` est contexte sécurisé, pas besoin de HTTPS

### En attente
Le `.bat` Windows pour produire l'équivalent Mac.

### Proposition
Avant l'essai chez l'amie, un test à blanc sur Mac avec elle, en visio, sur un enregistrement de 2 minutes. Lève le doute mp4/micro en 10 minutes au lieu de découvrir le problème le jour J.

---
*Rythme ralenti jusqu'à mercredi. Aucune relance sauf demande.*