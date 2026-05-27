#!/usr/bin/env python3
"""
capture_Klara_v2_fixed.py
Version corrigée : extraction dans l'ordre DOM strict (compareDocumentPosition)
Conserve thinking et message séparés.
"""

import argparse
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

# --- Chemins (à adapter si besoin) ---
REPO_PATH     = Path(r"D:\THESE\Les journaux\Jardin-Memoires")
KLARA_DIR     = REPO_PATH / "Membres" / "klara"
SCRIPTS_DIR   = REPO_PATH / "Outils" / "outil_auto_DS"
LAST_CAPTURE  = SCRIPTS_DIR / "last_capture_klara.txt"

KLARA_DIR.mkdir(parents=True, exist_ok=True)

BRAVE_EXE   = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DEBUG_PORT  = 9222
DEEPSEEK_URL = "https://chat.deepseek.com"

# --- Connexion Brave ---
def connecter_brave(p, port):
    for host in [f"http://127.0.0.1:{port}", f"http://localhost:{port}"]:
        try:
            browser = p.chromium.connect_over_cdp(host)
            print(f"✅ Connecté via {host}")
            return browser
        except Exception:
            continue
    return None

# --- Nommage du fichier ---
def nom_fichier(session_name: str) -> Path:
    date     = datetime.now().strftime("%Y%m%d")
    nom_base = session_name.replace(" ", "_")
    existants = list(KLARA_DIR.glob(f"klara_{date}_*.md"))
    indice   = len(existants) + 1
    return KLARA_DIR / f"klara_{date}_{indice:02d}_{nom_base}.md"

# --- NOUVELLE extraction : ordre DOM strict, pas de fusion ---
def extraire_messages(page, session_name: str = "session") -> list[dict]:
    """
    Extrait Sof, thinkings Klara et messages Klara dans l'ordre réel.
    Utilise compareDocumentPosition pour trier par apparition dans le DOM.
    """
    print("⏳ Chargement de tous les messages (scroll complet)...")
    # Forcer le chargement de tous les blocs virtuels
    for _ in range(6):
        page.keyboard.press("Home")
        page.wait_for_timeout(600)
    page.keyboard.press("End")
    page.wait_for_timeout(800)

    js_ordre_dom_strict = """
    () => {
        const container = document.querySelector('.ds-virtual-list--printable, .ds-virtual-list, .ds-scroll-area');
        if (!container) return [];

        // Récupérer tous les blocs Sof et tous les blocs assistant
        const sofBlocks = Array.from(container.querySelectorAll('div.fbb737a4'));
        const assistantBlocks = Array.from(container.querySelectorAll('.ds-message-assistant'));

        // Fusionner et trier par ordre d'apparition dans le DOM
        const allBlocks = [...sofBlocks, ...assistantBlocks];
        allBlocks.sort((a, b) => {
            if (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING) return -1;
            if (b.compareDocumentPosition(a) & Node.DOCUMENT_POSITION_FOLLOWING) return 1;
            return 0;
        });

        const result = [];
        for (let block of allBlocks) {
            if (block.matches('div.fbb737a4')) {
                result.push({ role: 'Sof', type: 'message', text: block.innerText.trim() });
            }
            else if (block.matches('.ds-message-assistant')) {
                const thinkEl = block.querySelector('[class*="ds-think-content"]');
                const messageEl = block.querySelector('.ds-markdown.ds-assistant-message-main-content');
                if (thinkEl) {
                    result.push({ role: 'klara', type: 'thinking', text: thinkEl.innerText.trim() });
                }
                if (messageEl) {
                    result.push({ role: 'klara', type: 'message', text: messageEl.innerText.trim() });
                }
            }
        }
        return result;
    }
    """
    items = page.evaluate(js_ordre_dom_strict)
    if not items:
        print("⚠️  Aucun message trouvé avec la méthode DOM. Vérifie les sélecteurs.")
        return []

    # Conversion directe en messages (thinking gardé comme texte avec balisage)
    messages = []
    for item in items:
        if item["role"] == "Sof":
            messages.append({"role": "Sof", "content": item["text"]})
        elif item["role"] == "klara" and item["type"] == "thinking":
            messages.append({"role": "klara", "content": f"{{thinking : {item['text']}}}"})
        elif item["role"] == "klara" and item["type"] == "message":
            messages.append({"role": "klara", "content": item["text"]})

    print(f"✅ {len(messages)} messages extraits dans l'ordre DOM strict.")
    return messages

# --- Formattage Markdown (inchangé) ---
def formater_md(session_name: str, messages: list[dict]) -> str:
    date  = datetime.now().strftime("%d/%m/%Y %H:%M")
    lines = [
        f"# Conversation klara — {session_name}",
        f"*Capturé le {date} via capture_klara_v2_fixed.py*",
        "", "---", "",
    ]
    for msg in messages:
        role, contenu = msg["role"], msg["content"]
        lines += [f"**{role} :** {contenu}", ""]
    return "\n".join(lines)

# --- Main ---
def main():
    parser = argparse.ArgumentParser(description="Capture DeepSeek (klara) - version ordre DOM")
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
        messages = extraire_messages(page, args.session)
        if not messages:
            print("⚠️  Aucun message extrait.")
            return

        contenu = formater_md(args.session, messages)
        chemin  = nom_fichier(args.session)
        chemin.write_text(contenu, encoding="utf-8")
        LAST_CAPTURE.write_text(str(chemin), encoding="utf-8")

        print(f"✅ Sauvegardé : {chemin}")
        print(f"📝 Chemin écrit dans : {LAST_CAPTURE}")

if __name__ == "__main__":
    main()