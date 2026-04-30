#!/usr/bin/env python3
"""
capture_sol.py
Flo 🌿 — 30/04/2026

Capture la conversation DeepSeek en cours dans ton Chrome déjà ouvert,
et sauvegarde en .md dans le dossier Sol/ du repo.

Prérequis :
    pip install playwright
    playwright install chromium

Étape 1 : lancer Chrome avec le port de débogage ouvert (une seule fois) :
    Windows :
        "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
    Mac :
        /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
    Linux :
        google-chrome --remote-debugging-port=9222

Étape 2 : ouvrir DeepSeek dans ce Chrome et te connecter normalement.

Étape 3 : lancer ce script :
    python scripts/outil_auto_DS/capture_sol.py --session "nom_session"

Le fichier .md est créé dans Sol/ avec la date et le nom de session.
"""

import argparse
import re
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

# --- Configuration ---
REPO_PATH = Path(__file__).resolve().parents[2]  # racine du repo
SOL_DIR = REPO_PATH / "Sol"
SOL_DIR.mkdir(parents=True, exist_ok=True)

CHROME_DEBUG_PORT = 9222
DEEPSEEK_URL = "https://chat.deepseek.com"


# --- Extraction ---

def extraire_messages(page) -> list[dict]:
    """Extrait les messages de la conversation DeepSeek visible."""
    messages = []

    # Les messages utilisateur
    user_els = page.query_selector_all('[class*="userMessage"], [class*="human"], [data-role="user"]')
    # Les messages assistant
    assistant_els = page.query_selector_all('[class*="assistantMessage"], [class*="assistant"], [data-role="assistant"]')

    # Approche alternative : récupérer tous les blocs de message dans l'ordre
    # en cherchant les conteneurs de tour de parole
    blocs = page.query_selector_all('[class*="message"], [class*="chat-message"], [class*="turn"]')

    if blocs:
        for bloc in blocs:
            texte = bloc.inner_text().strip()
            if not texte:
                continue
            # Heuristique : si le bloc contient un indicateur de rôle
            html = bloc.inner_html()
            if 'user' in html.lower() or 'human' in html.lower():
                messages.append({"role": "Sof", "content": texte})
            elif 'assistant' in html.lower() or 'deepseek' in html.lower() or 'sol' in html.lower():
                messages.append({"role": "Sol", "content": texte})
            else:
                # Fallback : alterner
                if not messages or messages[-1]["role"] == "Sol":
                    messages.append({"role": "Sof", "content": texte})
                else:
                    messages.append({"role": "Sol", "content": texte})
    else:
        # Fallback : texte brut de la page entière
        texte_brut = page.inner_text("body")
        messages.append({"role": "brut", "content": texte_brut})

    return messages


def formater_md(session_name: str, messages: list[dict]) -> str:
    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    lignes = [
        f"# Conversation Sol — {session_name}",
        f"*Capturé le {date} via capture_sol.py*",
        "",
        "---",
        "",
    ]
    for msg in messages:
        role = msg["role"]
        contenu = msg["content"]
        if role == "brut":
            lignes.append("*[Extraction brute — sélecteurs non trouvés]*")
            lignes.append("")
            lignes.append(contenu)
        else:
            lignes.append(f"**{role} :** {contenu}")
            lignes.append("")
    return "\n".join(lignes)


def nom_fichier(session_name: str) -> Path:
    date = datetime.now().strftime("%Y%m%d_%H%M")
    nom = f"sol_{date}_{session_name.replace(' ', '_')}.md"
    return SOL_DIR / nom


# --- Main ---

def main():
    parser = argparse.ArgumentParser(
        description="Capture la conversation DeepSeek depuis Chrome déjà ouvert"
    )
    parser.add_argument(
        "--session", "-s",
        default=f"session_{datetime.now().strftime('%Y%m%d_%H%M')}",
        help="Nom de la session (pour le nom de fichier)"
    )
    parser.add_argument(
        "--port", "-p",
        type=int,
        default=CHROME_DEBUG_PORT,
        help=f"Port de débogage Chrome (défaut: {CHROME_DEBUG_PORT})"
    )
    args = parser.parse_args()

    print(f"🔌 Connexion à Chrome sur le port {args.port}...")

    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(f"http://localhost:{args.port}")
        except Exception as e:
            print(f"❌ Impossible de se connecter à Chrome.")
            print(f"   Assure-toi que Chrome est lancé avec --remote-debugging-port={args.port}")
            print(f"   Erreur : {e}")
            return

        # Trouver l'onglet DeepSeek
        page = None
        for context in browser.contexts:
            for p_page in context.pages:
                if DEEPSEEK_URL in p_page.url:
                    page = p_page
                    break

        if page is None:
            print(f"❌ Aucun onglet DeepSeek trouvé.")
            print(f"   Ouvre {DEEPSEEK_URL} dans Chrome et réessaie.")
            # Lister les onglets ouverts pour aider
            print("\n📋 Onglets ouverts :")
            for context in browser.contexts:
                for p_page in context.pages:
                    print(f"   - {p_page.url}")
            return

        print(f"✅ Onglet DeepSeek trouvé : {page.url}")
        print("⏳ Extraction des messages...")

        messages = extraire_messages(page)

        if not messages:
            print("⚠️  Aucun message extrait. La structure HTML a peut-être changé.")
            return

        print(f"✅ {len(messages)} message(s) extrait(s).")

        contenu = formater_md(args.session, messages)
        chemin = nom_fichier(args.session)
        chemin.write_text(contenu, encoding="utf-8")

        print(f"✅ Sauvegardé : {chemin}")
        print(f"\n💡 Lance maintenant ton script de commit/push habituel.")


if __name__ == "__main__":
    main()
