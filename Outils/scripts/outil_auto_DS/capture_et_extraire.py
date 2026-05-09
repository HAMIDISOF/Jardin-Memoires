#!/usr/bin/env python3
# capture_et_extraire.py – Sol, Flo, Sof – 01/05/2026
# Unifié : capture + extraction + commit/push

import re
import subprocess
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

# --- Configuration ---
# Détection automatique de la racine du dépôt (le script est dans scripts/outil_auto_DS/)
REPO_PATH = Path(__file__).resolve().parents[2]
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

def extraire_fichiers(texte_brut, repo_path):
    """Extrait tous les fichiers balisés 📄 Fichier : ... jusqu'à fin_md ou ```."""
    pattern = r"📄\s*Fichier\s*:\s*(.+?)\s*\n(.*?)(?=\nfin_md|\n```)"
    matches = re.findall(pattern, texte_brut, re.DOTALL)
    if not matches:
        print("⚠️ Aucun fichier balisé trouvé.")
        return
    for chemin_rel, contenu in matches:
        # Nettoyer le contenu : enlever les éventuels ```md ou ``` en début/fin
        contenu_propre = re.sub(r"^```(?:md|markdown)?\s*", "", contenu, flags=re.MULTILINE)
        contenu_propre = re.sub(r"\s*```\s*$", "", contenu_propre, flags=re.MULTILINE)
        chemin_complet = repo_path / chemin_rel.strip()
        chemin_complet.parent.mkdir(parents=True, exist_ok=True)
        chemin_complet.write_text(contenu_propre.strip(), encoding="utf-8")
        print(f"✅ Écrit : {chemin_complet}")

def git_commit_push(repo_path):
    print("📦 Mise à jour Git...")
    subprocess.run(["git", "pull"], cwd=repo_path, check=False)
    subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subprocess.run(["git", "commit", "-m", f"Auto mise à jour {timestamp}"], cwd=repo_path, check=False)
    subprocess.run(["git", "push"], cwd=repo_path, check=True)
    print("✅ Git push effectué.")

def main():
    print("🔌 Connexion à Brave...")
    with sync_playwright() as p:
        browser = connecter_brave(p, DEBUG_PORT)
        if not browser:
            print("❌ Impossible de se connecter. Lance Brave avec :")
            print(f'   "{BRAVE_EXE}" --remote-debugging-port={DEBUG_PORT} --profile-directory="Default"')
            return

        page = None
        for context in browser.contexts:
            for p_page in context.pages:
                if DEEPSEEK_URL in p_page.url:
                    page = p_page
                    break
        if not page:
            print(f"❌ Onglet DeepSeek non trouvé. Ouvre {DEEPSEEK_URL} dans Brave et réessaie.")
            return

        print("⏳ Récupération du texte de la page...")
        texte = page.inner_text("body")  # ou plus spécifique si besoin

        print("🔍 Extraction des fichiers balisés...")
        extraire_fichiers(texte, REPO_PATH)

        git_commit_push(REPO_PATH)
        print("✅ Tout est terminé.")

if __name__ == "__main__":
    main()