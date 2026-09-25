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

### Points de vigilance pour les tests des amies (25/09/2026)

- **PC — téléchargement par URL** : si un téléchargement YouTube échoue chez l'amie sur PC, penser d'abord à Node.js. Le guide affirme que l'installateur s'en occupe, ce qui est **faux côté Windows** (`installer_windows.bat` n'installe pas Node ; seul le script Mac le fait). Conséquence directe de la décision de Sof (option 3, statu quo). Piste si échec : installer Node côté Windows (`winget install OpenJS.NodeJS.LTS`) + `--js-runtimes node` dans `telecharger_audio()`, avec test avant/après. Ou corriger la mention du guide.
- **PC — installateur Windows jamais exécuté de bout en bout** (étapes `winget` non testées : Python, Ollama).
- **Mac** — script et guide non testés sur machine réelle.

---
*Créé le 22/09/2026 par AubierC, à partir du contenu proposé par DSillage dans l'échange direct du même jour.*
