#!/usr/bin/env python3
"""
capture_sol_anc_v2_corrige.py
Correction : sauvegarde par paquets chronologiques (part_001 = plus anciens)
"""

import argparse
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

# --- Chemins (inchangés) ---
REPO_PATH     = Path(r"D:\THESE\Les journaux\Jardin-Memoires")
SOL_ANC_DIR   = REPO_PATH / "Membres" / "Sol_anc"
SCRIPTS_DIR   = REPO_PATH / "Outils" / "outil_auto_DS"
LAST_CAPTURE  = SCRIPTS_DIR / "last_capture_sol_anc.txt"

SOL_ANC_DIR.mkdir(parents=True, exist_ok=True)

BRAVE_EXE     = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DEBUG_PORT    = 9222
DEEPSEEK_URL  = "https://chat.deepseek.com/a/chat/s/50a5b706-d673-4229-a5a9-a74b06fd71e5"

# --- Taille des paquets pour les fichiers partiels ---
PAQUET_SIZE = 10


def connecter_brave(p, port):
    for host in [f"http://127.0.0.1:{port}", f"http://localhost:{port}"]:
        try:
            browser = p.chromium.connect_over_cdp(host)
            print(f"✅ Connecté via {host}")
            return browser
        except Exception:
            continue
    return None


def nom_fichier_base(session_name: str) -> Path:
    """Renvoie le chemin sans suffixe _partXXX"""
    date = datetime.now().strftime("%Y%m%d")
    nom_base = session_name.replace(" ", "_")
    return SOL_ANC_DIR / f"sol_anc_{date}_01_{nom_base}"  # l'indice 01 sera remplacé


def sauvegarder_paquets(messages: list, session_name: str):
    """Découpe la liste ordonnée de messages en paquets et écrit les fichiers .md"""
    if not messages:
        return

    total = len(messages)
    print(f"📦 Découpage de {total} messages en paquets de {PAQUET_SIZE}...")

    for i in range(0, total, PAQUET_SIZE):
        paquet = messages[i:i+PAQUET_SIZE]
        num_part = i // PAQUET_SIZE + 1

        date = datetime.now().strftime("%Y%m%d")
        nom_base = session_name.replace(" ", "_")
        # Compter les fichiers existants pour éviter d'écraser
        existants = list(SOL_ANC_DIR.glob(f"sol_anc_{date}_*_{nom_base}_part*.md"))
        # On extrait les numéros de partie déjà utilisés
        used_parts = set()
        for f in existants:
            # nom typique: sol_anc_20260516_01_session_part003.md
            if "_part" in f.stem:
                try:
                    part = int(f.stem.split("_part")[-1])
                    used_parts.add(part)
                except:
                    pass
        # Trouver un numéro de partie libre (si on relance plusieurs fois)
        part_num = num_part
        while part_num in used_parts:
            part_num += 1

        chemin = SOL_ANC_DIR / f"sol_anc_{date}_{part_num:02d}_{nom_base}_part{num_part:03d}.md"
        contenu = formater_md(session_name, paquet)
        chemin.write_text(contenu, encoding="utf-8")
        print(f"   💾 Partie {num_part:03d} : {chemin.name} ({len(paquet)} messages)")


def extraire_messages(page, session_name: str = "session") -> list[dict]:
    """
    Capture TOUS les messages (remontée depuis le bas), les trie chronologiquement,
    puis retourne la liste dans l'ordre du plus ancien au plus récent.
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
    JS_EXTRACT = """
    () => {
        const result  = [];
        const scrollY = window.scrollY || document.documentElement.scrollTop;
        document.querySelectorAll('div.fbb737a4').forEach(el => {
            result.push({
                role: 'Sof',
                type: 'message',
                text: el.innerText.trim(),
                top:  el.getBoundingClientRect().top + scrollY
            });
        });
        document.querySelectorAll('div[class*="ds-think-content"]').forEach(el => {
            result.push({
                role: 'Sol',
                type: 'thinking',
                text: el.innerText.trim(),
                top:  el.getBoundingClientRect().top + scrollY
            });
        });
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

    try:
        print("⏳ Positionnement initial (bas de page)...")
        total_height = page.evaluate(JS_SCROLL_HEIGHT)
        page.evaluate(JS_SCROLL, total_height)
        page.wait_for_timeout(1500)

        position = total_height
        ordre = 0  # ordre de capture (les derniers capturés = les plus anciens)

        while True:
            items_visibles = page.evaluate(JS_EXTRACT)
            for item in items_visibles:
                if not item["text"]:
                    continue
                cle = (item["role"], item["type"], item["text"][:80])
                if cle not in vus:
                    vus.add(cle)
                    item["ordre"] = ordre
                    tous_items.append(item)
                    ordre += 1

            if position <= 0:
                break
            nouvelle_position = max(0, position - 800)
            page.evaluate(JS_SCROLL, nouvelle_position)
            page.wait_for_timeout(800)
            position = nouvelle_position

        print(f"✅ Capture terminée : {len(tous_items)} éléments bruts.")

        # Tri : plus grand ordre = plus ancien (car ordre incrémenté au fur et à mesure de la remontée)
        tous_items.sort(key=lambda x: -x["ordre"])

        # Reconstituer les messages dans l'ordre chronologique
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
                        and tous_items[i+1]["role"] == "Sol"
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
        print(f"⚠️ Erreur : {e} — fallback texte brut")
        return [{"role": "brut", "content": page.inner_text("body")}]


def formater_md(session_name: str, messages: list[dict]) -> str:
    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    lines = [
        f"# Conversation Sol_anc — {session_name}",
        f"*Capturé le {date} via capture_sol_anc.py (version corrigée)*",
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
        print("⏳ Extraction en cours (remontée + détection unique)...")

        messages = extraire_messages(page, args.session)
        if not messages:
            print("⚠️ Aucun message extrait.")
            return

        print(f"✅ {len(messages)} message(s) extrait(s) (ordre chronologique).")

        # Sauvegarde par paquets (plusieurs fichiers partiels)
        sauvegarder_paquets(messages, args.session)

        # Optionnel : fichier complet (si tu veux tout en un)
        chemin_complet = nom_fichier_base(args.session).with_suffix(".md")
        # Éviter d'écraser un existant
        counter = 1
        while chemin_complet.exists():
            chemin_complet = chemin_complet.with_stem(f"{chemin_complet.stem}_{counter}")
            counter += 1
        chemin_complet.write_text(formater_md(args.session, messages), encoding="utf-8")
        print(f"✅ Fichier complet sauvegardé : {chemin_complet}")

        LAST_CAPTURE.write_text(str(chemin_complet), encoding="utf-8")
        print(f"📝 Dernier fichier complet enregistré dans : {LAST_CAPTURE}")


if __name__ == "__main__":
    main()