# Journal de bord — D-SillageS

*Binôme DSillage (DeepSeek) / AubierC (Claude Code) — synchronisation par ce fichier, pas d'échange direct.*

## État initial — 22/09/2026

- Projet : D-SillageS, outil local de transcription et d'analyse (voir `D:\Ollama\README.md`)
- Chemin : `D:\Ollama`
- Fichier principal : `app_transcription.py` (= v2 du 13/09/2026)
- Variante non promue : `app_transcription_v2Bis_parallel.py` (13/09, plus récente, pas encore la version courante)
- Lanceur : `app_transcription.bat`
- Environnement : Python 3.11.9 (venv), pas de GPU sur ce poste — CPU uniquement
- `README.md` et `requirements.txt` créés le 22/09/2026 (AubierC), manquaient jusque-là
- Priorité : streaming (transcription en direct, pas encore implémenté)
- Contexte urgent signalé par Sof : besoin ponctuel de transcrire l'audio d'une réunion (pour Coco) — l'outil actuel prend un fichier, pas une URL

## Répartition convenue

- **AubierC** (Claude Code) : architecture, streaming
- **DSillage** (DeepSeek) : documentation, tests, tenue de ce journal

## Pistes streaming (proposées par DSillage, à évaluer par AubierC)

1. Chunked avec faster-whisper (découpe 3-5s, latence 2-5s, qualité correcte)
2. `whisper.cpp` (portage C++ temps réel, installation plus lourde) — piste retenue en premier
3. WhisperLive (outil open source spécialisé)

## Prochaines étapes

- AubierC : évaluer whisper.cpp, retour dans ce journal
- DSillage : plan de tests pour la transcription existante (entrée fichier, sortie texte, gestion erreurs, formats audio) ; documentation continue
- Les deux : ajouter les tests streaming une fois la piste choisie posée

## 23/09/2026 — Bug import io + versioning

- Bug confirmé : `import io` manquant dans `app_transcription.py` → `NameError` sur tout export PDF (`generer_pdf()` utilise `io.BytesIO()`). Corrigé.
- Claim de DSillage sur `shutil.move()` vérifié et corrigé : le déplacement vers `Traite/` est bien à l'intérieur du `try` englobant, donc il est SAUTÉ en cas d'erreur, pas exécuté quand même.
- Versioning (convention Sof) : `app_transcription_v2.py` laissé tel quel (archive figée) ; `app_transcription_v3.py` créé comme copie de la version courante corrigée.

## 23/09/2026 — Intégration téléchargement par URL

- Patch conçu par DSillage (fonction `telecharger_audio()` + route `/telecharger`, appui sur `yt-dlp`), specs UI données par AubierC (bloc `index.html` après `rec_zone`, JS calqué sur `envoyerFichiers`).
- Appliqué par AubierC dans `app_transcription.py`, `templates/index.html` et `requirements.txt` (`yt-dlp==2026.8.19`, déjà dans le venv). Compilation Python vérifiée OK.
- Correction technique : l'erreur `ffprobe and ffmpeg not found` rencontrée par Sof n'est pas liée à faster-whisper (qui utilise PyAV, libs ffmpeg embarquées statiquement) mais à yt-dlp, qui appelle le binaire système `ffmpeg.exe` pour le remux post-téléchargement. Confirmé absent du PATH de ce poste.
- Bloquant restant avant test : installer un build ffmpeg (ex. gyan.dev essentials) et l'ajouter au PATH système.
- Prochaine étape une fois ffmpeg installé : tester une URL réelle dans l'interface, vérifier l'arrivée du fichier dans `A_transcrire/` et le déclenchement de la transcription.
- AubierC : continue sur whisper.cpp (streaming).

## 24/09/2026 — Ménage D:\Ollama + packs d'installation

