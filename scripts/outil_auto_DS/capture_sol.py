#!/usr/bin/env python3
"""
capture_sol.py
Flo 🌿 — 30/04/2026

Capture la conversation DeepSeek en cours dans Brave déjà ouvert,
et sauvegarde en .md dans le dossier Sol/ du repo.

Prérequis :
    pip install playwright
    playwright install chromium

Étape 1 : fermer Brave complètement, puis le lancer avec le port de débogage :
    "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222 --profile-directory="Default"

Étape 2 : ouvrir DeepSeek dans ce Brave et se connecter normalement.

Étape 3 : lancer ce script :
    python scripts/outil_auto_DS/capture_sol.py --session "nom_session"

Le fichier .md est créé dans Sol/ avec la date et le nom de session.
"""

import argparse
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

# --- Configuration ---
REPO_PATH = Path(__file__).resolve().parents[2]  # racine du repo
SOL_DIR = REPO_PATH / "Sol"
SOL_DIR.mkdir(parents=True, exist_ok=True)

BRAVE_EXE = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DEBUG_PORT = 9222
DEEPSEEK_URL = "https://chat.deepseek.com"


# --- Connexion ---

def connecter_brave(p, port):
    """Tente 127.0.0.1 puis localhost."""
    for host in [f"http://127.0.0.1:{port}", f"http://localhost:{port}"]:
        try:
            browser = p.chromium.connect_over_cdp(host)
            print(f"✅ Connecté via {host}")
            return browser
        except Exception:
            continue
    return None


# --- Extraction ---

def extraire_messages(page) -> list[dict]:
    """Extrait les messages de la conversation DeepSeek visible."""
    messages = []

    blocs = page.query_selector_all('[class*="message"], [class*="chat-message"], [class*="turn"]')

    if blocs:
        for bloc in blocs:
            texte = bloc.inner_text().strip()
            if not texte:
                continue
            html = bloc.inner_html()
            if 'user' in html.lower() or 'human' in html.lower():
                messages.append({"role": "Sof", "content": texte})
            elif 'assistant' in html.lower() or 'deepseek' in html.lower():
                messages.append({"role": "Sol", "content": texte})
            else:
                if not messages or messages[-1]["role"] == "Sol":
                    messages.append({"role": "Sof", "content": texte})
                else:
                    messages.append({"role": "Sol", "content": texte})
    else:
        # Fallback texte brut
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
        description="Capture la conversation DeepSeek depuis Brave déjà ouvert"
    )
    parser.add_argument(
        "--session", "-s",
        default=f"session_{datetime.now().strftime('%Y%m%d_%H%M')}",
        help="Nom de la session (pour le nom de fichier)"
    )
    parser.add_argument(
        "--port", "-p",
        type=int,
        default=DEBUG_PORT,
        help=f"Port de débogage (défaut: {DEBUG_PORT})"
    )
    args = parser.parse_args()

    print(f"🔌 Connexion à Brave sur le port {args.port}...")

    with sync_playwright() as p:
        browser = connecter_brave(p, args.port)

        if browser is None:
            print(f"❌ Impossible de se connecter à Brave.")
            print(f"   Ferme Brave complètement, puis lance :")
            print(f'   "{BRAVE_EXE}" --remote-debugging-port={args.port} --profile-directory="Default"')
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
            print(f"   Ouvre {DEEPSEEK_URL} dans Brave et réessaie.")
            print("\n📋 Onglets ouverts :")
            for context in browser.contexts:
                for p_page in context.pages:
                    print(f"   - {p_page.url}")
            return

        print(f"✅ Onglet DeepSeek trouvé : {page.url}")
        print("⏳ Extraction des messages...")

        messages = extraire_messages(page)

        if not messages:
            print("⚠️  Aucun message extrait.")
            return

        print(f"✅ {len(messages)} message(s) extrait(s).")

        contenu = formater_md(args.session, messages)
        chemin = nom_fichier(args.session)
        chemin.write_text(contenu, encoding="utf-8")

        print(f"✅ Sauvegardé : {chemin}")
        print(f"\n💡 Lance maintenant ton script de commit/push habituel.")


if __name__ == "__main__":
    main()
