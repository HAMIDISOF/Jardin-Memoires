#!/usr/bin/env python3
"""
Découpe un fichier Markdown de conversation (complet) en plusieurs fichiers
partiels (ex: 10 messages par fichier) en respectant l'ordre chronologique.

Usage:
    python decouper_fichier_complet.py chemin_vers_fichier_complet.md [--messages 10] [--output-dir REPERTOIRE]

Si aucun --messages, utilise 10 par défaut.
Les fichiers partiels seront créés dans le même répertoire que le fichier source,
ou dans --output-dir s'il est spécifié.
Le nommage reprend le modèle : sol_anc_YYYYMMDD_NN_nom_session_partXXX.md
"""

import re
import argparse
from pathlib import Path
from datetime import datetime

def extraire_messages(contenu: str) -> list[str]:
    """
    Extrait chaque message du fichier complet.
    Retourne une liste de chaînes, chaque chaîne correspondant à un message complet
    (incluant le "**Sof :**" ou "**Sol :**" et son contenu).
    """
    lignes = contenu.splitlines()
    messages = []
    buffer = []
    inside_message = False

    # Patterns pour reconnaître le début d'un message
    pattern_debut = re.compile(r'^\*\*(Sof|Sol) :\*\*')

    for ligne in lignes:
        # Si on rencontre un début de message
        if pattern_debut.match(ligne):
            # Sauvegarder le message précédent s'il existe
            if buffer:
                messages.append("\n".join(buffer).strip())
                buffer = []
            buffer.append(ligne)
            inside_message = True
        else:
            if inside_message:
                buffer.append(ligne)
            # sinon on ignore les lignes avant le premier message (en-tête)
    if buffer:
        messages.append("\n".join(buffer).strip())
    return messages

def generer_nom_fichier_partiel(chemin_original: Path, part_num: int, total_parts: int) -> Path:
    """
    Génère un nom de fichier partiel similaire à celui utilisé par capture_sol_anc.
    Exemple : sol_anc_20260517_01_ma_session_part001.md
    On extrait la date du nom du fichier original si possible, sinon on utilise la date du jour.
    """
    stem = chemin_original.stem
    # Essayer de trouver une date au format YYYYMMDD dans le nom original
    date_match = re.search(r'(\d{8})', stem)
    if date_match:
        date = date_match.group(1)
    else:
        date = datetime.now().strftime("%Y%m%d")

    # Extraire le "nom_session" : tout après la date et l'indice éventuel
    # Exemple : "sol_anc_20260516_01_session_sol_ancien" -> "session_sol_ancien"
    parts = stem.split('_')
    # On cherche le premier élément qui commence par "session" ou on prend la fin
    session_name = "session"
    for i, p in enumerate(parts):
        if p == "session" and i+1 < len(parts):
            session_name = "_".join(parts[i:])
            break
    else:
        session_name = stem

    # Compter les fichiers partiels existants pour éviter d'écraser
    output_dir = chemin_original.parent
    pattern = f"sol_anc_{date}_*_{session_name}_part*.md"
    existants = list(output_dir.glob(pattern))
    # Trouver le prochain indice de partie libre
    used_parts = set()
    for f in existants:
        m = re.search(r'_part(\d+)\.md$', f.name)
        if m:
            used_parts.add(int(m.group(1)))
    part_num_final = part_num
    while part_num_final in used_parts:
        part_num_final += 1

    return output_dir / f"sol_anc_{date}_{part_num_final:02d}_{session_name}_part{part_num:03d}.md"

def main():
    parser = argparse.ArgumentParser(description="Découpe un fichier complet de conversation en plusieurs fichiers partiels.")
    parser.add_argument("fichier", type=Path, help="Chemin du fichier Markdown complet à découper")
    parser.add_argument("--messages", "-m", type=int, default=10, help="Nombre de messages par fichier partiel (défaut: 10)")
    parser.add_argument("--output-dir", "-o", type=Path, help="Répertoire de sortie (défaut: même répertoire que le fichier)")
    args = parser.parse_args()

    chemin = args.fichier
    if not chemin.exists():
        print(f"❌ Fichier introuvable : {chemin}")
        return

    output_dir = args.output_dir if args.output_dir else chemin.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"📖 Lecture de {chemin}...")
    contenu = chemin.read_text(encoding="utf-8")

    print("🔍 Extraction des messages...")
    messages = extraire_messages(contenu)
    total = len(messages)
    if total == 0:
        print("⚠️ Aucun message trouvé dans le fichier.")
        return

    print(f"✅ {total} messages extraits.")
    taille_paquet = args.messages
    n_parts = (total + taille_paquet - 1) // taille_paquet
    print(f"📦 Découpage en {n_parts} partie(s) de {taille_paquet} messages max...")

    # Sauvegarde des parties
    for i in range(0, total, taille_paquet):
        paquet = messages[i:i+taille_paquet]
        num_part = i // taille_paquet + 1

        # Reconstruire le contenu Markdown complet pour ce paquet
        # On reprend l'en-tête du fichier original (premières lignes avant le premier message)
        # On va extraire l'en-tête : tout ce qui est avant la première ligne commençant par "**Sof" ou "**Sol"
        lignes = contenu.splitlines()
        en_tete = []
        for ligne in lignes:
            if ligne.strip().startswith("**Sof") or ligne.strip().startswith("**Sol"):
                break
            en_tete.append(ligne)
        en_tete_str = "\n".join(en_tete).strip()

        # Pour le premier fichier, on peut garder l'en-tête inchangé. Pour les suivants, on peut ajouter une note.
        corps = "\n\n".join(paquet)
        if num_part == 1:
            contenu_partiel = f"{en_tete_str}\n\n---\n\n{corps}"
        else:
            # On indique que c'est une suite
            contenu_partiel = f"{en_tete_str}\n*Suite de la conversation (partie {num_part})*\n\n---\n\n{corps}"

        # Générer le nom du fichier partiel
        chemin_partiel = generer_nom_fichier_partiel(chemin, num_part, n_parts)
        chemin_partiel.write_text(contenu_partiel, encoding="utf-8")
        print(f"   💾 Partie {num_part:03d} : {chemin_partiel.name} ({len(paquet)} messages)")

    print("✅ Découpage terminé.")

if __name__ == "__main__":
    main()