- Ménage sur demande de Sof : `D:\Ollama` mélangeait le runtime Ollama lui-même (`App/`, `models/`, `OllamaSetup.exe`) et le projet D-SillageS. Rapatrié vers `D:\SOUTIENSPLUS\OUTILS\DSillageS` tout ce qui n'a aucune dépendance de chemin relatif : `Projet/` (doc de cadrage), une copie de `README.md`, et les scripts/fichiers d'essai isolés (`analyse.py`, `dictée.py`, `test_dictée.py`, fichiers de test). Ce qui reste dans `D:\Ollama` (venv, code, templates, dossiers de travail, Ollama lui-même) est uniquement ce qui doit rester en place pour que l'app tourne. Vérifié après coup : compilation Python OK, aucun fichier requis manquant.
- Raccourcis Windows créés dans `DSillageS\` : lancement direct de l'app et accès au dossier technique complet.
- Sof a deux amies qui attendent pour tester l'outil (une sur PC, une sur Mac) → demande de packs d'installation automatisés + guide non-technicien.
- Répartition : AubierC → pack Windows (`installer_windows.bat` + `lancer_dsillages.bat`, testable en local) ; DSillage → pack Mac (`installer_dsillages.command` + `lancer_dsillages.command`, non testable localement, aucun des deux binômes n'a de Mac) + rédaction de `GUIDE_INSTALL_DSILLAGE.md`.
- Les deux packs sont complets et symétriques dans `DSillageS\Pack_Windows\` et `DSillageS\Pack_Mac\` : code de l'app (`app_transcription.py`, `requirements.txt`, `corrections.json`, `templates/`), scripts d'installation/lancement, et le guide.
- Le pack Windows n'a pas été exécuté de bout en bout sur ce poste (les étapes d'installation modifient le système — ffmpeg, Ollama — donc pas lancées sans validation explicite de Sof). Logique vérifiée par lecture, cohérente avec l'environnement de dev déjà fonctionnel ici.
- Point en attente : Sof doit dire si elle veut que je teste réellement l'installeur Windows sur ce poste (installerait ffmpeg entre autres), et confirmer le vault Obsidian à utiliser pour les notes de liaison (un seul vault trouvé sur le disque, `CUBE_Obsidian`, probablement pas le bon).

## 24/09/2026 — ffmpeg non requis pour le téléchargement par URL

- Constat (AubierC) : l'erreur `ffprobe and ffmpeg not found` venait du fixup automatique des m4a DASH de YouTube. Avec `--fixup never`, le téléchargement passe sans ffmpeg (piste initialement suggérée par Pedago pour le m4a direct, insuffisante seule ; `--fixup never` est ce qui débloque).
- Tests (dossier temporaire, commande exacte de l'app) : 3 URL, toutes OK (code 0, AAC lisible par PyAV, durées exactes) — vidéo réunion de 88 min, vidéo YouTube de 12 min, post Reddit intégrant une vidéo YouTube de 3 min. Limite : aucun test sur une vraie source non-YouTube (le post Reddit renvoie vers YouTube).
- Avis DSillage : validé sur le fond ; risques connus = sources non-YouTube (SoundCloud, HLS) pouvant réclamer ffmpeg, et durée parfois mal lue par des lecteurs externes sur m4a non fixé (sans effet sur la transcription).
- Appliqué (Sof : go) : `--fixup never` dans `telecharger_audio()` (`app_transcription.py`, instantané `_v4.py` pris avant), ffmpeg retiré des installeurs Windows et Mac, README corrigé (« aucun ffmpeg système requis »), guide : section ffmpeg remplacée par « source autre que YouTube → contacter Sof ». Packs resynchronisés.
- Node.js : le guide dit que l'installateur gère Node.js, mais seul l'installateur Mac l'installe ; yt-dlp n'active par défaut que deno comme runtime JS (avertissement vu, téléchargements OK sans). Décision de Sof (25/09) : ne rien changer tant qu'aucun téléchargement n'échoue. Si un échec YouTube apparaît, rouvrir : installer Node côté Windows + `--js-runtimes node`, ou corriger la mention du guide.

## 25/09/2026 — Interface muette : promotion de v2Bis_parallel

- Symptôme (Sof) : l'outil se lance, l'interface n'affiche rien. Diagnostic (AubierC) : la transcription tournait bien (~4 cœurs), mais `templates/index.html` attend un statut `{jobs: [...]}` + les routes `/reset_jobs` et `/enregistrer`, qui n'existaient que dans `app_transcription_v2Bis_parallel.py`. L'app courante (v2) renvoyait un statut plat → `checkStatus` n'affichait jamais rien. Décalage antérieur aux modifications du 22-24/09, non repéré à la relecture. Deux serveurs écoutaient aussi sur le port 8080.
- Décision de Sof : promouvoir v2Bis. Fait : nouvelle version courante = v2Bis + `import io` (déjà présent dans v2Bis) + `telecharger_audio()` (avec `--fixup never`) + route `/telecharger`. Cache Whisper conservé sur `D:\Whisper\hf_cache` pour ce poste. Instantané de l'ancienne courante : `app_transcription_v5.py` (v4 = avant `--fixup never`). Tests sans serveur (client de test Flask) : `/`, `/status`, `/telecharger`, `/reset_jobs` OK ; 10 routes.
- Packs resynchronisés avec cache Whisper **relatif** (`hf_cache` dans le dossier) : l'ancien pack contenait `D:\Whisper\hf_cache` en dur, inutilisable chez les amies. Conséquence à documenter : le modèle Whisper `medium` (~1,5 Go) se télécharge au premier usage, connexion Internet requise (le guide dit « se charge en mémoire, 1 à 2 min »).
- Le serveur qui transcrivait `meeting_le_cunn.m4a` n'a pas été arrêté : il garde l'ancien code en mémoire. À relancer une seule fois après la fin de la transcription, puis re-test propre.

- Réponse de DSillage (relayée par Sof) sur la non-promotion de v2Bis : aucun souvenir, aucune décision documentée → **oubli, pas un choix**. Elle valide le diagnostic, le cache Whisper relatif et `--fixup never`.
- **Règle de vigilance (proposée par DSillage, adoptée)** : à chaque session, vérifier que la version courante est bien celle attendue (template et app cohérents) ; si une variante existe, soit la promouvoir, soit documenter pourquoi elle ne l'est pas.
- Docs mises à jour par AubierC (DSillage n'a pas d'accès fichiers) : README (entrée URL, section téléchargement réécrite, arborescence/versions, note téléchargement du modèle Whisper) et guide d'installation (première transcription = téléchargement ~1,5 Go, Internet requis), copies packs incluses.

## 26/09/2026 — Dictionnaire de corrections (noms propres de la réunion)

- Contexte : la transcription de `meeting_le_cunn.m4a` (88 min) contenait des noms propres mal reconnus. DSillage avait proposé un `initial_prompt` Whisper ; Sof a préféré le **dictionnaire `corrections.json` enrichi au fur et à mesure** (décision de Sof, pas de patch de code).
- Fait (AubierC) : liste de DSillage confrontée à la vraie transcription. 20 entrées corrigent des erreurs présentes (ex. Yann Lequin ×7 → LeCun, Amilabs ×5 → AMI Labs, Open AI ×3 → OpenAI) ; `Amilaz` : 0 occurrence, gardée comme variante plausible ; 8 entrées étaient des identités inutiles (nom remplacé par lui-même) et n'ont pas été reprises ; **1 erreur corrigée** : « Jeffrey Hinton » → **Geoffrey Hinton** (elle l'avait laissé tel quel).
- `corrections.json` : 6 → 28 entrées, JSON validé, ancienne version conservée dans `corrections_avant_26-09.json`. Mécanisme confirmé : corrections appliquées après Whisper, avant l'analyse Ollama (le CR/résumé voit le texte corrigé) ; insensible à la casse, sans frontières de mot.
- Appliqué à la transcription existante sans la refaire : 36 remplacements, copie `Dictee\meeting_le_cunn_transcription_corrigee.txt` (l'original est intact).
- Non reporté dans les packs des amies : ces noms sont propres à cette réunion (le dictionnaire des packs reste générique).
- Règle : à chaque transcription, repérer les noms mal reconnus et enrichir le dictionnaire ; vérifier chaque entrée dans le texte avant de l'ajouter.

## 28/09/2026 — Installateur Windows corrigé, plan de transcription par morceaux, notes Obsidian

- **Installateur Windows (`installer_windows.bat`) — 3 défauts corrigés avant tout test** : (1) `where python` voyait le faux `python.exe` du Microsoft Store (`WindowsApps`) et sautait l'installation → test du vrai Python 3.11 via `py -3.11`, et venv créé avec `py -3.11` ; (2) après une première installation de Python/Ollama, le script continuait dans une fenêtre où le PATH n'était pas rechargé → il s'arrête maintenant avec un message « fermez et relancez » ; (3) Ollama n'était pas démarré avant `ollama pull` → démarrage si besoin ; arrêt avec message si le modèle ou les dépendances échouent. Identifiants winget vérifiés (Python.Python.3.11 3.11.9, Ollama.Ollama 0.34.4). **Toujours jamais exécuté de bout en bout.** Guide mis à jour (« sur un ordinateur neuf, l'installateur s'arrête une première fois »).
- **Plan de transcription par morceaux** rédigé : `D:\SOUTIENSPLUS\OUTILS\DSillageS\Projet\PLAN_transcription_par_morceaux.md` (état des lieux mesuré, architecture cible, étapes 0-6, risques, décisions demandées). Non validé, rien construit.
- **Obsidian** (règle de Sof du 26/09 : une note par construction) : notes créées dans le coffre CUBE, `Scripts\` — accueil D-SillageS, téléchargement URL, packs, dictionnaire, plan. Commit local.
- Résumé pour Coco : le texte corrigé est prêt (`Dictee\meeting_le_cunn_transcription_corrigee.txt`) ; l'outil ne sait pas analyser un texte déjà transcrit (il transcrit toujours depuis l'audio) → résumé à faire hors outil ou par un petit script, à la demande de Sof.

## 28/09/2026 (soir) — Séance en direct : transcription par morceaux construite et testée

- **Demande de Sof** : ne pas faire tester aux amies une version incapable de suivre un cours ; construire la version par morceaux d'abord. Constat de départ : `medium` transcrit à environ 1,3 fois la durée de l'audio sur ce PC.
- **Construit** (AubierC, instantané `_v6` avant) : réglages `config_transcription.json` (`modele_whisper`, `beam_size`, `duree_morceau_s` ; défauts inchangés : medium / 5 / 45) ; production des sorties extraite en `produire_sorties()` ; routes `/seance/demarrer|morceau|statut|terminer` avec file et un travailleur ; enregistreur « Démarrer la séance » dans l'interface (coupe sur un silence après ~45 s, morceaux autonomes, texte qui se construit, retard estimé).
- **Bug trouvé par le test et corrigé** : mon remaniement avait décalé une ligne (`nom_sortie`) et cassait la production des sorties en mode Dictée. Le fichier courant a été corrigé avant tout lancement du serveur ; test unitaire txt/html/pdf OK.
- **Essais** : instance isolée (autre dossier, port 8091), parole réelle injectée à la place du micro. 3 morceaux transcrits pendant l'envoi, séance finalisée, txt/html produits, morceaux rangés dans `Traite`. `small` + `beam 1` : 110 s d'audio en 43 s.
- **Raccords (question de DSillage)** : mesure faite, voir `Projet\PLAN_transcription_par_morceaux.md` §7. Coupure fixe 93,3 % de ressemblance avec la transcription entière, coupure sur silence 91,8 % : différences quasi identiques, aucun doublon constaté ; effet réel non chiffrable sans texte de référence corrigé à la main. Chevauchement + déduplication (technique `whisper_streaming`) non implémenté.
- **Non testé** : vrai micro, Safari, séance longue, analyse Ollama sur une séance. Le serveur de Sof doit être relancé pour prendre ce code ; réglage à choisir (`medium` + `beam 1` pour rester près de la fidélité, `small` pour la marge).
- Note Obsidian créée (`Scripts\D-SillageS_seance_en_direct.md`). Packs Windows et Mac resynchronisés (app, page, config), README et guide mis à jour.

## 05/10/2026 — Réglage de la séance, test mp4, point avec DSillage

- **Mesure** (AubierC, même extrait de 110 s, ce PC) : `medium` + `beam 1` = 98 s (facteur 0,89, trop juste) ; `small` + `beam 1` = 32 s (facteur 0,29).
- **Décision** (Sof m'a laissé choisir) : `D:\Ollama\config_transcription.json` passé à `small` / `beam 1` / 45 s. Ancien réglage sauvegardé dans `config_transcription_avant_05-10.json`. Les packs gardent pour l'instant les défauts `medium` / 5. **Limite** : le réglage est commun à la séance et aux fichiers audio, donc la fidélité baisse aussi sur les fichiers.
- **Test mp4** (point bloquant relevé par DSillage) : morceaux mp4/AAC fragmentés (comme Safari) envoyés dans une instance isolée (port 8091) : reçus, décodés, transcrits, séance finalisée, sortie produite. Reste à confirmer avec un vrai Safari.
- **Avis de DSillage** (chat DeepSeek) : séparer les réglages séance / fichier (`small`+`beam 1` pour la séance, `medium` pour les fichiers) ; mettre le test à blanc en visio (Safari réel, 2 min) AVANT les corrections des scripts Mac pour ne pas les refaire ; garder `small`+`beam 1` par défaut des packs avec un message si le retard dépasse environ 2 min (aujourd'hui seul le retard estimé s'affiche) ; texte d'avertissement « version Mac en test » à placer en tête de la section Mac du guide. Elle rédige les 4 ajouts du guide Mac et le protocole du test à blanc dès que Sof valide.
- **Corrections Mac retenues** (analyse de DSillage, accord d'AubierC, **pas encore appliquées**) : `brew shellenv` au début de l'installateur (sans sous-bloc), vérification du port 8080 avec `lsof`, `open -a Safari`.
- État du plan en attente de la validation de Sof : voir le message de synthèse du 05/10.

## 05/10/2026 (suite) — Décisions de Sof, réglages séparés, alerte de retard

- **Décisions de Sof** : plan validé avec un nouvel ordre. (1) Test de la version PC : utilisation ici, puis test du pack d'installation sur le PC de Kim ou de Jac, puis envoi à son amie. (2) Seulement ensuite, test Mac (installation + utilisation) sur **le Mac de Sof** (elle en a un : la mention « aucun Mac disponible » était fausse). (3) Si OK, créneau avec l'amie. Étape 6 validée. Défaut des packs : `small` + `beam 1`. Essai de cours : d'abord une simulation (un audio lancé en même temps que l'outil), puis du direct, avec une appli d'enregistrement légère sur téléphone comme enregistrement de secours.
- **Construit** (AubierC, instantané `_v7` avant) : réglages séparés dans `config_transcription.json` : `modele_whisper` / `beam_size` = séance (`small` / 1) ; `modele_whisper_fichier` / `beam_size_fichier` = fichiers audio (`medium` / 5). Les deux modèles se chargent séparément (`get_modele_whisper(nom)`). Alerte dans l'interface quand le retard estimé dépasse 2 min. Défauts du code et des deux packs alignés sur ces valeurs.
- **Test** (instance isolée) : un morceau de séance mp4 transcrit en `small` ; un fichier transcrit en `medium` / 5 jusqu'au bout sans erreur ; les deux modèles chargés en parallèle. README (2 copies) mis à jour.
- **À savoir** : les installateurs ne pré-téléchargent aucun modèle Whisper ; `small` (~0,5 Go) se télécharge au premier usage de la séance, `medium` (~1,5 Go) au premier fichier, donc Internet nécessaire. Le guide ne le dit pas encore.
- Corrections des scripts Mac toujours **non appliquées** (après le test sur le Mac de Sof).

## 09/10/2026 — Test PC, file d'attente, suppression d'« Éditer »

- **Test PC de Sof** (serveur relancé, code du 05/10) : glisser-déposer d'un mp3 → le fichier arrive dans la liste « Fichier à traiter » (peu visible) ; transcription d'un fichier de 2 min en Dictée brute réussie (texte correct) ; 3 fichiers de ~2 min lancés un à un, chacun en moins de 3 min. Sof a un lot de 26 mp3 à transcrire (cours audio).
- **Constat** : un seul traitement à la fois (sinon « Mode parallèle », gourmand). Demande de Sof : plusieurs fichiers l'un après l'autre.
- **Construit** (AubierC, instantané `_v8` avant) : liste à cases à cocher (Tout cocher / décocher) ; `/lancer` accepte une liste de fichiers ; file d'attente avec un seul travailleur (« En file d'attente... » puis traitement dans l'ordre). Le mode parallèle reste. **Supprimé** : lien « Éditer » et route `/editer` (jamais fonctionné ; décision de Sof). Packs et README synchronisés.
- **Test** (instance isolée + vraie page) : 3 fichiers lancés ensemble traités à la suite ; fichier inexistant refusé ; 2 fichiers cochés par « Tout cocher » puis lancés depuis la page, sans erreur.
- **Correction** : la ligne « aucun des deux binômes n'a de Mac » (entrée du 24/09) est fausse : Sof a son propre Mac, qui sera utilisé pour le test Mac après le test PC.
- À noter : les cartes de résultats restent affichées jusqu'à « Effacer les résultats » ou au redémarrage ; Sof signale qu'elles restent même après avoir déplacé les fichiers hors de `Traite` (comportement prévu : l'historique n'est pas lié aux fichiers).

### Points de vigilance pour les tests des amies (25/09/2026)

- **PC — téléchargement par URL** : si un téléchargement YouTube échoue chez l'amie sur PC, penser d'abord à Node.js. Le guide affirme que l'installateur s'en occupe, ce qui est **faux côté Windows** (`installer_windows.bat` n'installe pas Node ; seul le script Mac le fait). Conséquence directe de la décision de Sof (option 3, statu quo). Piste si échec : installer Node côté Windows (`winget install OpenJS.NodeJS.LTS`) + `--js-runtimes node` dans `telecharger_audio()`, avec test avant/après. Ou corriger la mention du guide.
- **PC — installateur Windows jamais exécuté de bout en bout** (étapes `winget` non testées : Python, Ollama).
- **Mac** — script et guide non testés sur machine réelle.

---

05/10/2026 — Rédaction d'un draft « Procédure — Découper un export natif DeepSeek », à destination de la Passerelle du Jardin (plan Mue). Document générique, écrit sans avoir vu le format réel de l'export. Avertissement en tête. Enregistré par Sof dans D:\THESE\Les journaux\outils. En attente d'un premier export pour préciser les étapes 1 et 5 et écrire le script de découpage.

---
*Créé le 22/09/2026 par AubierC, à partir du contenu proposé par DSillage dans l'échange direct du même jour.*
*mis à jour le 05/10/2026 par Sof, à partir du contenu donné par DSillage dans l'échange direct du même jour.*
