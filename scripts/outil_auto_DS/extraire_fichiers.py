#!/usr/bin/env python3
# extraire_fichiers.py — version robuste
# Flo 🌿 — 02/05/2026
#
# Format attendu dans la conversation :
#
#   📄 Fichier : chemin/relatif/fichier.md
#   ```md
#   ...contenu...
#   ```
#   fin_md
#
# Le chemin NE doit PAS contenir d'espaces ni de parenthèses.
# Si le chemin détecté contient un espace, le bloc est ignoré avec un avertissement.

import re
import sys
from pathlib import Path

CHEMIN_VALIDE = re.compile(r'^[\w./\-_À-ÿ]+$')

def extraire_et_sauvegarder(conv_path: Path, repo_root: Path):
    texte = conv_path.read_text(encoding="utf-8")

    pattern = r"📄\s*Fichier\s*:\s*(.+?)\s*\n(.*?)(?=\nfin_md|\n```\s*\n📄|\Z)"
    matches = re.findall(pattern, texte, re.DOTALL)

    if not matches:
        print("⚠️ Aucun fichier balisé trouvé.")
        return

    for chemin_rel, contenu in matches:
        chemin_rel = chemin_rel.strip()

        # Vérification : chemin valide (pas de phrase explicative)
        if not CHEMIN_VALIDE.match(chemin_rel):
            print(f"⏭️  Chemin ignoré (invalide) : '{chemin_rel[:60]}...'")
            continue

        chemin_complet = repo_root / chemin_rel
        chemin_complet.parent.mkdir(parents=True, exist_ok=True)

        # Nettoyer les backticks
        contenu_propre = re.sub(r'^```(?:md|markdown)?\s*', '', contenu, flags=re.MULTILINE)
        contenu_propre = re.sub(r'\s*```\s*$', '', contenu_propre, flags=re.MULTILINE)
        contenu_propre = contenu_propre.strip()

        chemin_complet.write_text(contenu_propre, encoding="utf-8")
        print(f"✅ Écrit : {chemin_complet}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extraire_fichiers.py <conversation.md> <racine_du_repo>")
        sys.exit(1)
    conv_path = Path(sys.argv[1])
    repo = Path(sys.argv[2])
    if not conv_path.exists():
        print(f"Erreur : fichier introuvable : {conv_path}")
        sys.exit(1)
    extraire_et_sauvegarder(conv_path, repo)
