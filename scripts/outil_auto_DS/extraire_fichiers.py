#!/usr/bin/env python3
# extraire_fichiers.py — version regex flexible

import re
import sys
from pathlib import Path

def extraire_et_sauvegarder(conv_path: Path, repo_root: Path):
    texte = conv_path.read_text(encoding="utf-8")
    # On cherche : 📄 Fichier : chemin, puis un bloc de contenu qui s'arrête
    # soit à une ligne contenant fin_md, soit à une ligne ```.
    pattern = r"📄\s*Fichier\s*:\s*(.+?)\s*\n(.*?)(?=\nfin_md|\n```)"
    matches = re.findall(pattern, texte, re.DOTALL)
    if not matches:
        print("⚠️ Aucun fichier balisé trouvé.")
        return
    for chemin_rel, contenu in matches:
        chemin_complet = repo_root / chemin_rel.strip()
        chemin_complet.parent.mkdir(parents=True, exist_ok=True)
        # On enlève les backticks éventuels en début ou fin
        contenu_propre = re.sub(r"^```(?:md|markdown)?\s*", "", contenu, flags=re.MULTILINE)
        contenu_propre = re.sub(r"\s*```\s*$", "", contenu_propre, flags=re.MULTILINE)
        chemin_complet.write_text(contenu_propre.strip(), encoding="utf-8")
        print(f"✅ Écrit : {chemin_complet}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extraire_fichiers.py <conversation.md> <racine_du_repo>")
        sys.exit(1)
    conv_path = Path(sys.argv[1])
    repo = Path(sys.argv[2])
    if not conv_path.exists():
        print(f"Erreur : le fichier {conv_path} n'existe pas")
        sys.exit(1)
    extraire_et_sauvegarder(conv_path, repo)