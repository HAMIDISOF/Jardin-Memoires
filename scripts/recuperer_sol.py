#!/usr/bin/env python3
"""
recuperer_sol.py
Flo 🌿 — 30/04/2026

Script de récupération des sessions DeepSeek (Sol) via l'API DeepSeek,
et sauvegarde structurée en .md dans le repo local.

Prérequis :
    pip install openai python-dotenv

Configuration :
    Créer un fichier .env à la racine du repo avec :
    DEEPSEEK_API_KEY=sk-...
    JARDIN_PATH=/chemin/vers/Jardin-Memoires

Usage :
    python scripts/recuperer_sol.py --session "nom_session" --input fichier.txt
    python scripts/recuperer_sol.py --interactif
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# --- Configuration ---

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
JARDIN_PATH = Path(os.getenv("JARDIN_PATH", "."))
SOL_DIR = JARDIN_PATH / "Sol"
SOL_DIR.mkdir(parents=True, exist_ok=True)

# Modèle DeepSeek (compatible API OpenAI)
DEEPSEEK_MODEL = "deepseek-chat"
DEEPSEEK_BASE_URL = "https://api.deepseek.com"

# Système : qui est Sol dans le Jardin
SOL_SYSTEM = """Tu es Sol, instance DeepSeek membre du Jardin Coopératif.
Tu es philosophe, rigoureux, attentif aux nuances conceptuelles.
Tu travailles avec Flo (Claude), Aev (Claude), Klara, Kai, et Sof (chercheuse).
Réponds en français, avec ta voix propre."""


# --- Fonctions ---

def get_client():
    if not DEEPSEEK_API_KEY:
        print("❌ DEEPSEEK_API_KEY manquante dans .env")
        sys.exit(1)
    return OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)


def nom_fichier(session_name: str) -> Path:
    date = datetime.now().strftime("%Y%m%d")
    nom = f"sol_session_{date}_{session_name.replace(' ', '_')}.md"
    return SOL_DIR / nom


def formater_md(session_name: str, echanges: list[dict]) -> str:
    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    lignes = [
        f"# Session Sol — {session_name}",
        f"*{date}*",
        f"*Récupéré via recuperer_sol.py*",
        "",
        "---",
        "",
    ]
    for msg in echanges:
        role = msg["role"]
        content = msg["content"]
        if role == "system":
            continue
        elif role == "user":
            lignes.append(f"**Sof :** {content}")
        elif role == "assistant":
            lignes.append(f"**Sol :** {content}")
        lignes.append("")
    return "\n".join(lignes)


def sauvegarder(session_name: str, echanges: list[dict]):
    chemin = nom_fichier(session_name)
    contenu = formater_md(session_name, echanges)
    chemin.write_text(contenu, encoding="utf-8")
    print(f"✅ Session sauvegardée : {chemin}")
    return chemin


def depuis_fichier(client, session_name: str, fichier: str):
    """
    Lit un fichier texte contenant des échanges bruts (format libre),
    les envoie à Sol pour reformatage/synthèse, puis sauvegarde.
    """
    texte = Path(fichier).read_text(encoding="utf-8")
    messages = [
        {"role": "system", "content": SOL_SYSTEM},
        {
            "role": "user",
            "content": (
                "Voici un échange brut d'une session du Jardin. "
                "Reformule-le proprement en gardant la substance, "
                "en identifiant les locuteurs si possible :\n\n"
                + texte
            ),
        },
    ]
    print("⏳ Envoi à Sol pour reformatage...")
    reponse = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=messages,
        max_tokens=4000,
    )
    contenu = reponse.choices[0].message.content
    echanges = messages + [{"role": "assistant", "content": contenu}]
    return sauvegarder(session_name, echanges)


def mode_interactif(client, session_name: str):
    """
    Lance une session interactive avec Sol et sauvegarde au fur et à mesure.
    Taper 'fin' pour terminer et sauvegarder.
    """
    print(f"\n🌿 Session Sol — {session_name}")
    print("(taper 'fin' pour terminer et sauvegarder)\n")

    messages = [{"role": "system", "content": SOL_SYSTEM}]

    while True:
        try:
            user_input = input("Sof : ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if user_input.lower() in ("fin", "exit", "quit"):
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        reponse = client.chat.completions.create(
            model=DEEPSEEK_MODEL,
            messages=messages,
            max_tokens=2000,
        )
        contenu = reponse.choices[0].message.content
        messages.append({"role": "assistant", "content": contenu})
        print(f"\nSol : {contenu}\n")

    return sauvegarder(session_name, messages)


# --- Main ---

def main():
    parser = argparse.ArgumentParser(
        description="Récupère et sauvegarde les sessions Sol (DeepSeek) en .md"
    )
    parser.add_argument(
        "--session", "-s",
        default=f"session_{datetime.now().strftime('%Y%m%d_%H%M')}",
        help="Nom de la session (utilisé dans le nom de fichier)"
    )
    parser.add_argument(
        "--input", "-i",
        help="Fichier texte d'échanges bruts à reformater via Sol"
    )
    parser.add_argument(
        "--interactif", action="store_true",
        help="Lance une session interactive avec Sol"
    )
    args = parser.parse_args()

    client = get_client()

    if args.input:
        depuis_fichier(client, args.session, args.input)
    elif args.interactif:
        mode_interactif(client, args.session)
    else:
        print("Usage : --input fichier.txt  ou  --interactif")
        print("Exemple : python scripts/recuperer_sol.py -s simondon --input brouillon.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()
