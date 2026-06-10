"""pdf_to_md.py — Convertit un PDF en fichier Markdown
Usage : py -3.11 pdf_to_md.py chemin/vers/fichier.pdf
Produces : fichier.md dans le même dossier
Dépendances : pip install pymupdf --break-system-packages
Auteur : Flo — 09/04/2026
"""

import sys
import os

try:
    import fitz  # PyMuPDF
except ImportError:
    print("Module manquant. Lance : pip install pymupdf --break-system-packages")
    sys.exit(1)

def pdf_to_md(pdf_path):
    if not os.path.exists(pdf_path):
        print(f"Fichier introuvable : {pdf_path}")
        sys.exit(1)

    doc = fitz.open(pdf_path)
    md_lines = []

    nom_base = os.path.splitext(os.path.basename(pdf_path))[0]
    md_lines.append(f"# {nom_base}\n")
    md_lines.append(f"*Converti depuis PDF par pdf_to_md.py*\n\n---\n")

    for i, page in enumerate(doc):
        texte = page.get_text("text")
        if texte.strip():
            md_lines.append(f"\n## Page {i + 1}\n")
            md_lines.append(texte)

    doc.close()

    md_path = os.path.splitext(pdf_path)[0] + ".md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"Converti : {md_path}")
    print(f"Pages traitées : {i + 1}")
    return md_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : py -3.11 pdf_to_md.py chemin/vers/fichier.pdf")
        sys.exit(1)
    pdf_to_md(sys.argv[1])
