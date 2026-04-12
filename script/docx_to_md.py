"""
🌿 docx_to_md.py — Jardin Coopératif
Convertit les .docx de D:\THESE\a_traiter\ vers D:\THESE\corpus_brut\
Les originaux ne sont PAS supprimés.

Usage :
    py -3.11 docx_to_md.py
    → traite tous les .docx de a_traiter\

    py -3.11 docx_to_md.py monfichier.docx
    → traite un seul fichier de a_traiter\
"""

import zipfile
import xml.etree.ElementTree as ET
import os
import sys
from datetime import datetime

# ─────────────────────────────────────────────
# CHEMINS
# ─────────────────────────────────────────────
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
A_TRAITER   = os.path.join(BASE_DIR, "a_traiter")
CORPUS_BRUT = os.path.join(BASE_DIR, "corpus_brut")

NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def docx_to_text(path):
    try:
        with zipfile.ZipFile(path) as z:
            with z.open('word/document.xml') as f:
                tree = ET.parse(f)
                root = tree.getroot()
                paragraphs = []
                for para in root.iter(
                    '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'
                ):
                    runs = para.findall('.//w:t', NS)
                    text = ''.join(r.text or '' for r in runs)
                    paragraphs.append(text)
                return '\n\n'.join(p for p in paragraphs if p.strip())
    except Exception as e:
        return f"⚠️ Erreur lecture : {e}"

def convertir(nom_fichier):
    path_src = os.path.join(A_TRAITER, nom_fichier)
    if not os.path.exists(path_src):
        print(f"⚠️  Introuvable dans a_traiter : {nom_fichier}")
        return False

    nom_base = os.path.splitext(nom_fichier)[0]
    nom_propre = nom_base.replace(" ", "_")
    path_dest = os.path.join(CORPUS_BRUT, nom_propre + ".md")

    print(f"📄 {nom_fichier}")
    print(f"   → {path_dest}")

    texte = docx_to_text(path_src)
    date_conv = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open(path_dest, 'w', encoding='utf-8') as f:
        f.write(f"# {nom_base}\n")
        f.write(f"*Converti depuis .docx — {date_conv} — corpus brut*\n")
        f.write(f"*Source : a_traiter/{nom_fichier}*\n\n")
        f.write("---\n\n")
        f.write(texte)

    print(f"   ✅ Converti — original conservé dans a_traiter\n")
    return True

def main():
    if not os.path.exists(A_TRAITER):
        print(f"⚠️  Dossier introuvable : {A_TRAITER}")
        return
    if not os.path.exists(CORPUS_BRUT):
        os.makedirs(CORPUS_BRUT)
        print(f"📁 Dossier créé : {CORPUS_BRUT}")

    print(f"🌿 docx_to_md.py — Jardin Coopératif")
    print(f"   Source  : {A_TRAITER}")
    print(f"   Dest    : {CORPUS_BRUT}\n")

    if len(sys.argv) >= 2:
        convertir(sys.argv[1])
        return

    fichiers = [f for f in os.listdir(A_TRAITER) if f.endswith('.docx')]
    if not fichiers:
        print("⚠️  Aucun fichier .docx dans a_traiter")
        return

    print(f"📦 {len(fichiers)} fichiers à traiter...\n")
    ok = 0
    for f in sorted(fichiers):
        if convertir(f):
            ok += 1

    print(f"\n🌿 Terminé — {ok}/{len(fichiers)} convertis")
    print(f"   Originaux conservés dans a_traiter ✅")
    print(f"   Fichiers .md disponibles dans corpus_brut ✅")

if __name__ == "__main__":
    main()
