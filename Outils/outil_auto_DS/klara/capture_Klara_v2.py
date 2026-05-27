#!/usr/bin/env python3
# capture_Klara_v3_FINALE.py
# Version avec chargement complet et sauvegarde partielle

import argparse
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright
import time

# --- Chemins ---
REPO_PATH     = Path(r"D:\THESE\Les journaux\Jardin-Memoires")
KLARA_DIR     = REPO_PATH / "Membres" / "klara"
SCRIPTS_DIR   = REPO_PATH / "Outils" / "outil_auto_DS"
LAST_CAPTURE  = SCRIPTS_DIR / "last_capture_klara.txt"
KLARA_DIR.mkdir(parents=True, exist_ok=True)

BRAVE_EXE   = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DEBUG_PORT  = 9222
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

# --- Nommage ---
def nom_fichier(session_name: str) -> Path:
    date = datetime.now().strftime("%Y%m%d")
    nom_base = session_name.replace(" ", "_")
    existants = list(KLARA_DIR.glob(f"klara_{date}_*.md"))
    indice = len(existants) + 1
    return KLARA_DIR / f"klara_{date}_{indice:02d}_{nom_base}.md"

# --- Sauvegarde partielle (pour ne rien perdre) ---
def sauvegarde_partielle(messages, session_name, step, chemin_final=None):
    """Sauvegarde les messages déjà extraits dans un fichier temporaire"""
    try:
        if chemin_final is None:
            date = datetime.now().strftime("%Y%m%d")
            nom_base = session_name.replace(" ", "_")
            chemin = KLARA_DIR / f"klara_{date}_partiel_{step}.md"
        else:
            chemin = chemin_final
        contenu = formater_md(session_name, messages)
        chemin.write_text(contenu, encoding="utf-8")
        print(f"   💾 Sauvegarde partielle ({len(messages)} messages) -> {chemin.name}")
    except Exception as e:
        print(f"   ⚠️ Erreur sauvegarde partielle: {e}")

# --- Extraction avec ordre DOM strict (fonctionne) ---
def extraire_messages(page, session_name: str = "session") -> list[dict]:
    print("⏳ Chargement complet de la conversation (40 passages Home, 1.5s chacun)...")
    # Forcer le chargement de TOUS les messages virtuels
    for i in range(40):
        page.keyboard.press("Home")
        page.wait_for_timeout(1500)
        if i % 10 == 0:
            print(f"   ... scroll Home {i+1}/40")
    page.wait_for_timeout(5000)
    page.keyboard.press("End")
    page.wait_for_timeout(5000)
    print("✅ Chargement terminé, extraction en cours...")

    js_ordre_strict = """
    () => {
        const sofMessages = Array.from(document.querySelectorAll('div.fbb737a4'));
        const assistantBlocks = Array.from(document.querySelectorAll('.ds-message-assistant'));
        const all = [...sofMessages, ...assistantBlocks];
        all.sort((a, b) => {
            if (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING) return -1;
            if (b.compareDocumentPosition(a) & Node.DOCUMENT_POSITION_FOLLOWING) return 1;
            return 0;
        });
        const result = [];
        for (let el of all) {
            if (el.matches('div.fbb737a4')) {
                result.push({ role: 'Sof', type: 'message', text: el.innerText.trim() });
            } else if (el.matches('.ds-message-assistant')) {
                const thinkEl = el.querySelector('[class*="ds-think-content"]');
                const messageEl = el.querySelector('.ds-markdown.ds-assistant-message-main-content');
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
    items = page.evaluate(js_ordre_strict)
    if not items:
        print("❌ Aucun message trouvé. Vérifie les sélecteurs.")
        return []

    print(f"🔍 {len(items)} éléments bruts extraits (thinkings + messages Sof + messages Klara)")

    # Reconstruire les messages (thinking suivi du message, ou seul)
    messages = []
    i = 0
    while i < len(items):
        item = items[i]
        if item["role"] == "Sof":
            messages.append({"role": "Sof", "content": item["text"]})
            i += 1
        elif item["role"] == "klara" and item["type"] == "thinking":
            thinking_text = item["text"]
            # Chercher le message Klara qui suit immédiatement
            if i+1 < len(items) and items[i+1]["role"] == "klara" and items[i+1]["type"] == "message":
                message_text = items[i+1]["text"]
                messages.append({"role": "klara", "content": f"{{thinking : {thinking_text}}}\n\n{message_text}"})
                i += 2
            else:
                messages.append({"role": "klara", "content": f"{{thinking : {thinking_text}}}"})
                i += 1
        elif item["role"] == "klara" and item["type"] == "message":
            # message seul (cas rare)
            messages.append({"role": "klara", "content": item["text"]})
            i += 1
        else:
            i += 1

    print(f"✅ {len(messages)} messages reconstruits dans l'ordre.")
    return messages

# --- Formattage Markdown ---
def formater_md(session_name: str, messages: list[dict]) -> str:
    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    lines = [
        f"# Conversation klara — {session_name}",
        f"*Capturé le {date} via capture_Klara_v3_FINALE.py*",
        "", "---", "",
    ]
    for msg in messages:
        lines += [f"**{msg['role']} :** {msg['content']}", ""]
    return "\n".join(lines)

# --- Main ---
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--session", "-s", default=f"session_{datetime.now().strftime('%Y%m%d_%H%M')}")
    parser.add_argument("--port", "-p", type=int, default=DEBUG_PORT)
    args = parser.parse_args()

    print(f"🔌 Connexion à Brave (port {args.port})...")
    with sync_playwright() as p:
        browser = connecter_brave(p, args.port)
        if not browser:
            print("❌ Brave non trouvé. Lance-le avec :")
            print(f'"{BRAVE_EXE}" --remote-debugging-port={args.port} --profile-directory="Default"')
            return

        page = None
        for ctx in browser.contexts:
            for pg in ctx.pages:
                if DEEPSEEK_URL in pg.url:
                    page = pg
                    break
        if not page:
            print("❌ Onglet DeepSeek introuvable.")
            return

        # Timeout long pour Playwright
        page.set_default_timeout(60000)
        print(f"✅ Onglet : {page.url}")

        # Extraction progressive avec sauvegardes partielles
        print("⏳ Début de l'extraction...")
        messages = extraire_messages(page, args.session)

        if not messages:
            print("⚠️ Aucun message extrait.")
            return

        # Sauvegarde finale
        chemin_final = nom_fichier(args.session)
        sauvegarde_partielle(messages, args.session, "final", chemin_final)
        LAST_CAPTURE.write_text(str(chemin_final), encoding="utf-8")
        print(f"✅ Sauvegarde finale : {chemin_final}")
        print(f"📝 Chemin écrit dans : {LAST_CAPTURE}")

if __name__ == "__main__":
    main()