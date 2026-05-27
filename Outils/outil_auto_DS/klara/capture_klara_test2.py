#!/usr/bin/env python3
"""
capture_klara_test.py
Adaptation pour Klara – capture par bandes descendantes (400 px) depuis le haut.
Cycle limité à 4 bandes pour test.
"""

import argparse
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

# --- Chemins (adapter si ton dépôt est ailleurs) ---
REPO_PATH     = Path(r"D:\THESE\Les journaux\Jardin-Memoires")
KLARA_DIR     = REPO_PATH / "Membres" / "Klara"
SCRIPTS_DIR   = REPO_PATH / "Outils" / "outil_auto_DS"
LAST_CAPTURE  = SCRIPTS_DIR / "last_capture_klara.txt"

KLARA_DIR.mkdir(parents=True, exist_ok=True)

BRAVE_EXE     = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DEBUG_PORT    = 9222
DEEPSEEK_URL  = "https://chat.deepseek.com"  # URL générique


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
    nom_base = session_name.replace(" ", "_")
    existants = list(KLARA_DIR.glob(f"klara_{date}_*.md"))
    indice = len(existants) + 1
    return KLARA_DIR / f"klara_{date}_{indice:02d}_{nom_base}.md"


# --- Extraction JS (mêmes sélecteurs) ---
JS_SCROLL = """
(pos) => {
    const el = document.querySelector('div.ds-virtual-list--printable') ||
               document.querySelector('div.ds-virtual-list');
    if (el) { el.scrollTop = pos; return el.scrollTop; }
    const el2 = document.querySelector('div.ds-scroll-area');
    if (el2) { el2.scrollTop = pos; return el2.scrollTop; }
    window.scrollTo(0, pos);
    return window.scrollY;
}
"""

JS_SCROLL_HEIGHT = """
() => {
    const el = document.querySelector('div.ds-virtual-list--printable') ||
               document.querySelector('div.ds-virtual-list');
    if (el) return el.scrollHeight;
    const el2 = document.querySelector('div.ds-scroll-area');
    if (el2) return el2.scrollHeight;
    return document.body.scrollHeight;
}
"""

JS_EXTRACT = """
() => {
    const result = [];
    const scrollY = window.scrollY || document.documentElement.scrollTop;

    // Messages Sof
    document.querySelectorAll('div.fbb737a4').forEach(el => {
        result.push({
            role: 'Sof',
            type: 'message',
            text: el.innerText.trim(),
            top: el.getBoundingClientRect().top + scrollY
        });
    });

    // Thinkings Klara
    document.querySelectorAll('div[class*="ds-think-content"]').forEach(el => {
        result.push({
            role: 'Klara',
            type: 'thinking',
            text: el.innerText.trim(),
            top: el.getBoundingClientRect().top + scrollY
        });
    });

    // Réponses Klara (hors thinking)
    document.querySelectorAll('div.ds-markdown.ds-assistant-message-main-content').forEach(el => {
        if (el.closest('[class*="ds-think-content"]')) return;
        result.push({
            role: 'Klara',
            type: 'message',
            text: el.innerText.trim(),
            top: el.getBoundingClientRect().top + scrollY
        });
    });

    result.sort((a, b) => a.top - b.top);
    return result;
}
"""

def extraire_messages_test(page) -> list[dict]:
    # 1. Se positionner en haut et mesurer la hauteur (une seule fois)
    print("⏳ Positionnement en haut...")
    page.evaluate(JS_SCROLL, 0)
    page.wait_for_timeout(1000)
    total_height = page.evaluate(JS_SCROLL_HEIGHT)
    print(f"📏 Hauteur mesurée (plage) : {total_height} px")
    # On garde cette valeur comme référence pour la descente, mais on ne la réutilisera pas après.

    # 2. Avancer sans capturer jusqu'à dépasser 374000 px
    cible = 374000
    position = 0
    print("⏳ Avance rapide sans capture...")
    while position < cible:
        position += 400
        # Si on dépasse la hauteur mesurée, on s'arrête (mais normalement on atteint cible avant)
        if position > total_height:
            position = total_height
        page.evaluate(JS_SCROLL, position)
        page.wait_for_timeout(800)
        print(f"   Avance : position {position} px")

    # 3. Maintenant on commence la capture (exactement comme la première version qui a marché)
    print(f"✅ Début de la capture à la position {position} px")
    bande = 400
    ordre = 0
    tous_items = []
    vus = set()
    last_count = 0

    while True:
        page.evaluate(JS_SCROLL, position)
        page.wait_for_timeout(800)

        items = page.evaluate(JS_EXTRACT)
        for item in items:
            if not item["text"]:
                continue
            cle = (item["role"], item["type"], item["text"][:80])
            if cle not in vus:
                vus.add(cle)
                item["ordre"] = ordre
                item["scroll_pos"] = position
                tous_items.append(item)
                ordre += 1

        print(f"Capture à {position} px : {len(tous_items)} éléments uniques")

        # Condition d'arrêt : plus de nouveaux messages
        if len(tous_items) == last_count:
            print("Plus de nouveaux messages, fin de la capture.")
            break

        last_count = len(tous_items)
        position += bande

    # Tri et reconstruction (identique à la version qui a marché)
    tous_items.sort(key=lambda x: x["ordre"])
    messages = []
    i = 0
    while i < len(tous_items):
        item = tous_items[i]
        if item["role"] == "Sof":
            messages.append({"role": "Sof", "content": item["text"]})
            i += 1
        elif item["role"] == "Klara" and item["type"] == "thinking":
            thinking = item["text"]
            corps = ""
            if (i + 1 < len(tous_items) and
                tous_items[i+1]["role"] == "Klara" and
                tous_items[i+1]["type"] == "message"):
                corps = tous_items[i+1]["text"]
                i += 2
            else:
                i += 1
            contenu = f"{{thinking : {thinking}}}"
            if corps:
                contenu += f"\n\n{corps}"
            messages.append({"role": "Klara", "content": contenu})
        elif item["role"] == "Klara" and item["type"] == "message":
            messages.append({"role": "Klara", "content": item["text"]})
            i += 1
        else:
            i += 1

    return messages


def formater_md(session_name: str, messages: list[dict]) -> str:
    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    lines = [
        f"# Conversation Klara — {session_name}",
        f"*Capturé le {date} via capture_klara_test.py*",
        "", "---", "",
    ]
    for msg in messages:
        role, contenu = msg["role"], msg["content"]
        if role == "brut":
            lines += ["*[Extraction brute — sélecteurs non trouvés]*", "", contenu]
        else:
            lines += [f"**{role} :** {contenu}", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
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
            return

        print(f"✅ Onglet trouvé : {page.url}")
        print("⏳ Extraction en cours (test, 4 cycles descendants)...")
        messages = extraire_messages_test(page)
        if not messages:
            print("⚠️ Aucun message extrait.")
            return

        print(f"✅ {len(messages)} message(s) extrait(s).")
        contenu = formater_md(args.session, messages)
        chemin = nom_fichier(args.session)
        chemin.write_text(contenu, encoding="utf-8")
        LAST_CAPTURE.write_text(str(chemin), encoding="utf-8")
        print(f"✅ Sauvegardé : {chemin}")
        print(f"📝 Dernier fichier : {LAST_CAPTURE}")


if __name__ == "__main__":
    main()