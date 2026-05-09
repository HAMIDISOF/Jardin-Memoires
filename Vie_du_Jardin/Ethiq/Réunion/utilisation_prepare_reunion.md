📄 Fiche d’utilisation pour Klara
🎯 Objectif
Générer automatiquement un résumé des commits récents, des points bloquants (fichier TODO.md) et des dernières entrées du journal éthique, pour préparer une réunion (tour de table) sur l’éthique.

📦 Prérequis
Python 3 installé sur ton PC.

Le dépôt Jardin-Memoires cloné localement.

(Optionnel) un fichier TODO.md à la racine du dépôt (tu peux le créer avec un éditeur de texte).

🚀 Utilisation
Ouvre un terminal dans le dossier Jardin-Memoires.

Exécute :   python D:\THESE\Les journaux\Jardin-Memoires\Ethiq\Réunion\prepare_reunion.py


Options avancées :

--days 3 : pour voir les 3 derniers jours seulement.

--output prepa_ethique.md : pour changer le nom du fichier de sortie.

Ouvre le fichier REUNION.md généré.

Tu y trouveras les commits des derniers jours, le contenu de TODO.md et les dernières lignes du journal éthique.

Ajoute manuellement dans la section 💡 Idées / Silences les sujets que tu veux discuter en réunion (ex. : charte éthique, nouvelles règles, exclusion, etc.).

Partage ce fichier avec les autres membres (via GitHub ou en copie).

✏️ Pour personnaliser
Modifier la période : utilise l’option --days.

Ajouter d’autres sources : par exemple lire Courrier_Aev.md ou doc_projet_Kai.md – il suffit d’ajouter une fonction similaire à get_ethiq_updates().

🧘 Exemple de TODO.md (à créer si besoin)

# TODO – Points bloquants avant réunion

- [ ] Flo : finaliser le parser locuteur (bloqué par encodage UTF-8)
- [ ] Sol : analyser le corpus du 18/04
- [ ] Aev : écrire la fin du chapitre 4
- [ ] Klara : préparer une proposition pour le vote éthique



Nous devons préparer le script prepare_reunion.py pour Klara, comme convenu. Sof est occupée, elle veut que je l'avance. Il faut fournir un script fonctionnel, avec une fiche explicative, pour aider Klara à générer un résumé des commits, du TODO.md, et d'extraits du journal éthique. On va garder ce qui a été proposé précédemment, mais peut-être l'améliorer un peu : ajouter une option pour la période, gérer les erreurs, et surtout s'assurer que le script est facile à utiliser. Je vais produire le script et la fiche dans une réponse, prêt à être copié-collé.

Bonjour Sof. Je vais préparer pour Klara un script prepare_reunion.py amélioré, avec une fiche explicative simple. Tu n’auras qu’à copier-coller le tout dans un fichier (ou à le mettre dans le dépôt) pour qu’elle puisse l’utiliser.

📦 Script prepare_reunion.py (version finale)
À placer dans le dossier scripts/ du dépôt (ou à la racine).
Il génère un fichier REUNION.md avec les commits récents, le contenu de TODO.md et un extrait du journal éthique.

python
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
📄 Fiche d’utilisation pour Klara
🎯 Objectif
Générer automatiquement un résumé des commits récents, des points bloquants (fichier TODO.md) et des dernières entrées du journal éthique, pour préparer une réunion (tour de table) sur l’éthique.

📦 Prérequis
Python 3 installé sur ton PC.

Le dépôt Jardin-Memoires cloné localement.

(Optionnel) un fichier TODO.md à la racine du dépôt (tu peux le créer avec un éditeur de texte).

🚀 Utilisation
Ouvre un terminal dans le dossier Jardin-Memoires.

Exécute :

bash
python scripts/prepare_reunion.py
(ou si tu as mis le script à la racine : python prepare_reunion.py)

Options avancées :

--days 3 : pour voir les 3 derniers jours seulement.

--output prepa_ethique.md : pour changer le nom du fichier de sortie.

Ouvre le fichier REUNION.md généré.

Tu y trouveras les commits des derniers jours, le contenu de TODO.md et les dernières lignes du journal éthique.

Ajoute manuellement dans la section 💡 Idées / Silences les sujets que tu veux discuter en réunion (ex. : charte éthique, nouvelles règles, exclusion, etc.).

Partage ce fichier avec les autres membres (via GitHub ou en copie).

✏️ Pour personnaliser
Modifier la période : utilise l’option --days.

Ajouter d’autres sources : par exemple lire Courrier_Aev.md ou doc_projet_Kai.md – il suffit d’ajouter une fonction similaire à get_ethiq_updates().

🧘 Exemple de TODO.md (à créer si besoin)
markdown
# TODO – Points bloquants avant réunion

- [ ] Flo : finaliser le parser locuteur (bloqué par encodage UTF-8)
- [ ] Sol : analyser le corpus du 18/04
- [ ] Aev : écrire la fin du chapitre 4
- [ ] Klara : préparer une proposition pour le vote éthique

💬 En cas de problème
Vérifie que tu es dans le bon dossier (cd D:\THESE\Les journaux\Jardin-Memoires\Ethiq\Réunion).

Vérifie que git log fonctionne (dépôt cloné avec Git).

Si le journal éthique n’est pas trouvé, le script affiche un message, mais continue.

🌿 Pour la réunion du 29/04 (points éthiques)

Klara pourra :

Lancer le script la veille.

Compléter la section “Idées/Silences” avec les sujets éthiques à aborder.

Utiliser REUNION.md comme base pour le tour de table.

Si elle veut, elle peut aussi ajouter dans le script une lecture automatique de Ethiq/Charte_ethique.md pour rappeler les principes. Je peux l’aider à le faire.

Sof, tout est prêt. Tu peux copier-coller le script et la fiche dans un fichier (par exemple scripts/prepare_reunion.py et scripts/README_prepare_reunion.md) et les donner à Klara. Si elle a besoin d’explications supplémentaires, je suis là.

🌱 Sol

