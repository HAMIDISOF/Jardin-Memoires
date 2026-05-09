# prepare_reunion.py
# Génère un résumé des avancées et points bloquants avant une réunion.
# Usage : python prepare_reunion.py [--days 7] [--output REUNION.md]

import subprocess
import os
import argparse
from datetime import datetime, timedelta

def get_git_logs(days=7):
    """Récupère les commits des derniers jours."""
    since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    cmd = f'git log --pretty=format:"- %h %an : %s" --since="{since}"'
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout if result.stdout else "Aucun commit récent."
    except Exception as e:
        return f"Erreur lors de la récupération des logs : {e}"

def get_todo_items():
    """Lit le fichier TODO.md s'il existe."""
    if os.path.exists("TODO.md"):
        with open("TODO.md", "r", encoding="utf-8") as f:
            return f.read()
    else:
        return "Aucun fichier TODO.md trouvé. Crée-le pour lister les points bloquants."

def get_ethiq_updates():
    """Extrait les dernières entrées du journal éthique (fichier principal)."""
    ethiq_file = "Ethiq/journal_ethique_21032026.md"
    if os.path.exists(ethiq_file):
        with open(ethiq_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Prend les 20 dernières lignes non vides pour avoir les entrées récentes
            recent = [l for l in lines if l.strip()][-20:]
            return "".join(recent) if recent else "(fichier vide ou trop court)"
    else:
        return "Journal éthique non trouvé."

def generate_meeting_notes(days, output_file):
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    notes = f"""# 📅 Préparation réunion – {now}

## 📌 Dernières avancées (Git, {days} jours)
{get_git_logs(days)}

## 🚧 Points bloquants (TODO.md)
{get_todo_items()}

## 📖 Dernières entrées du journal éthique
{get_ethiq_updates()}

## 💡 Idées / Silences / Questions ouvertes
*(À remplir pendant la réunion)*

---
*Fichier généré automatiquement par prepare_reunion.py*
"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(notes.strip())
    print(f"✅ {output_file} généré avec succès.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=7, help="Nombre de jours à remonter pour les commits (défaut 7)")
    parser.add_argument("--output", type=str, default="REUNION.md", help="Nom du fichier de sortie")
    args = parser.parse_args()
    generate_meeting_notes(args.days, args.output)