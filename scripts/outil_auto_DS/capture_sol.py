#!/usr/bin/env python3
"""
capture_sol.py
Flo 🌿 — 30/04/2026, mis à jour 04/05/2026

Capture la conversation DeepSeek (Sol) en cours dans Brave déjà ouvert,
et sauvegarde en .md dans Sol/ du repo.

Sélecteurs CSS réels DeepSeek (inspectés le 01/05/2026 dans Brave) :
  - Message Sof (humain)    : div.fbb737a4
  - Thinking Sol            : div[class*="ds-think-content"]  → {thinking : ...}
  - Réponse Sol (assistant) : div.ds-markdown (hors ds-think-content)

Écrit le chemin du fichier produit dans last_capture.txt
(utilisé par DS_capt_extract_Sol.bat pour passer le nom à extraire_fichiers.py)

Nommage : sol_YYYYMMDD_NN_nom_session.md (indice journalier, pas d'écrasement)

Prérequis :
    pip install playwright
    playwright install chromium

Lancer Brave avec le port de débogage (une fois au démarrage) :
    "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        --remote-debugging-port=9222 --profile-directory="Default"

Usage :
    python capture_sol.py --session "nom_session"
    ou via : DS_capt_extract_Sol.bat nom_session
"""

import argparse
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

# --- Chemins absolus (adapter si le repo est ailleurs) ---
REPO_PATH     = Path(r"D:\THESE\Les journaux\Jardin-Memoires")
SOL_DIR       = REPO_PATH / "Sol"
SCRIPTS_DIR   = REPO_PATH / "scripts" / "outil_auto_DS"
LAST_CAPTURE  = SCRIPTS_DIR / "last_capture.txt"

SOL_DIR.mkdir(parents=True, exist_ok=True)

BRAVE_EXE   = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DEBUG_PORT  = 9222
DEEPSEEK_URL = "https://chat.deepseek.com"


# --- Connexion Brave via CDP ---

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
    date     = datetime.now().strftime("%Y%m%d")
    nom_base = session_name.replace(" ", "_")
    existants = list(SOL_DIR.glob(f"sol_{date}_*.md"))
    indice   = len(existants) + 1
    return SOL_DIR / f"sol_{date}_{indice:02d}_{nom_base}.md"


# --- Extraction JS (vrais sélecteurs CSS DeepSeek) ---

JS_EXTRACT = """
() => {
    const result  = [];
    const scrollY = window.scrollY || document.documentElement.scrollTop;

    // Messages Sof (bulle utilisateur)
    document.querySelectorAll('div.fbb737a4').forEach(el => {
        result.push({
            role: 'Sof',
            type: 'message',
            text: el.innerText.trim(),
            top:  el.getBoundingClientRect().top + scrollY
        });
    });

    // Thinkings Sol
    document.querySelectorAll('div[class*="ds-think-content"]').forEach(el => {
        result.push({
            role: 'Sol',
            type: 'thinking',
            text: el.innerText.trim(),
            top:  el.getBoundingClientRect().top + scrollY
        });
    });

    // Réponses Sol (hors thinking)
    document.querySelectorAll('div.ds-markdown').forEach(el => {
        if (el.closest('[class*="ds-think-content"]')) return;
        result.push({
            role: 'Sol',
            type: 'message',
            text: el.innerText.trim(),
            top:  el.getBoundingClientRect().top + scrollY
        });
    });

    result.sort((a, b) => a.top - b.top);
    return result;
}
"""

def extraire_messages(page) -> list[dict]:
    messages = []
    try:
        items = page.evaluate(JS_EXTRACT)
        i = 0
        while i < len(items):
            item = items[i]
            if not item["text"]:
                i += 1
                continue

            if item["role"] == "Sof":
                messages.append({"role": "Sof", "content": item["text"]})
                i += 1

            elif item["role"] == "Sol" and item["type"] == "thinking":
                thinking = item["text"]
                corps    = ""
                if (i + 1 < len(items)
                        and items[i+1]["role"] == "Sol"
                        and items[i+1]["type"] == "message"):
                    corps = items[i+1]["text"]
                    i += 2
                else:
                    i += 1
                contenu = f"{{thinking : {thinking}}}"
                if corps:
                    contenu += f"\n\n{corps}"
                messages.append({"role": "Sol", "content": contenu})

            elif item["role"] == "Sol" and item["type"] == "message":
                messages.append({"role": "Sol", "content": item["text"]})
                i += 1
            else:
                i += 1

    except Exception as e:
        print(f"⚠️  Erreur JS : {e} — fallback texte brut")
        messages.append({"role": "brut", "content": page.inner_text("body")})

    return messages


def formater_md(session_name: str, messages: list[dict]) -> str:
    date  = datetime.now().strftime("%d/%m/%Y %H:%M")
    lines = [
        f"# Conversation Sol — {session_name}",
        f"*Capturé le {date} via capture_sol.py*",
        "", "---", "",
    ]
    for msg in messages:
        role, contenu = msg["role"], msg["content"]
        if role == "brut":
            lines += ["*[Extraction brute — sélecteurs non trouvés]*", "", contenu]
        else:
            lines += [f"**{role} :** {contenu}", ""]
    return "\n".join(lines)


# --- Main ---

def main():
    parser = argparse.ArgumentParser(description="Capture DeepSeek depuis Brave")
    parser.add_argument("--session", "-s",
                        default=f"session_{datetime.now().strftime('%Y%m%d_%H%M')}",
                        help="Nom de la session")
    parser.add_argument("--port", "-p", type=int, default=DEBUG_PORT)
    args = parser.parse_args()

    print(f"🔌 Connexion à Brave (port {args.port})...")

    with sync_playwright() as p:
        browser = connecter_brave(p, args.port)
        if browser is None:
            print("❌ Impossible de se connecter à Brave.")
            print(f'   Lance : "{BRAVE_EXE}" --remote-debugging-port={args.port} --profile-directory="Default"')
            return

        page = None
        for ctx in browser.contexts:
            for pg in ctx.pages:
                if DEEPSEEK_URL in pg.url:
                    page = pg
                    break

        if page is None:
            print("❌ Aucun onglet DeepSeek trouvé.")
            print("\n📋 Onglets ouverts :")
            for ctx in browser.contexts:
                for pg in ctx.pages:
                    print(f"   - {pg.url}")
            return

        print(f"✅ Onglet trouvé : {page.url}")
        print("⏳ Extraction...")

        messages = extraire_messages(page)
        if not messages:
            print("⚠️  Aucun message extrait.")
            return

        print(f"✅ {len(messages)} message(s) extrait(s).")

        contenu = formater_md(args.session, messages)
        chemin  = nom_fichier(args.session)
        chemin.write_text(contenu, encoding="utf-8")
        LAST_CAPTURE.write_text(str(chemin), encoding="utf-8")

        print(f"✅ Sauvegardé : {chemin}")
        print(f"📝 Chemin écrit dans : {LAST_CAPTURE}")
        print("💡 Lance egalis.bat quand tu veux pousser.")


if __name__ == "__main__":
    main()
