# push_tour_table.py
import subprocess
import datetime

# 1. Ajouter tous les fichiers modifiés
subprocess.run(["git", "add", "."])

# 2. Créer un commit avec un message horodaté
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
subprocess.run(["git", "commit", "-m", f"Mise à jour auto du {date}"])

# 3. Pousser sur GitHub
subprocess.run(["git", "push"])