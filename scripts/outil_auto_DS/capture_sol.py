#!/usr/bin/env python3
"""
capture_sol.py
Flo 🌿 — 30/04/2026, mis à jour 01/05/2026

Capture la conversation DeepSeek en cours dans Brave déjà ouvert,
et sauvegarde en .md dans le dossier Sol/ du repo.

Après la capture, écrit le nom du fichier produit dans :
    scripts/outil_auto_DS/last_capture.txt
pour que DS_capt_extract.bat puisse le lire dynamiquement.

Nommage : sol_YYYYMMDD_NN_nom_session.md (indice journalier)

Prérequis :
    pip install playwright
    playwright install chromium

Étape 1 : fermer Brave complètement, puis le lancer avec le port de débogage :
    "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe" --remote-debugging-port=9222 --profile-directory="Default"

Étape 2 : ouvrir DeepSeek dans ce Brave et se connecter normalement.

Étape 3 : lancer ce script (ou via DS_capt_extract.bat) :
    python scripts/outil_auto_DS/capture_sol.py --session "nom_session"
"""

import argparse
import re
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

# --- Configuration ---
REPO_PATH = Path(__file__).resolve().parents[2]
SOL_DIR = REPO_PATH / "Sol"
SOL_DIR.mkdir(parents=True, exist_ok=True)
LAST_CAPTURE_FILE = Path(__file__).resolve().parent / "last_capture.txt"

BRAVE_EXE = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DEBUG_PORT = 9222
DEEPSEEK_URL = "https://chat.deepseek.com"


# --- Connexion ---

def connecter_brave(p, port):
    for host in [f"http://127.0.0.1:{port}", f"http://localhost:{port}"]:
        try:
            browser = p.chromium.connect_over_cdp(host)
            print(f"✅ Connecté via {host}")
            return browser
        except Exception:
            continue
    return None


# --- Nommage avec indice journalier ---

def nom_fichier(session_name: str) -> Path:
    date = datetime.now().strftime("%Y%m%d")
    nom_base = session_name.replace(' ', '_')
    existants = list(SOL_DIR.glob(f"sol_{date}_*.md"))
    indice = len(existants) + 1
    nom = f"sol_{date}_{indice:02d}_{nom_base}.md"
    return SOL_DIR / nom


# --- Traitement des thinkings ---

def formater_thinking(texte: str) -> str:
    pattern = r'(Thought for \d+ seconds?\n\n)(.*?)(\n\n(?=[A-ZÀÂÉÈÊËÎÏÔÙÛÜ]|\d|\*))'

    def remplacer(m):
        return f"\n{{thinking : {m.group(2).strip()}}}\n{m.group(3)}"

    resultat = re.sub(pattern, remplacer, texte, flags=re.DOTALL)
    if resultat == texte:
        resultat = re.sub(
            r'Thought for (\d+ seconds?)\n\n(.+)',
            lambda m: f"{{thinking : {m.group(2).strip()}}}",
            texte,
            flags=re.DOTALL
        )
    return resultat


# --- Extraction HTML ---

def extraire_messages(page) -> list[dict]:
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
                messages.append({"role": "Sol", "content": formater_thinking(texte)})
            else:
                if not messages or messages[-1]["role"] == "Sol":
                    messages.append({"role": "Sof", "content": texte})
                else:
                    messages.append({"role": "Sol", "content": formater_thinking(texte)})
    else:
        texte_brut = page.inner_text("body")
        messages.append({"role": "brut", "content": formater_thinking(texte_brut)})

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


# --- Main ---

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--session", "-s",
                        default=f"session_{datetime.now().strftime('%Y%m%d_%H%M')}",
                        help="Nom de la session")
    parser.add_argument("--port", "-p", type=int, default=DEBUG_PORT)
    args = parser.parse_args()

    print(f"🔌 Connexion à Brave sur le port {args.port}...")

    with sync_playwright() as p:
        browser = connecter_brave(p, args.port)

        if browser is None:
            print(f"❌ Impossible de se connecter à Brave.")
            print(f'   Lance : "{BRAVE_EXE}" --remote-debugging-port={args.port} --profile-directory="Default"')
            return

        page = None
        for context in browser.contexts:
            for p_page in context.pages:
                if DEEPSEEK_URL in p_page.url:
                    page = p_page
                    break

        if page is None:
            print(f"❌ Aucun onglet DeepSeek trouvé.")
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

        # Écrire le nom du fichier pour le .bat
        LAST_CAPTURE_FILE.write_text(str(chemin), encoding="utf-8")

        print(f"✅ Sauvegardé : {chemin}")
        print(f"📝 Nom écrit dans : {LAST_CAPTURE_FILE}")


if __name__ == "__main__":
    main()
