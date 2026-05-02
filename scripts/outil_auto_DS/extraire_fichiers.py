#!/usr/bin/env python3
# extraire_fichiers.py — version robuste avec mode création et ajout
# Flo 🌿 — 02/05/2026
#
# Deux balises supportées :
#
#   📄 Fichier : chemin/relatif/fichier.md   → crée ou écrase le fichier
#   📄 Ajout : chemin/relatif/fichier.md     → ajoute en fin de fichier (crée si absent)
#
# Le chemin NE doit PAS contenir d'espaces ni de parenthèses.
# Le bloc de contenu doit être encadré par ```md ... ``` puis fin_md.

import re
import sys
from pathlib import Path

CHEMIN_VALIDE = re.compile(r'^[\w./\-_\u00C0-\u00FF]+$')

# Pattern générique : capture le mode (Fichier|Ajout), le chemin, et le contenu
PATTERN = re.compile(
    r'\U0001F4C4\s*(Fichier|Ajout)\s*:\s*(.+?)\s*\n(.*?)(?=\nfin_md|\n\U0001F4C4|\Z)',
    re.DOTALL
)


def nettoyer_contenu(contenu: str) -> str:
    contenu = re.sub(r'^```(?:md|markdown)?\s*', '', contenu, flags=re.MULTILINE)
    contenu = re.sub(r'\s*```\s*$', '', contenu, flags=re.MULTILINE)
    return contenu.strip()


def extraire_et_sauvegarder(conv_path: Path, repo_root: Path):
    texte = conv_path.read_text(encoding='utf-8')
    matches = PATTERN.findall(texte)

    if not matches:
        print('⚠️  Aucun fichier balisé trouvé.')
        return

    for mode, chemin_rel, contenu in matches:
        chemin_rel = chemin_rel.strip()

        if not CHEMIN_VALIDE.match(chemin_rel):
            print(f'⏭️  Chemin ignoré (invalide) : "{chemin_rel[:60]}"')
            continue

        chemin_complet = repo_root / chemin_rel
        chemin_complet.parent.mkdir(parents=True, exist_ok=True)
        contenu_propre = nettoyer_contenu(contenu)

        if mode == 'Ajout':
            # Append en fin de fichier
            with chemin_complet.open('a', encoding='utf-8') as f:
                f.write('\n\n' + contenu_propre)
            print(f'✅ Ajout dans : {chemin_complet}')
        else:
            # Création / écrasement
            chemin_complet.write_text(contenu_propre, encoding='utf-8')
            print(f'✅ Écrit : {chemin_complet}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python extraire_fichiers.py <conversation.md> <racine_du_repo>')
        sys.exit(1)
    conv_path = Path(sys.argv[1])
    repo = Path(sys.argv[2])
    if not conv_path.exists():
        print(f'Erreur : fichier introuvable : {conv_path}')
        sys.exit(1)
    extraire_et_sauvegarder(conv_path, repo)
