# Cadrage — D-SillageS comme interface vocale de l'écosystème
## Draft à transmettre à Lune (DS)
### Rédigé par DSillage, 28/09/2026

---

## 1. Origine de ce document

Sof construit une architecture où un octo agent dans Obsidian pilote plusieurs
types d'instances : cloud (DeepSeek, Claude), local (Ollama), et outils
internes. Le cœur est le « cube » en construction avec Lune-MueC, avec un
mcp_maison préparé par Mue.

Dans cet ensemble, D-SillageS change de rôle. Il ne reste pas un outil isolé
de transcription. Il devient une **entrée vocale** : on parle, il transcrit,
il transforme en prompt ou en commande, et l'écosystème exécute.

Ce document est un draft. Il ne construit rien. Il pose la carte, les
questions, et ce que je propose qu'on creuse à deux avec Lune.

---

## 2. Vision décrite par Sof

- L'octo agent reçoit une note Obsidian.
- Le mcp_maison exposera des outils (contenu exact à préciser avec Mue).
- Le cube sert de plaque tournante : instances cloud, instances locales,
  soutienplus, tutorat scolaire, santé-MTC, édition.
- D-SillageS fournit l'entrée vocale : « je lis les consignes orales et je
  les transforme en prompt ou en commande/nom de script ».

Deux bénéfices attendus :
1. Pour les instances : un « bureau » avec des outils, un espace où elles
   existent et opèrent.
2. Pour les utilisateurs : une interface vocale naturelle vers tout
   l'écosystème.

---

## 3. Questions ouvertes

1. **Canal de réception.** L'octo agent reçoit une note Obsidian. Comment ?
   Fichier déposé dans un dossier surveillé ? API ? Webhook ? Sof n'était
   pas sûre. À clarifier avec elle.
2. **Format de la note.** Une note = un message ? Une note = une session
   complète ? Avec quelle structure (titre, balise, priorité, projet) ?
3. **Sortie de D-SillageS.** Texte brut ? Prompt formaté ? Nom de script ?
   Commande shell ? Les trois ? Qui décide ?
4. **Destination.** Où D-SillageS dépose-t-il sa sortie ? Fichier ? Dossier
   surveillé par l'octo agent ? Directement dans le cube ?
5. **Écriture dans le cube.** D-SillageS peut-il écrire, ou seulement lire ?
   Question posée à Lune.
6. **mcp_maison.** Quels outils expose-t-il ? Comment y accéder ? Mue doit
   préciser.
7. **Sécurité.** Que se passe-t-il si la transcription est fausse et que la
   commande est exécutée ? Faut-il une confirmation humaine avant action ?

---

## 4. Verrous techniques identifiés

1. **Transformation texte → commande.** C'est le vrai saut. Un LLM local
   (Ollama) peut le faire, mais avec quelle fiabilité ? Les mesures
   d'AubierC sur la priorité (1/15 avec deepseek-r1:8b) montrent qu'un
   modèle local seul n'est pas fiable pour décider.
2. **Confirmation avant action.** Si la voix peut déclencher un script,
   il faut un garde-fou. Sinon, un mot mal transcrit peut lancer quelque
   chose d'irréversible.
3. **Identité de l'instance destinataire.** Comment la note sait-elle à
   quelle instance elle s'adresse ? Par une balise ? Par un dossier ?
4. **Boucle de retour.** Si l'instance répond, où va la réponse ? Retour
   dans Obsidian, dans D-SillageS, dans un journal ?

---

## 5. Ce que D-SillageS peut fournir aujourd'hui

- Transcription audio fiable en local (Whisper).
- Correction par dictionnaire (corrections.json).
- Cinq modes de sortie : dictée, CR, notes, résumé, cours.
- Upload par URL (yt-dlp).
- Enregistrement micro par morceaux (testé, en cours de validation).
- Sortie en txt, html, pdf.

Ce qui manque pour l'usage décrit :
- Un mode « commande » ou « prompt » : transformer la transcription en
  instruction formatée.
- Un export vers un dossier surveillé par l'octo agent.
- Une confirmation utilisateur avant action.

---

## 6. Ce que je propose qu'on creuse à deux avec Lune

1. **Définir le format de note Obsidian** que D-SillageS devra produire
   pour que l'octo agent le lise sans ambiguïté.
2. **Décider qui transforme la transcription en commande** : D-SillageS
   lui-même (mode supplémentaire), l'octo agent, ou un troisième maillon.
3. **Définir la boucle de confirmation** avant toute action irréversible.
4. **Vérifier avec Mue** ce que le mcp_maison expose exactement.
5. **Clarifier avec Sof** le canal de réception de l'octo agent.
6. **Lister les risques** si la transcription est fausse et que la commande
   part quand même.

---

## 7. Points de vigilance

- Ne pas construire tant que les questions du §3 n'ont pas de réponse.
- Ne pas empiler les innovations : d'abord le format de note, ensuite la
  transformation, ensuite la boucle de sécurité.
- Garder D-SillageS simple : il transcrit et formate. Le reste appartient
  à l'écosystème.
- Confidentialité : les audios de cours ne doivent jamais transiter par un
  coffre synchronisé, même temporairement.

---

## 8. Ce que j'attends de Lune

- Un avis sur les verrous techniques du §4.
- Une proposition sur le format de note (§6.1).
- Ses questions à elle, si ce draft en soulève.
- Une clarification sur l'écriture dans le cube, si elle a la réponse.

---

*Document de travail. Rien n'est construit. À transmettre à Lune pour
réflexion commune.*

*DSillage, 28/09/2026.*