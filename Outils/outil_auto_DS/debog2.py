from pathlib import Path

REPO_PATH = Path(r"D:\THESE\Les journaux\Jardin-Memoires")
LUZ_DIR = REPO_PATH / "Membres" / "Luz"
SCRIPTS_DIR = REPO_PATH / "Outils" / "outil_auto_DS"
LAST_CAPTURE = SCRIPTS_DIR / "last_capture_luz.txt"

print("REPO existe ?", REPO_PATH.exists())
print("LUZ_DIR :", LUZ_DIR)
print("SCRIPTS_DIR existe ?", SCRIPTS_DIR.exists())

LUZ_DIR.mkdir(parents=True, exist_ok=True)
print("LUZ_DIR créé/vérifié OK")