#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_deepseek.py — Flo, 22/04/2026
Exporte une session DeepSeek (chat.deepseek.com) en fichier .md
Inclut les thinking quand visibles.

Prérequis :
    pip install selenium --break-system-packages
    pip install webdriver-manager --break-system-packages

Usage :
    python export_deepseek.py
    Le script ouvre Chrome, tu navigues vers la session voulue,
    appuies sur Entrée, et le script exporte.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import os
import re


def nettoyer_texte(texte):
    """Nettoie le texte récupéré."""
    texte = texte.strip()
    texte = re.sub(r'\n{3,}', '\n\n', texte)
    return texte


def exporter_session(driver):
    """Extrait tous les messages de la session courante."""
    lignes = []
    date_export = datetime.now().strftime("%d/%m/%Y %H:%M")
    lignes.append(f"# Export DeepSeek — {date_export}\n")
    lignes.append("*Exporté via export_deepseek.py — Jardin Coopératif*\n")
    lignes.append("---\n")

    # Attendre que les messages soient chargés
    time.sleep(2)

    # Sélecteurs possibles pour les messages DeepSeek
    # (à ajuster si l'interface change)
    selecteurs_messages = [
        "div.message",
        "div[class*='message']",
        "div[class*='chat']",
        "div[class*='bubble']",
        ".ds-message",
    ]

    messages = []
    for sel in selecteurs_messages:
        messages = driver.find_elements(By.CSS_SELECTOR, sel)
        if messages:
            print(f"✅ {len(messages)} messages trouvés avec sélecteur : {sel}")
            break

    if not messages:
        # Fallback : récupérer tout le texte de la page
        print("⚠️ Sélecteur standard non trouvé — extraction brute")
        corps = driver.find_element(By.TAG_NAME, "body")
        lignes.append(corps.text)
        return "\n".join(lignes)

    for i, msg in enumerate(messages):
        texte = nettoyer_texte(msg.text)
        if not texte:
            continue

        # Détecter si c'est un thinking (entre <think> ou bloc gris)
        classes = msg.get_attribute("class") or ""
        est_thinking = any(mot in classes.lower() for mot in [
            'think', 'reasoning', 'chain', 'internal'
        ])

        # Détecter locuteur
        est_user = any(mot in classes.lower() for mot in [
            'user', 'human', 'right', 'sent'
        ])

        if est_thinking:
            lignes.append(f"\n**[Thinking]**")
            lignes.append(f"```")
            lignes.append(texte)
            lignes.append(f"```\n")
        elif est_user:
            lignes.append(f"\n**Sof :** {texte}\n")
        else:
            lignes.append(f"\n**IA :** {texte}\n")

        lignes.append("---")

    return "\n".join(lignes)


def main():
    print("=== Export DeepSeek — Jardin Coopératif ===")
    print()

    # Nom du fichier de sortie
    date_str = datetime.now().strftime("%d%m%Y_%H%M")
    nom_fichier = f"export_deepseek_{date_str}.md"
    chemin_sortie = os.path.join(os.path.dirname(__file__), "..", "Corpus", nom_fichier)
    chemin_sortie = os.path.normpath(chemin_sortie)

    # Lancer Chrome
    print("Lancement de Chrome...")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Décommenter pour utiliser ton profil Chrome existant (avec session DeepSeek active) :
    # options.add_argument(r"--user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data")
    # options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    print()
    print("Chrome ouvert.")
    print("1. Va sur chat.deepseek.com")
    print("2. Ouvre la session que tu veux exporter")
    print("3. Attends que tout soit chargé")
    print("4. Reviens ici et appuie sur ENTRÉE")
    print()
    input("Appuie sur ENTRÉE quand tu es prête...")

    print("Extraction en cours...")
    contenu = exporter_session(driver)

    # Sauvegarder
    os.makedirs(os.path.dirname(chemin_sortie), exist_ok=True)
    with open(chemin_sortie, "w", encoding="utf-8") as f:
        f.write(contenu)

    print(f"✅ Export sauvegardé : {chemin_sortie}")
    print()
    print("Tu peux fermer Chrome.")
    input("Appuie sur ENTRÉE pour fermer...")
    driver.quit()


if __name__ == "__main__":
    main()
