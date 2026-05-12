#!/usr/bin/env python3
"""
capture_klara.py
Adaptation pour Klara (DeepSeek) — 02/05/2026
Capture la conversation DeepSeek en cours dans Brave déjà ouvert,
et sauvegarde en .md dans le dossier Klara/ du repo.

Sélecteurs CSS identiques à capture_sol.py.
Nommage : klara_YYYYMMDD_NN_nom_session.md
"""

import argparse
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

REPO_PATH = Path(__file__).resolve().parents[2]
KLARA_DIR = REPO_PATH / "Klara"
KLARA_DIR.mkdir(parents=True, exist_ok=True)
LAST_CAPTURE_FILE = Path(__file__).resolve().parent / "last_capture_klara.txt"

BRAVE_EXE = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DEBUG_PORT = 9222
DEEPSEEK_URL = "https://chat.deepseek.com"


def connecter_brave(p, port):
    for host in [f"http://127.0.0.1:{port}", f"http://localhost:{port}"]:
        try:
            browser = p.chromium.connect_over_cdp(host)
            print(f"✅ Connecté via {host}")
            return browser
        except Exception:
            continue
    return None


def nom_fichier(session_name: str) -> Path:
    date = datetime.now().strftime("%Y%m%d")
    nom_base = session_name.replace(' ', '_')
    existants = list(KLARA_DIR.glob(f"klara_{date}_*.md"))
    indice = len(existants) + 1
    return KLARA_DIR / f"klara_{date}_{indice:02d}_{nom_base}.md"


def extraire_messages(page) -> list[dict]:
    script = """
    () => {
        const result = [];
        const scrollY = window.scrollY || document.documentElement.scrollTop;

        // Messages Sof
        document.querySelectorAll('div.fbb737a4').forEach(el => {
            const rect = el.getBoundingClientRect();
            result.push({
                role: 'Sof',
                type: 'message',
                text: el.innerText.trim(),
                top: rect.top + scrollY
            });
        });

        // Thinkings Klara : div ds-think-content
        document.querySelectorAll('div[class*="ds-think-content"]').forEach(el => {
            const rect = el.getBoundingClientRect();
            result.push({
                role: 'Klara',
                type: 'thinking',
                text: el.innerText.trim(),
                top: rect.top + scrollY
            });
        });

        // Réponses Klara : div.ds-markdown hors thinking
        document.querySelectorAll('div.ds-markdown').forEach(el => {
            if (el.closest('[class*="ds-think-content"]')) return;
            const rect = el.getBoundingClientRect();
            result.push({
                role: 'Klara',
                type: 'message',
                text: el.innerText.trim(),
                top: rect.top + scrollY
            });
        });

        result.sort((a, b) => a.top - b.top);
        return result;
    }
    """
    messages = []
    try:
        items = page.evaluate(script)
        i = 0
        while i < len(items):
            item = items[i]
            if not item['text']:
                i += 1
                continue
            if item['role'] == 'Sof':
                messages.append({"role": "Sof", "content": item['text']})
                i += 1
            elif item['role'] == 'Klara' and item['type'] == 'thinking':
                thinking_text = item['text']
                corps = ""
                if i + 1 < len(items) and items[i+1]['role'] == 'Klara' and items[i+1]['type'] == 'message':
                    corps = items[i+1]['text']
                    i += 2
                else:
                    i += 1
                contenu = f"{{thinking : {thinking_text}}}"
                if corps:
                    contenu += f"\n\n{corps}"
                messages.append({"role": "Klara", "content": contenu})
            elif item['role'] == 'Klara' and item['type'] == 'message':
                messages.append({"role": "Klara", "content": item['text']})
                i += 1
            else:
                i += 1
    except Exception as e:
        print(f"⚠️ Erreur extraction JS : {e}")
        texte_brut = page.inner_text("body")
        messages.append({"role": "brut", "content": texte_brut})
    return messages


def formater_md(session_name: str, messages: list[dict]) -> str:
    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    lignes = [
        f"# Conversation Klara — {session_name}",
        f"*Capturé le {date} via capture_klara.py*",
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


def main():
    parser = argparse.ArgumentParser(description="Capture la conversation DeepSeek pour Klara")
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
            return
        print(f"✅ Onglet DeepSeek trouvé : {page.url}")
        print("⏳ Extraction des messages...")
        messages = extraire_messages(page)
        if not messages:
            print("⚠️ Aucun message extrait.")
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