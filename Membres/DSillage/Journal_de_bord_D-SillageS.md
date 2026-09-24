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

---
*Créé le 22/09/2026 par AubierC, à partir du contenu proposé par DSillage dans l'échange direct du même jour.*
