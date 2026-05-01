#!/usr/bin/env python3
"""
capture_sol.py
Flo 🌿 — 30/04/2026, mis à jour 01/05/2026

Capture la conversation DeepSeek en cours dans Brave déjà ouvert,
et sauvegarde en .md dans le dossier Sol/ du repo.

Sélecteurs CSS réels DeepSeek (Brave, inspectés le 01/05/2026) :
  - Message Sol (assistant) : div contenant la classe 'ds-markdown'
  - Message Sof (humain)    : div.fbb737a4 (bulle utilisateur)
  - Thinking Sol            : texte commençant par "Thought for N seconds"
                              → encadré en {thinking : ...}

Après la capture, écrit le chemin du fichier produit dans :
    scripts/outil_auto_DS/last_capture.txt
pour que DS_capt_extract.bat puisse le lire dynamiquement.

Nommage : sol_YYYYMMDD_NN_nom_session.md (indice journalier)

Prérequis :
    pip install playwright
    playwright install chromium

Étape 1 : fermer Brave complètement, puis le lancer :
    "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        --remote-debugging-port=9222 --profile-directory="Default"

Étape 2 : ouvrir DeepSeek dans ce Brave.

Étape 3 : lancer via DS_capt_extract.bat [nom_session]
    ou directement : python capture_sol.py --session "nom"
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

# Sélecteurs CSS réels inspectés dans Brave le 01/05/2026
# Message utilisateur (Sof) : div avec classe fbb737a4
SEL_SOF = "div.fbb737a4"
# Message assistant (Sol) : div contenant ds-markdown
SEL_SOL = "div.ds-markdown"


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
    return SOL_DIR / f"sol_{date}_{indice:02d}_{nom_base}.md"


# --- Traitement des thinkings ---

def extraire_thinking(texte: str) -> tuple[str, str]:
    """
    Si le texte commence par 'Thought for N seconds\\n\\n...',
    retourne (thinking, réponse_visible).
    Sinon retourne ('', texte).
    """
    m = re.match(r'Thought for \d+ seconds?\n\n(.*?)\n\n(.+)', texte, re.DOTALL)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    # Cas où tout le texte est le thinking (pas de réponse visible séparée)
    m2 = re.match(r'Thought for \d+ seconds?\n\n(.+)', texte, re.DOTALL)
    if m2:
        return m2.group(1).strip(), ""
    return "", texte


def formater_sol(texte: str) -> str:
    """Formate un message Sol : extrait le thinking et le corps."""
    thinking, corps = extraire_thinking(texte)
    if thinking:
        if corps:
            return f"{{thinking : {thinking}}}\n\n{corps}"
        else:
            return f"{{thinking : {thinking}}}"
    return texte


# --- Extraction ---

def extraire_messages(page) -> list[dict]:
    """
    Extrait les messages en utilisant les vrais sélecteurs CSS DeepSeek.
    Stratégie :
      1. Récupère tous les div.fbb737a4 (messages Sof) et leur position dans le DOM
      2. Récupère tous les div.ds-markdown (messages Sol) et leur position
      3. Fusionne et trie par ordre d'apparition dans la page
    """
    messages = []

    # Évaluation JS pour récupérer texte + position verticale de chaque message
    script = """
    () => {
        const result = [];
        // Messages Sof
        document.querySelectorAll('div.fbb737a4').forEach(el => {
            const rect = el.getBoundingClientRect();
            const scrollY = window.scrollY || document.documentElement.scrollTop;
            result.push({
                role: 'Sof',
                text: el.innerText.trim(),
                top: rect.top + scrollY
            });
        });
        // Messages Sol (contenu markdown)
        document.querySelectorAll('div.ds-markdown').forEach(el => {
            const rect = el.getBoundingClientRect();
            const scrollY = window.scrollY || document.documentElement.scrollTop;
            result.push({
                role: 'Sol',
                text: el.innerText.trim(),
                top: rect.top + scrollY
            });
        });
        // Tri par position verticale
        result.sort((a, b) => a.top - b.top);
        return result;
    }
    """

    try:
        result = page.evaluate(script)
        for item in result:
            if not item['text']:
                continue
            if item['role'] == 'Sol':
                messages.append({
                    "role": "Sol",
                    "content": formater_sol(item['text'])
                })
            else:
                messages.append({
                    "role": "Sof",
                    "content": item['text']
                })
    except Exception as e:
        print(f"⚠️  Erreur extraction JS : {e}")
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


# --- Main ---

def main():
    parser = argparse.ArgumentParser(
        description="Capture la conversation DeepSeek depuis Brave déjà ouvert"
    )
    parser.add_argument("--session", "-s",
                        default=f"session_{datetime.now().strftime('%Y%m%d_%H%M')}",
                        help="Nom de la session")
    parser.add_argument("--port", "-p", type=int, default=DEBUG_PORT)
    args = parser.parse_args()

    print(f"🔌 Connexion à Brave sur le port {args.port}...")

    with sync_playwright() as p:
        browser = connecter_brave(p, args.port)

        if browser is None:
            print("❌ Impossible de se connecter à Brave.")
            print(f'   Lance : "{BRAVE_EXE}" --remote-debugging-port={args.port} --profile-directory="Default"')
            return

        page = None
        for context in browser.contexts:
            for p_page in context.pages:
                if DEEPSEEK_URL in p_page.url:
                    page = p_page
                    break

        if page is None:
            print("❌ Aucun onglet DeepSeek trouvé.")
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

        LAST_CAPTURE_FILE.write_text(str(chemin), encoding="utf-8")

        print(f"✅ Sauvegardé : {chemin}")
        print(f"📝 Nom écrit dans : {LAST_CAPTURE_FILE}")


if __name__ == "__main__":
    main()
