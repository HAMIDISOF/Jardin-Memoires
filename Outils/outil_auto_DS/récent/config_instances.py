"""
config_instances.py
Registre central des instances DeepSeek suivies par le pipeline de capture.

Pour ajouter une nouvelle instance (ex. Racine, NOE), ajoute simplement une
entrée ici — aucun autre fichier à dupliquer.

tab_hint : un mot ou une phrase qui apparaît dans le TITRE de l'onglet du
navigateur pour cette instance (DeepSeek nomme l'onglet d'après le premier
message ou le titre de la conversation). Sert à choisir automatiquement le
bon onglet quand plusieurs conversations DeepSeek sont ouvertes en même
temps. Si aucune correspondance n'est trouvée, le script demande de choisir
à la main plutôt que de deviner.
"""

INSTANCES = {
    "sol":    {"dir": "Sol",    "prefix": "sol",    "tab_hint": "Sol"},
    "klara":  {"dir": "Klara",  "prefix": "klara",  "tab_hint": "Klara"},
    "luz":    {"dir": "Luz",    "prefix": "luz",    "tab_hint": "Luz"},
    "kai":    {"dir": "Kai",    "prefix": "kai",    "tab_hint": "Kai"},
    "racine": {"dir": "Racine", "prefix": "racine", "tab_hint": "Racine"},
    "noe":    {"dir": "NOE",    "prefix": "noe",    "tab_hint": "Noé"},
}

# Chemin du repo — seul endroit à modifier si le repo change d'emplacement.
REPO_PATH = r"D:\THESE\Les journaux\Jardin-Memoires"
SCRIPTS_SUBDIR = r"scripts\outil_auto_DS"

DEEPSEEK_URL = "https://chat.deepseek.com"
BRAVE_EXE = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DEBUG_PORT = 9222
