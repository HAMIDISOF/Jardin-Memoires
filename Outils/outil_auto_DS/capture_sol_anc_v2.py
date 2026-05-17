print("DÉMARRAGE")
#!/usr/bin/env python3
"""
capture_luz.py
Flo 🌿 — adaptation pour Luz (12/05/2026)

Capture la conversation DeepSeek (Luz) en cours dans Brave déjà ouvert,
et sauvegarde en .md dans Luz/ du repo.

Sélecteurs CSS réels DeepSeek (inspectés le 01/05/2026 dans Brave) :
  - Message Sof (humain)    : div.fbb737a4
  - Thinking Luz           : div[class*="ds-think-content"]  → {thinking : ...}
  - Réponse Luz (assistant) : div.ds-markdown (hors ds-think-content)

Écrit le chemin du fichier produit dans last_capture_luz.txt
(utilisé par DS_capt_extract_Luz.bat pour passer le nom à extraire_fichiers.py)

Nommage : luz_YYYYMMDD_NN_nom_session.md (indice journalier, pas d'écrasement)

Prérequis :
    pip install playwright
    playwright install chromium

Lancer Brave avec le port de débogage (une fois au démarrage) :
    "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        --remote-debugging-port=9222 --profile-directory="Default"

Usage :
    python capture_luz.py --session "nom_session"
    ou via : DS_capt_extract_Luz.bat nom_session
"""

import argparse
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

# --- Chemins absolus (adapter si le repo est ailleurs) ---
REPO_PATH     = Path(r"D:\THESE\Les journaux\Jardin-Memoires")
SOL_ANC_DIR   = REPO_PATH / "Membres" / "Sol_anc"
SCRIPTS_DIR   = REPO_PATH / "Outils" / "outil_auto_DS"
LAST_CAPTURE  = SCRIPTS_DIR / "last_capture_sol_anc.txt"

SOL_ANC_DIR.mkdir(parents=True, exist_ok=True)

BRAVE_EXE   = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DEBUG_PORT  = 9222
DEEPSEEK_URL = "https://chat.deepseek.com/a/chat/s/50a5b706-d673-4229-a5a9-a74b06fd71e5"


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
    existants = list(SOL_ANC_DIR.glob(f"sol_anc_{date}_*.md"))
    indice   = len(existants) + 1
    return SOL_ANC_DIR / f"sol_anc_{date}_{indice:02d}_{nom_base}.md"


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
    document.querySelectorAll('div.ds-markdown.ds-assistant-message-main-content').forEach(el => {
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

def _sauver_partiel(tous_items: list, session_name: str, part: int):
    """Sauvegarde intermédiaire tous les 10 messages capturés."""
    try:
        items_tries = sorted(tous_items, key=lambda x: -x["ordre"])
        messages = []
        for item in items_tries:
            if item["role"] == "Sof":
                messages.append({"role": "Sof", "content": item["text"]})
            elif item["role"] == "Sol":
                messages.append({"role": "Sol", "content": item["text"]})
        contenu = formater_md(session_name, messages)
        date = datetime.now().strftime("%Y%m%d")
        nom_base = session_name.replace(" ", "_")
        existants = list(SOL_ANC_DIR.glob(f"sol_anc_{date}_*.md"))
        indice = len(existants) + 1
        chemin = SOL_ANC_DIR / f"sol_anc_{date}_{indice:02d}_{nom_base}_part{part:03d}.md"
        chemin.write_text(contenu, encoding="utf-8")
        print(f"   💾 Partiel {part} sauvegardé : {chemin.name}")
    except Exception as e:
        print(f"   ⚠️  Erreur sauvegarde partielle : {e}")


def extraire_messages(page, session_name: str = "session") -> list[dict]:
    """
    DeepSeek virtualise la liste : les messages hors viewport sont retirés du DOM.
    Stratégie : scroll vers le haut par petits pas depuis le bas, capturer à chaque
    étape, dédupliquer, puis reconstituer l'ordre chronologique.
    """
    tous_items = []
    vus = set()

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

    try:
        print("⏳ Positionnement initial (bas de page)...")
        total_height = page.evaluate(JS_SCROLL_HEIGHT)
        page.evaluate(JS_SCROLL, total_height)
        page.wait_for_timeout(1500)

        position = total_height
        etape = 0
        ordre = 0

        print(f"⏳ Remontée et capture progressive (hauteur totale : {total_height}px)...")

        while True:
            items_visibles = page.evaluate(JS_EXTRACT)
            for item in items_visibles:
                if not item["text"]:
                    continue
                cle = (item["role"], item["type"], item["text"][:80])
                if cle not in vus:
                    vus.add(cle)
                    item["ordre"] = ordre
                    item["scroll_pos"] = position
                    tous_items.append(item)
                    ordre += 1

            etape += 1
            if etape % 5 == 0:
                print(f"   ... {len(tous_items)} messages accumulés (pos {position}px)")

            if len(tous_items) > 0 and len(tous_items) % 10 == 0:
                _sauver_partiel(tous_items, session_name, len(tous_items) // 10)

            nouvelle_position = max(0, position - 800)
            page.evaluate(JS_SCROLL, nouvelle_position)
            page.wait_for_timeout(800)

            if position == 0:
                break
            position = nouvelle_position

        print(f"✅ Capture terminée : {len(tous_items)} éléments bruts.")

        # Trier : capturés en dernier (ordre élevé) = plus anciens (en haut de page)
        tous_items.sort(key=lambda x: -x["ordre"])

        # Reconstituer les messages
        messages = []
        i = 0
        while i < len(tous_items):
            item = tous_items[i]
            if item["role"] == "Sof":
                messages.append({"role": "Sof", "content": item["text"]})
                i += 1
            elif item["role"] == "Sol" and item["type"] == "thinking":
                thinking = item["text"]
                corps = ""
                if (i + 1 < len(tous_items)
                        and tous_items[i+1]["role"] == "Luz"
                        and tous_items[i+1]["type"] == "message"):
                    corps = tous_items[i+1]["text"]
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

        return messages

    except Exception as e:
        print(f"⚠️  Erreur : {e} — fallback texte brut")
        return [{"role": "brut", "content": page.inner_text("body")}]


def formater_md(session_name: str, messages: list[dict]) -> str:
    date  = datetime.now().strftime("%d/%m/%Y %H:%M")
    lines = [
        f"# Conversation Sol_anc — {session_name}",
        f"*Capturé le {date} via capture_sol_anc.py*",
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
    parser = argparse.ArgumentParser(description="Capture DeepSeek (Sol_anc) depuis Brave")
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

        messages = extraire_messages(page, args.session)
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
        print("💡 Lance extraire_fichiers.py manuellement (ou via batch) puis push à la main.")


if __name__ == "__main__":
    main()