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

---
*Créé le 22/09/2026 par AubierC, à partir du contenu proposé par DSillage dans l'échange direct du même jour.*
