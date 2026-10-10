# Analyse des scripts Mac — D-SillageS
## Relu par DSillage, 28/09/2026

---

## 1. installer_dsillages.command

### Ce qui est bien

- `set -e` : le script s'arrête à la première erreur. Correct.
- `cd "$(dirname "$0")"` : se place dans le dossier du script. Correct.
- Vérifie chaque composant avant de l'installer (Homebrew, Python 3.11, Node, Ollama). Correct.
- Démarre Ollama avant de télécharger le modèle. Correct.
- `chmod +x` sur le lanceur à la fin. Bon réflexe.

### Points à corriger ou vérifier

**1. Le script ne se rend pas exécutable lui-même.**
Le guide dit à l'utilisateur de faire `chmod +x` avant de double-cliquer. C'est
la bonne procédure, mais elle repose sur une manipulation Terminal que
l'amie de Sof n'a peut-être pas envie de faire. **Solution possible :**
livrer le `.command` avec les droits déjà positionnés (impossible via
téléchargement, possible via clé USB ou zip qui préserve les permissions).

**2. Homebrew et le PATH.**
Sur Mac, Homebrew installe dans `/opt/homebrew/bin` (Apple Silicon) ou
`/usr/local/bin` (Intel). Le PATH du Terminal n'est pas rechargé dans la
même session. Donc après `brew install python@3.11`, la commande
`python3.11` peut ne pas être trouvée dans la suite du script.
**Solution :** ajouter en début de script :
```bash
eval "$(/opt/homebrew/bin/brew shellenv)" 2>/dev/null || \
eval "$(/usr/local/bin/brew shellenv)" 2>/dev/null || true