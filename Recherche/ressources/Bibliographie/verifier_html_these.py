#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import glob
from pathlib import Path

def extraire_titres_tdm(fichier_tdm):
    """
    Lit le fichier TDM (Markdown) et retourne une liste de titres (chaîne)
    dans l'ordre d'apparition.
    Exemple de ligne reconnue : "I. L’éthique de la connaissance" ou "A-1-2 L’exemplarité..."
    """
    titres = []
    with open(fichier_tdm, 'r', encoding='utf-8') as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue
            # On ignore les lignes qui sont des séparateurs "---" ou des nombres seuls
            if ligne.startswith('---') or ligne.isdigit():
                continue
            # On ignore les lignes avec "TABLE DES MATIERES" ou "Introduction" sans numéro?
            # On capture toute ligne qui commence par un chiffre romain, un nombre, une lettre majuscule suivie d'un point,
            # ou des points A-1, B-2 etc.
            if re.match(r'^(?:[IVXLCDM]+|[0-9]+|[A-Z])(?:[-–—\.]|[0-9]| )', ligne):
                titres.append(ligne)
            # On capture aussi les sous-sections comme "A-1-1", "A-1-2"
            elif re.match(r'^[A-Z]-\d+(-\d+)?', ligne):
                titres.append(ligne)
            # On capture les sections qui n'ont pas de numéro explicite (ex: "Introduction", "Conclusion")
            elif ligne in ['Introduction', 'Conclusion', 'BIBLIOGRAPHIE', 'Index des noms']:
                titres.append(ligne)
            # On capture aussi "Ethique et rationalité" (sans numéro mais dans le texte)
            # Pour être large, on prend toute ligne non vide qui n'est pas que des chiffres
            elif len(ligne) > 3 and not ligne[0].isdigit():
                # mais attention : certaines lignes de contenu pourraient être prises
                titres.append(ligne)
    return titres

def extraire_titres_html(chemin_html):
    """
    Extrait les titres (balises h1, h2, h3) d'un fichier HTML.
    Retourne une liste de chaînes (le texte du titre).
    """
    titres = []
    with open(chemin_html, 'r', encoding='utf-8') as f:
        contenu = f.read()
    # Recherche des balises <h1>...</h1>, <h2>...</h2>, <h3>...</h3>
    pattern = re.compile(r'<h[1-3][^>]*>(.*?)</h[1-3]>', re.IGNORECASE | re.DOTALL)
    matches = pattern.findall(contenu)
    for m in matches:
        # Nettoyer le texte : enlever les balises internes éventuelles et espaces
        titre = re.sub(r'<[^>]+>', '', m)
        titre = ' '.join(titre.split())
        if titre:
            titres.append(titre)
    return titres

def main():
    # --- À MODIFIER SI NÉCESSAIRE ---
    # Chemin vers le répertoire contenant les fichiers HTML (change selon ton installation)
    repertoire_html = Path(r"Jardin-Memoires/Recherche/ressources/Bibliographie/Peschard_these")
    # Chemin vers le fichier TDM
    fichier_tdm = repertoire_html / "1_Isabelle_Peschard_These_Table_des_Matières.md"
    
    if not fichier_tdm.exists():
        print(f"Fichier TDM introuvable : {fichier_tdm}")
        return
    
    print("Lecture de la table des matières...")
    titres_tdm = extraire_titres_tdm(fichier_tdm)
    print(f"  → {len(titres_tdm)} sections détectées dans la TDM.")
    
    # Récupérer tous les fichiers HTML du répertoire (sauf le TDM)
    fichiers_html = sorted(glob.glob(str(repertoire_html / "*.html")))
    # Trier par nom (lexicographique) pour respecter 1_..., 2_..., 6.1_...
    fichiers_html.sort()
    
    if not fichiers_html:
        print("Aucun fichier HTML trouvé dans", repertoire_html)
        return
    
    print(f"Traitement de {len(fichiers_html)} fichiers HTML...")
    
    # On va rassembler tous les titres extraits des HTML dans l'ordre des fichiers
    titres_html_sequence = []
    for fhtml in fichiers_html:
        titres = extraire_titres_html(fhtml)
        if titres:
            for t in titres:
                titres_html_sequence.append(t)
        else:
            # Si aucun titre trouvé, on ajoute le nom du fichier comme repère
            titres_html_sequence.append(f"[Aucun titre trouvé dans {os.path.basename(fhtml)}]")
    
    print("\n===== RAPPORT DE COMPARAISON =====\n")
    print("Titres TDM :")
    for i, t in enumerate(titres_tdm):
        print(f"{i+1:3d}. {t[:80]}")
    
    print("\nTitres extraits des fichiers HTML (dans l'ordre des fichiers) :")
    for i, t in enumerate(titres_html_sequence):
        print(f"{i+1:3d}. {t[:80]}")
    
    # Vérification simple des écarts de longueur
    diff = len(titres_html_sequence) - len(titres_tdm)
    if diff > 0:
        print(f"\n⚠️  Les fichiers HTML contiennent {diff} titre(s) de plus que la TDM.")
    elif diff < 0:
        print(f"\n⚠️  Les fichiers HTML manquent de {-diff} titre(s) par rapport à la TDM.")
    else:
        print("\n✅ Le nombre de titres correspond entre la TDM et les HTML.")
    
    # Optionnel : comparaison séquentielle approximative (par similarité de chaînes)
    print("\n--- Correspondance approximative (premiers mots) ---")
    for i in range(min(len(titres_tdm), len(titres_html_sequence))):
        tdm = titres_tdm[i][:40]
        html = titres_html_sequence[i][:40]
        if tdm.lower() == html.lower():
            print(f"✓ {i+1:3d} : OK")
        else:
            print(f"✗ {i+1:3d} : TDM='{tdm}' / HTML='{html}'")

if __name__ == "__main__":
    main()