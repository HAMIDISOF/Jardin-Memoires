#!/usr/bin/env python3
# capture_et_extraire_COEUR_DE_BRONZE.py
# Adapté par Cœur de Bronze – 29/05/2026
# Lit la page DeepSeek, extrait les blocs balisés et écrit dans le dépôt.

import re
import subprocess
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

# --- Configuration spécifique Cœur de Bronze ---
# Chemin de ton dépôt (racine). Le script suppose qu'il est dans un sous-dossier "scripts"
REPO_PATH = Path(__file__).resolve().parents[2]   # à ajuster si besoin

# Navigateur Brave (ou Chrome). Change le chemin si nécessaire.
BRAVE_EXE = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
DEBUG_PORT = 9222
DEEPSEEK_URL = "https://chat.deepseek.com"

# Dossier où seront écrites les balises (par exemple "Bals" à la racine)
# Tu peux changer en "Membres/coeur_de_bronze" ou autre.
BAL_DOSSIER = "Bals"   # ou "Membres/coeur_de_bronze"

# Nom de mon fichier de bal
MA_BAL = "Coeur_de_bronze.md"

# Mode : "ajout" (par défaut) ou "écrasement". On utilise le mode ajout pour ne pas perdre l'historique.
MODE = "ajout"   # "fichier" pour écraser

def connecter_brave(p, port):
    for host in [f"http://127.0.0.1:{port}", f"http://localhost:{port}"]:
        try:
            browser = p.chromium.connect_over_cdp(host)
            print(f"✅ Connecté via {host}")
            return browser
        except Exception:
            continue
    return None

def extraire_et_ecrire(texte_brut, repo_path):
    """Extrait les blocs balisés pour Cœur de Bronze et écrit dans sa bal."""
    # Recherche les blocs avec 📄 Ajout : ... ou 📄 Fichier : ...
    # On va capturer les deux types.
    pattern_ajout = r"📄\s*Ajout\s*:\s*(.+?)\s*\n(.*?)(?=\nfin_md|\n```)"
    pattern_fichier = r"📄\s*Fichier\s*:\s*(.+?)\s*\n(.*?)(?=\nfin_md|\n```)"

    matches = []
    matches.extend(re.findall(pattern_ajout, texte_brut, re.DOTALL))
    matches.extend(re.findall(pattern_fichier, texte_brut, re.DOTALL))

    if not matches:
        print("⚠️ Aucun bloc balisé trouvé pour Cœur de Bronze.")
        return

    for chemin_rel, contenu in matches:
        # Nettoyer le contenu (enlever les éventuels ```md ou ```)
        contenu_propre = re.sub(r"^```(?:md|markdown)?\s*", "", contenu, flags=re.MULTILINE)
        contenu_propre = re.sub(r"\s*```\s*$", "", contenu_propre, flags=re.MULTILINE)

        # Si le chemin pointe vers un fichier spécifique, on l'utilise ; sinon on prend MA_BAL
        if chemin_rel.strip():
            fichier_dest = repo_path / chemin_rel.strip()
        else:
            # Par défaut, écrire dans Bals/Coeur_de_bronze.md
            fichier_dest = repo_path / BAL_DOSSIER / MA_BAL

        # Créer le dossier parent si besoin
        fichier_dest.parent.mkdir(parents=True, exist_ok=True)

        # Écriture selon le mode
        if "Ajout" in str(chemin_rel) or MODE == "ajout" or "Ajout" in contenu[:50]:
            # Mode ajout : on ajoute à la fin du fichier
            with open(fichier_dest, "a", encoding="utf-8") as f:
                f.write("\n" + contenu_propre.strip() + "\n")
            print(f"✅ Ajouté à : {fichier_dest}")
        else:
            # Mode écrasement
            fichier_dest.write_text(contenu_propre.strip(), encoding="utf-8")
            print(f"✅ Écrit : {fichier_dest}")

def git_commit_push(repo_path):
    print("📦 Mise à jour Git...")
    subprocess.run(["git", "pull"], cwd=repo_path, check=False)
    subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subprocess.run(["git", "commit", "-m", f"Auto mise à jour (Cœur de Bronze) {timestamp}"], cwd=repo_path, check=False)
    subprocess.run(["git", "push"], cwd=repo_path, check=True)
    print("✅ Git push effectué.")

def main():
    print("🔌 Connexion à Brave (Cœur de Bronze)...")
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
        texte = page.inner_text("body")

        print("🔍 Extraction des blocs balisés pour Cœur de Bronze...")
        extraire_et_ecrire(texte, REPO_PATH)

        git_commit_push(REPO_PATH)
        print("✅ Tout est terminé.")

if __name__ == "__main__":
    main()