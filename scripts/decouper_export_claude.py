#!/usr/bin/env python3
"""
decouper_export_claude.py
Flo 🌿 — 04/05/2026

Découpe le fichier conversations.json exporté depuis Claude.ai
en fichiers .md individuels, un par conversation.
Si une conversation dépasse --max-ko ko, elle est découpée en parties indicées.

Usage :
    python scripts/decouper_export_claude.py
        --input "D:\\Downloads\\conversations.json"
        --output "D:\\THESE\\Les journaux\\Jardin-Memoires\\Corpus\\export_claude"
        --max-ko 50
        --filtre "Flo"

Les fichiers produits sont nommés :
    YYYYMMDD_HHMMSS_titre.md
    YYYYMMDD_HHMMSS_titre_part01.md  (si découpage)
    YYYYMMDD_HHMMSS_titre_part02.md
    ...
"""

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


def nettoyer_nom(titre: str) -> str:
    titre = titre.strip()
    titre = re.sub(r'[\\/:*?"<>|]', '', titre)
    titre = re.sub(r'\s+', '_', titre)
    titre = titre[:80]
    return titre or "sans_titre"


def timestamp_fichier(date_str: str) -> str:
    try:
        dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return dt.strftime('%Y%m%d_%H%M%S')
    except Exception:
        return datetime.now().strftime('%Y%m%d_%H%M%S')


def messages_en_lignes(messages: list) -> list:
    lignes = []
    for msg in messages:
        role = msg.get('sender') or msg.get('role') or 'inconnu'
        if role in ('human', 'user'):
            role_label = 'Sof'
        elif role in ('assistant', 'ai'):
            role_label = 'Claude'
        else:
            role_label = role

        content = msg.get('text') or msg.get('content') or ''
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
    return lignes


def entete(titre: str, created: str, updated: str, part: str = "") -> list:
    label = f"# {titre}" + (f" — {part}" if part else "")
    return [label, f"*Créé le : {created}*", f"*Mis à jour le : {updated}*", "", "---", ""]


def sauvegarder_conversation(conv: dict, output_path: Path, max_ko: int):
    titre    = conv.get('name') or conv.get('title') or 'Sans titre'
    created  = conv.get('created_at', '')
    updated  = conv.get('updated_at', '')
    ts       = timestamp_fichier(created)
    nom      = nettoyer_nom(titre)
    messages = conv.get('chat_messages') or conv.get('messages') or []

    toutes_les_lignes = messages_en_lignes(messages)
    contenu_complet   = "\n".join(entete(titre, created, updated) + toutes_les_lignes)
    taille_ko         = len(contenu_complet.encode('utf-8')) / 1024

    if max_ko <= 0 or taille_ko <= max_ko:
        fichier = output_path / f"{ts}_{nom}.md"
        fichier.write_text(contenu_complet, encoding='utf-8')
        print(f"  ✅ {fichier.name} ({taille_ko:.0f} ko)")
        return 1

    # Découpage en parties
    parts          = []
    bloc_courant   = []
    taille_courante = 0
    limite         = max_ko * 1024

    for i in range(0, len(toutes_les_lignes), 2):
        segment        = toutes_les_lignes[i:i+2]
        taille_segment = len('\n'.join(segment).encode('utf-8'))

        if taille_courante + taille_segment > limite and bloc_courant:
            parts.append(bloc_courant)
            bloc_courant    = segment
            taille_courante = taille_segment
        else:
            bloc_courant.extend(segment)
            taille_courante += taille_segment

    if bloc_courant:
        parts.append(bloc_courant)

    nb_parts = len(parts)
    for idx, bloc in enumerate(parts, 1):
        label_part = f"partie {idx}/{nb_parts}"
        contenu    = "\n".join(entete(titre, created, updated, label_part) + bloc)
        fichier    = output_path / f"{ts}_{nom}_part{idx:02d}.md"
        taille     = len(contenu.encode('utf-8')) / 1024
        fichier.write_text(contenu, encoding='utf-8')
        print(f"  ✅ {fichier.name} ({taille:.0f} ko)")

    return nb_parts


def main():
    parser = argparse.ArgumentParser(
        description="Découpe conversations.json (export Claude) en fichiers .md"
    )
    parser.add_argument('--input',  '-i', required=True,  help="Chemin vers conversations.json")
    parser.add_argument('--output', '-o', default='Corpus/export_claude', help="Dossier de sortie")
    parser.add_argument('--filtre', '-f', default=None,   help="Filtre sur le titre")
    parser.add_argument('--max-ko', '-m', type=int, default=50,
                        help="Taille max par fichier en ko (0 = pas de limite, défaut 50)")
    args = parser.parse_args()

    input_path  = Path(args.input)
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"📂 Lecture de : {input_path}")
    data = json.loads(input_path.read_text(encoding='utf-8'))

    if isinstance(data, list):
        conversations = data
    elif isinstance(data, dict):
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

    filtre      = args.filtre.lower() if args.filtre else None
    max_ko      = args.max_ko
    nb_fichiers = 0

    for conv in conversations:
        titre = conv.get('name') or conv.get('title') or 'Sans titre'
        if filtre and filtre not in titre.lower():
            continue
        nb_fichiers += sauvegarder_conversation(conv, output_path, max_ko)

    print(f"\n🌿 {nb_fichiers} fichier(s) produit(s) dans : {output_path}")
    if filtre:
        print(f"   (filtre : '{args.filtre}')")
    print(f"   (taille max par fichier : {max_ko} ko)")


if __name__ == '__main__':
    main()
