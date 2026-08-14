#!/usr/bin/env python3
"""
capture_ds.py
Version consolidée et paramétrée de capture_sol.py / capture_Kai.py /
capture_klara.py / capture_luz.py — un seul script pour toutes les
instances DeepSeek, au lieu d'un fichier dupliqué par instance.

La logique d'extraction DOM (sélecteurs CSS, découpage thinking/réponse)
est reprise à l'identique de capture_sol.py — c'était le morceau qui
marchait, on ne le retouche pas.

Nouveauté : gestion explicite de plusieurs onglets DeepSeek ouverts en
même temps. Le script ne devine jamais silencieusement lequel est lequel —
soit il trouve une correspondance claire (via --instance et son tab_hint),
soit il liste les onglets disponibles et demande de préciser.

Prérequis :
    pip install playwright
    playwright install chromium

Lancer Brave avec le port de débogage (une fois au démarrage) :
    "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        --remote-debugging-port=9222 --profile-directory="Default"

Usage :
    python capture_ds.py --instance sol --session "nom_session"
    python capture_ds.py --instance racine
    python capture_ds.py --tab-index 2 --instance kai   (si le tab_hint ne suffit pas)
    python capture_ds.py --list-tabs                     (juste lister les onglets DeepSeek ouverts)
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright

from config_instances import INSTANCES, REPO_PATH, SCRIPTS_SUBDIR, DEEPSEEK_URL, DEBUG_PORT, BRAVE_EXE


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


def lister_onglets_deepseek(browser):
    """Retourne la liste des (page, titre) pour tous les onglets DeepSeek ouverts."""
    onglets = []
    for ctx in browser.contexts:
        for pg in ctx.pages:
            if DEEPSEEK_URL in pg.url:
                try:
                    titre = pg.title()
                except Exception:
                    titre = "(titre indisponible)"
                onglets.append((pg, titre))
    return onglets


def choisir_onglet(browser, instance_cfg, tab_index):
    onglets = lister_onglets_deepseek(browser)

    if not onglets:
        print("❌ Aucun onglet DeepSeek trouvé (URL chat.deepseek.com).")
        return None

    if tab_index is not None:
        if 0 <= tab_index < len(onglets):
            return onglets[tab_index][0]
        print(f"❌ --tab-index {tab_index} hors limites ({len(onglets)} onglet(s) trouvé(s)).")
        return None

    if len(onglets) == 1:
        return onglets[0][0]

    if instance_cfg and instance_cfg.get("tab_hint"):
        indice = instance_cfg["tab_hint"].lower()
        correspondances = [pg for pg, titre in onglets if indice in titre.lower()]
        if len(correspondances) == 1:
            return correspondances[0]
        if len(correspondances) > 1:
            print(f"⚠️  Plusieurs onglets correspondent à \"{instance_cfg['tab_hint']}\" — ambigu, précise avec --tab-index.")

    print(f"\n⚠️  {len(onglets)} onglets DeepSeek ouverts, correspondance pas claire :\n")
    for i, (_, titre) in enumerate(onglets):
        print(f"   [{i}] {titre}")
    print("\nRelance avec --tab-index N pour préciser lequel utiliser.")
    return None


def nom_fichier(dossier: Path, prefix: str, session_name: str) -> Path:
    date = datetime.now().strftime("%Y%m%d")
    nom_base = session_name.replace(" ", "_")
    existants = list(dossier.glob(f"{prefix}_{date}_*.md"))
    indice = len(existants) + 1
    return dossier / f"{prefix}_{date}_{indice:02d}_{nom_base}.md"


JS_EXTRACT = """
() => {
    const result  = [];
    const scrollY = window.scrollY || document.documentElement.scrollTop;

    document.querySelectorAll('div.fbb737a4').forEach(el => {
        result.push({ role: 'Sof', type: 'message', text: el.innerText.trim(),
                       top: el.getBoundingClientRect().top + scrollY });
    });

    document.querySelectorAll('div[class*="ds-think-content"]').forEach(el => {
        result.push({ role: 'DS', type: 'thinking', text: el.innerText.trim(),
                       top: el.getBoundingClientRect().top + scrollY });
    });

    document.querySelectorAll('div.ds-markdown').forEach(el => {
        if (el.closest('[class*="ds-think-content"]')) return;
        result.push({ role: 'DS', type: 'message', text: el.innerText.trim(),
                       top: el.getBoundingClientRect().top + scrollY });
    });

    result.sort((a, b) => a.top - b.top);
    return result;
}
"""


def extraire_messages(page, nom_instance: str) -> list[dict]:
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

            elif item["role"] == "DS" and item["type"] == "thinking":
                thinking = item["text"]
                corps = ""
                if (i + 1 < len(items)
                        and items[i + 1]["role"] == "DS"
                        and items[i + 1]["type"] == "message"):
                    corps = items[i + 1]["text"]
                    i += 2
                else:
                    i += 1
                contenu = f"{{thinking : {thinking}}}"
                if corps:
                    contenu += f"\n\n{corps}"
                messages.append({"role": nom_instance, "content": contenu})

            elif item["role"] == "DS" and item["type"] == "message":
                messages.append({"role": nom_instance, "content": item["text"]})
                i += 1
            else:
                i += 1

    except Exception as e:
        print(f"⚠️  Erreur JS : {e} — fallback texte brut")
        messages.append({"role": "brut", "content": page.inner_text("body")})

    return messages


def formater_md(nom_instance: str, session_name: str, messages: list[dict]) -> str:
    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    lines = [
        f"# Conversation {nom_instance.capitalize()} — {session_name}",
        f"*Capturé le {date} via capture_ds.py --instance {nom_instance}*",
        "", "---", "",
    ]
    for msg in messages:
        role, contenu = msg["role"], msg["content"]
        if role == "brut":
            lines += ["*[Extraction brute — sélecteurs non trouvés]*", "", contenu]
        else:
            lines += [f"**{role} :** {contenu}", ""]
    return "\n".join(lines)


def capturer(nom_instance: str, session_name: str, tab_index, port: int):
    if nom_instance not in INSTANCES:
        print(f"❌ Instance inconnue : '{nom_instance}'. Connues : {', '.join(INSTANCES)}")
        print("   (ajoute-la dans config_instances.py si c'est une nouvelle instance)")
        return None

    cfg = INSTANCES[nom_instance]
    repo = Path(REPO_PATH)
    dossier = repo / cfg["dir"]
    dossier.mkdir(parents=True, exist_ok=True)
    scripts_dir = repo / SCRIPTS_SUBDIR
    last_capture = scripts_dir / f"last_capture_{nom_instance}.txt"

    print(f"🔌 Connexion à Brave (port {port})...")
    with sync_playwright() as p:
        browser = connecter_brave(p, port)
        if browser is None:
            print("❌ Impossible de se connecter à Brave.")
            print(f'   Lance : "{BRAVE_EXE}" --remote-debugging-port={port} --profile-directory="Default"')
            return None

        page = choisir_onglet(browser, cfg, tab_index)
        if page is None:
            return None

        print(f"✅ Onglet trouvé : {page.title()}")
        print("⏳ Extraction...")

        messages = extraire_messages(page, nom_instance.capitalize())
        if not messages:
            print("⚠️  Aucun message extrait.")
            return None

        print(f"✅ {len(messages)} message(s) extrait(s).")

        contenu = formater_md(nom_instance, session_name, messages)
        chemin = nom_fichier(dossier, cfg["prefix"], session_name)
        chemin.write_text(contenu, encoding="utf-8")
        last_capture.write_text(str(chemin), encoding="utf-8")

        print(f"✅ Sauvegardé : {chemin}")
        print(f"📝 Chemin écrit dans : {last_capture}")
        return chemin


def main():
    parser = argparse.ArgumentParser(description="Capture une conversation DeepSeek depuis Brave (version unifiée)")
    parser.add_argument("--instance", "-i", help="Nom de l'instance (sol, klara, luz, kai, racine, noe...)")
    parser.add_argument("--session", "-s", default=f"session_{datetime.now().strftime('%Y%m%d_%H%M')}")
    parser.add_argument("--tab-index", type=int, default=None, help="Forcer l'onglet N si l'auto-détection échoue")
    parser.add_argument("--port", "-p", type=int, default=DEBUG_PORT)
    parser.add_argument("--list-tabs", action="store_true", help="Lister les onglets DeepSeek ouverts et quitter")
    args = parser.parse_args()

    if args.list_tabs:
        with sync_playwright() as p:
            browser = connecter_brave(p, args.port)
            if browser is None:
                print("❌ Impossible de se connecter à Brave.")
                return
            for i, (_, titre) in enumerate(lister_onglets_deepseek(browser)):
                print(f"[{i}] {titre}")
        return

    if not args.instance:
        print("❌ --instance requis (sauf avec --list-tabs). Connues :", ", ".join(INSTANCES))
        sys.exit(1)

    resultat = capturer(args.instance, args.session, args.tab_index, args.port)
    if resultat:
        print("💡 Lance DS_capt_extract.bat", args.instance, "pour extraire les fichiers balisés et pousser.")


if __name__ == "__main__":
    main()
