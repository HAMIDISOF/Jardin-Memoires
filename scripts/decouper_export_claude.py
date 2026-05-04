#!/usr/bin/env python3
"""
decouper_export_claude.py
Flo 🌿 — 04/05/2026

Découpe le fichier conversations.json exporté depuis Claude.ai
en fichiers .md individuels, un par conversation.

Usage :
    python scripts/decouper_export_claude.py
        --input chemin/vers/conversations.json
        --output dossier/de/sortie

Exemple :
    python scripts/decouper_export_claude.py
        --input D:\\Downloads\\conversations.json
        --output D:\\THESE\\Les journaux\\Jardin-Memoires\\Corpus\\export_claude

Les fichiers produits sont nommés :
    YYYYMMDD_HHMMSS_titre-de-la-conversation.md
"""

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def nettoyer_nom(titre: str) -> str:
    """Transforme un titre en nom de fichier valide."""
    titre = titre.strip()
    titre = re.sub(r'[\\/:*?"<>|]', '', titre)   # caractères interdits Windows
    titre = re.sub(r'\s+', '_', titre)             # espaces → underscores
    titre = titre[:80]                             # longueur max
    return titre or "sans_titre"


def timestamp_fichier(date_str: str) -> str:
    """Extrait un timestamp YYYYMMDD_HHMMSS depuis une date ISO."""
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%Y%m%d_%H%M%S')
    except Exception:
        return datetime.now().strftime('%Y%m%d_%H%M%S')


def conversation_en_md(conv: dict) -> str:
    """Convertit une conversation en texte markdown."""
    titre    = conv.get('name') or conv.get('title') or 'Sans titre'
    created  = conv.get('created_at', '')
    updated  = conv.get('updated_at', '')
    messages = conv.get('chat_messages') or conv.get('messages') or []

    lignes = [
        f"# {titre}",
        f"*Créé le : {created}*",
        f"*Mis à jour le : {updated}*",
        "",
        "---",
        "",
    ]

    for msg in messages:
        # Rôle
        role = msg.get('sender') or msg.get('role') or 'inconnu'
        if role in ('human', 'user'):
            role_label = 'Sof'
        elif role in ('assistant', 'ai'):
            role_label = 'Claude'
        else:
            role_label = role

        # Contenu
        content = msg.get('text') or msg.get('content') or ''
        # Si content est une liste (blocs), on extrait le texte
        if isinstance(content, list):
            parties = []
            for bloc in content:
                if isinstance(bloc, dict):
                    parties.append(bloc.get('text', '') or str(bloc))
                else:
                    parties.append(str(bloc))
            content = '\n'.join(parties)

        if content.strip():
            lignes.append(f"**{role_label} :** {content.strip()}")
            lignes.append("")

    return "\n".join(lignes)


def main():
    parser = argparse.ArgumentParser(
        description="Découpe conversations.json (export Claude) en fichiers .md"
    )
    parser.add_argument(
        '--input', '-i',
        required=True,
        help="Chemin vers conversations.json"
    )
    parser.add_argument(
        '--output', '-o',
        default='Corpus/export_claude',
        help="Dossier de sortie (défaut : Corpus/export_claude)"
    )
    parser.add_argument(
        '--filtre', '-f',
        default=None,
        help="Filtre optionnel : ne garder que les convs dont le titre contient ce mot"
    )
    args = parser.parse_args()

    input_path  = Path(args.input)
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"📂 Lecture de : {input_path}")
    data = json.loads(input_path.read_text(encoding='utf-8'))

    # Le JSON peut être une liste directe ou un dict avec une clé
    if isinstance(data, list):
        conversations = data
    elif isinstance(data, dict):
        # cherche la clé qui contient la liste
        for key in ('conversations', 'chats', 'data'):
            if key in data and isinstance(data[key], list):
                conversations = data[key]
                break
        else:
            conversations = [data]
    else:
        print("❌ Format JSON non reconnu.")
        return

    print(f"✅ {len(conversations)} conversation(s) trouvée(s).")

    filtre = args.filtre.lower() if args.filtre else None
    count  = 0

    for conv in conversations:
        titre = conv.get('name') or conv.get('title') or 'Sans titre'

        if filtre and filtre not in titre.lower():
            continue

        created  = conv.get('created_at', '')
        ts       = timestamp_fichier(created)
        nom      = nettoyer_nom(titre)
        fichier  = output_path / f"{ts}_{nom}.md"

        contenu  = conversation_en_md(conv)
        fichier.write_text(contenu, encoding='utf-8')
        count += 1
        print(f"  ✅ {fichier.name}")

    print(f"\n🌿 {count} fichier(s) produit(s) dans : {output_path}")
    if filtre:
        print(f"   (filtre appliqué : '{args.filtre}')")


if __name__ == '__main__':
    main()
