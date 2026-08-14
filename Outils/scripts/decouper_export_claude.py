#!/usr/bin/env python3
"""
Découpe le fichier conversations.json (export Claude.ai) en un fichier JSON
par conversation, nommé d'après le titre de la conversation, préfixé par
un numéro d'ordre chronologique (basé sur created_at) pour garder l'ordre
même une fois les fichiers triés alphabétiquement dans un dossier.

Usage :
    python3 decouper_export_claude.py conversations.json dossier_de_sortie

Si vous avez téléchargé un .zip contenant conversations.json, dézippez-le
d'abord (clic droit > extraire, ou `unzip export.zip`).
"""

import json
import re
import sys
from pathlib import Path


def slugify(name: str, fallback: str) -> str:
    """Transforme un nom de conversation en nom de fichier sûr."""
    name = (name or "").strip()
    if not name:
        name = fallback
    # Remplace tout ce qui n'est pas lettre/chiffre/espace/tiret par rien
    name = re.sub(r"[^\w\s\-]", "", name, flags=re.UNICODE)
    name = re.sub(r"\s+", "_", name.strip())
    return name[:80] if name else fallback


def main():
    if len(sys.argv) != 3:
        print("Usage : python3 decouper_export_claude.py conversations.json dossier_de_sortie")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    output_dir.mkdir(parents=True, exist_ok=True)

    with input_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        print("Format inattendu : je m'attendais à une liste de conversations.")
        print("Le fichier fourni contient un objet de type:", type(data))
        sys.exit(1)

    def get_created(conv):
        # Le champ standard de l'export Claude est created_at (ISO 8601)
        return conv.get("created_at") or conv.get("updated_at") or ""

    # Tri chronologique global des conversations
    conversations = sorted(data, key=get_created)

    seen_names = {}
    manifest = []

    for i, conv in enumerate(conversations, start=1):
        name = conv.get("name") or conv.get("summary") or ""
        uuid = conv.get("uuid", f"conv{i}")
        created = get_created(conv)

        base_slug = slugify(name, fallback=uuid)

        # Évite les doublons de nom de fichier
        count = seen_names.get(base_slug, 0)
        seen_names[base_slug] = count + 1
        suffix = f"_{count+1}" if count else ""

        # Préfixe numérique pour garder l'ordre chrono au tri alphabétique
        filename = f"{i:04d}_{base_slug}{suffix}.json"

        # Trie aussi les messages à l'intérieur de la conversation, par sécurité
        messages = conv.get("chat_messages", [])
        try:
            messages_sorted = sorted(messages, key=lambda m: m.get("created_at", ""))
            conv["chat_messages"] = messages_sorted
        except Exception:
            pass  # si la structure diffère, on garde l'ordre d'origine

        out_path = output_dir / filename
        with out_path.open("w", encoding="utf-8") as f:
            json.dump(conv, f, ensure_ascii=False, indent=2)

        manifest.append({
            "fichier": filename,
            "nom_conversation": name or "(sans titre)",
            "cree_le": created,
            "nb_messages": len(messages),
        })

        print(f"[{i:04d}] {filename}  ({len(messages)} messages, {created})")

    # Petit récapitulatif pour s'y retrouver
    manifest_path = output_dir / "_manifeste.json"
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print(f"\n{len(conversations)} conversations écrites dans {output_dir}")
    print(f"Récapitulatif : {manifest_path}")


if __name__ == "__main__":
    main()
