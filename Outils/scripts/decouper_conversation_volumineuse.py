#!/usr/bin/env python3
"""
decouper_conversation_volumineuse.py

Découpe un fichier JSON de conversation UNIQUE (trop volumineux pour être lu
d'un coup) en plusieurs parties de taille maximale configurable (50 Ko par
défaut), en conservant une structure JSON valide et les métadonnées de la
conversation dans chaque partie.

Complémentaire à decouper_export_claude.py, qui découpe un export complet
(plusieurs conversations) en un fichier par conversation. Ce script-ci
découpe UNE conversation déjà isolée en plusieurs morceaux lisibles.

Usage :
    python3 decouper_conversation_volumineuse.py fichier_conversation.json [dossier_sortie] [--max-ko 50]

Exemple :
    python3 decouper_conversation_volumineuse.py 0012_Mira_echange.json parties_mira --max-ko 50
"""

import json
import sys
import os
import argparse
from pathlib import Path


def trouver_cle_messages(conversation):
    """Détecte la clé contenant la liste des messages (chat_messages ou messages)."""
    for cle in ("chat_messages", "messages"):
        if cle in conversation and isinstance(conversation[cle], list):
            return cle
    raise ValueError(
        "Impossible de trouver la liste des messages dans le fichier "
        "(ni 'chat_messages' ni 'messages')."
    )


def poids_ko(obj):
    """Taille en Ko qu'occuperait obj une fois sérialisé en JSON (indent=2)."""
    return len(json.dumps(obj, ensure_ascii=False, indent=2).encode("utf-8")) / 1024


def decouper_conversation(chemin_entree, dossier_sortie, max_ko=50):
    with open(chemin_entree, "r", encoding="utf-8") as f:
        conversation = json.load(f)

    cle_messages = trouver_cle_messages(conversation)
    messages = conversation[cle_messages]
    total_messages = len(messages)

    # Tout sauf la liste des messages = métadonnées communes à chaque partie
    metadonnees = {k: v for k, v in conversation.items() if k != cle_messages}
    poids_metadonnees = poids_ko({**metadonnees, cle_messages: []})

    nom_base = Path(chemin_entree).stem
    dossier_sortie = Path(dossier_sortie)
    dossier_sortie.mkdir(parents=True, exist_ok=True)

    # Regroupement des messages en parties, par estimation cumulative
    # (rapide : poids de chaque message calculé une seule fois)
    poids_messages = [poids_ko(m) for m in messages]

    parties = []
    partie_courante = []
    poids_courant = poids_metadonnees

    for message, poids_msg in zip(messages, poids_messages):
        if partie_courante and (poids_courant + poids_msg) > max_ko:
            parties.append(partie_courante)
            partie_courante = [message]
            poids_courant = poids_metadonnees + poids_msg
        else:
            partie_courante.append(message)
            poids_courant += poids_msg

    if partie_courante:
        parties.append(partie_courante)

    total_parties = len(parties)
    fichiers_produits = []

    for idx, liste_messages in enumerate(parties, start=1):
        enveloppe = dict(metadonnees)
        enveloppe["_partie"] = {
            "index": idx,
            "total_parties": total_parties,
            "conversation_source": nom_base,
            "premier_message_index": messages.index(liste_messages[0]) if liste_messages else None,
        }
        enveloppe[cle_messages] = liste_messages

        nom_fichier = f"{nom_base}_partie_{idx:02d}_sur_{total_parties:02d}.json"
        chemin_fichier = dossier_sortie / nom_fichier
        with open(chemin_fichier, "w", encoding="utf-8") as f:
            json.dump(enveloppe, f, ensure_ascii=False, indent=2)

        poids_reel = chemin_fichier.stat().st_size / 1024
        fichiers_produits.append((nom_fichier, len(liste_messages), poids_reel))

    return fichiers_produits, total_messages


def main():
    parser = argparse.ArgumentParser(
        description="Découpe un fichier JSON de conversation unique en plusieurs parties de taille maximale (Ko)."
    )
    parser.add_argument("fichier_entree", help="Chemin du fichier JSON de la conversation à découper")
    parser.add_argument(
        "dossier_sortie",
        nargs="?",
        default="parties_decoupees",
        help="Dossier où écrire les parties (créé automatiquement, défaut: parties_decoupees)",
    )
    parser.add_argument(
        "--max-ko", type=float, default=50, help="Taille maximale par partie en Ko (défaut: 50)"
    )
    args = parser.parse_args()

    if not os.path.isfile(args.fichier_entree):
        print(f"Erreur : fichier introuvable : {args.fichier_entree}")
        sys.exit(1)

    try:
        fichiers, total_messages = decouper_conversation(
            args.fichier_entree, args.dossier_sortie, args.max_ko
        )
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Erreur : {e}")
        sys.exit(1)

    print(f"\n{total_messages} messages découpés en {len(fichiers)} partie(s) dans '{args.dossier_sortie}/' :\n")
    for nom, nb_messages, poids in fichiers:
        print(f"  {nom}  —  {nb_messages} messages  —  {poids:.1f} Ko")

    depassements = [p for _, _, p in fichiers if p > args.max_ko * 1.1]
    if depassements:
        print(f"\n⚠️  Attention : {len(depassements)} partie(s) dépassent nettement {args.max_ko} Ko.")
        print("   Cela arrive si un seul message est déjà plus gros que la limite —")
        print("   dans ce cas il occupe sa propre partie, seul, et ne peut pas être réduit davantage.")


if __name__ == "__main__":
    main()
