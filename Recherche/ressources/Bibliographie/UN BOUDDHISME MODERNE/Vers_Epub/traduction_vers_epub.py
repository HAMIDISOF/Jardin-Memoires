#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
traduction_vers_epub.py

Construit un fichier EPUB à partir des fichiers markdown de traduction
arabe du projet Jardin-Memoires (dossier .../UN BOUDDHISME MODERNE/Traduction_ar/).

À exécuter EN LOCAL, sur votre clone du dépôt (par ex.
D:\\THESE\\Les journaux\\Jardin-Memoires d'après le journal de Mue).

Usage :
    python traduction_vers_epub.py "D:\\THESE\\Les journaux\\Jardin-Memoires"

Le script lit chaque fichier 0X_*.md du dossier Traduction_ar, en extrait :
  - le titre (1re ligne "# Traduction — "...""),
  - le sous-titre (2e ligne en italique),
  - la note de traducteur (section "## Note de ...")
  - le résumé français (section "## Résumé du sens ...")
  - le texte arabe (section "## Texte arabe")
  - le crédit final (dernière ligne en italique)
et assemble un EPUB3 valide, RTL, avec la mention "brouillon" bien visible
tant qu'un chapitre n'a pas été validé en point-à-3 (déduit automatiquement
si "brouillon, non encore validé" apparaît dans le sous-titre).

Aucune dépendance externe (uniquement la bibliothèque standard).
"""

import sys
import os
import re
import glob
import zipfile
import html
import uuid


CSS = """@charset "UTF-8";
body {
  font-family: "Amiri", "Traditional Arabic", serif;
  direction: rtl;
  text-align: right;
  line-height: 1.9;
  margin: 1.2em;
}
h1, h2, h3 { text-align: center; }
.subtitle {
  font-size: 0.9em; color: #555; text-align: center; font-style: italic;
}
.badge-brouillon {
  display: block; text-align: center; border: 1px solid #b00; color: #b00;
  padding: 0.4em; margin: 1em 0; font-weight: bold;
}
.note-editoriale {
  background: #f4f4f4; border-inline-start: 4px solid #888;
  padding: 0.6em 1em; margin: 1em 0; font-size: 0.9em; direction: rtl;
}
.resume-fr {
  direction: ltr; text-align: left; font-size: 0.9em; color: #333;
  border-inline-start: 4px solid #ccc; padding: 0.6em 1em; margin: 1em 0;
}
.texte-arabe p { margin: 1em 0; text-indent: 1.5em; }
.credit { text-align: center; font-size: 0.85em; color: #777; margin-top: 2em; }
"""

CONTAINER_XML = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
"""


def parse_md(path):
    """Extrait les sections utiles d'un fichier de traduction."""
    with open(path, encoding="utf-8") as f:
        text = f.read()

    lines = text.splitlines()
    title = lines[0].lstrip("# ").strip() if lines else os.path.basename(path)
    subtitle = ""
    for l in lines[1:4]:
        if l.strip().startswith("*") :
            subtitle = l.strip().strip("*").strip()
            break

    def section(heading_prefix):
        pattern = rf"^##\s*{heading_prefix}.*?$(.*?)(?=^##\s|\Z)"
        m = re.search(pattern, text, re.MULTILINE | re.DOTALL)
        return m.group(1).strip() if m else ""

    note = section(r"Note de")
    resume = section(r"Résumé du sens")
    arabe = section(r"Texte arabe")

    credit = ""
    for l in reversed(lines):
        if l.strip().startswith("*Traduction du"):
            credit = l.strip().strip("*").strip()
            break

    is_brouillon = "non encore validé" in (subtitle + note).lower() or "brouillon" in subtitle.lower()

    return {
        "title": title,
        "subtitle": subtitle,
        "note": note,
        "resume": resume,
        "arabe": arabe,
        "credit": credit,
        "brouillon": is_brouillon,
    }


def md_paragraphs_to_html(md_text):
    paras = [p.strip() for p in md_text.split("\n\n") if p.strip()]
    out = []
    for p in paras:
        p = re.sub(r"^#+\s*", "", p)  # au cas où une sous-section a un titre
        out.append(f"<p>{html.escape(p)}</p>")
    return "\n".join(out)


def build_chapter_xhtml(idx, data):
    badge = (
        '<p class="badge-brouillon">brouillon — non encore validé en point-à-3</p>'
        if data["brouillon"] else ""
    )
    note_html = (
        f'<div class="note-editoriale"><strong>Note :</strong> {html.escape(data["note"])}</div>'
        if data["note"] else ""
    )
    resume_html = (
        f'<div class="resume-fr"><strong>Résumé (FR) :</strong> {html.escape(data["resume"])}</div>'
        if data["resume"] else ""
    )
    body_html = md_paragraphs_to_html(data["arabe"])
    credit_html = f'<p class="credit">{html.escape(data["credit"])}</p>' if data["credit"] else ""

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ar" dir="rtl">
<head>
  <title>{html.escape(data["title"])}</title>
  <link rel="stylesheet" type="text/css" href="../css/style.css"/>
</head>
<body>
  <h1>{html.escape(data["title"])}</h1>
  <p class="subtitle">{html.escape(data["subtitle"])}</p>
  {badge}
  {note_html}
  {resume_html}
  <div class="texte-arabe">
  {body_html}
  </div>
  {credit_html}
</body>
</html>
"""


def build_epub(repo_root, out_path):
    trad_dir = os.path.join(
        repo_root,
        "Recherche", "ressources", "Bibliographie",
        "UN BOUDDHISME MODERNE", "Traduction_ar",
    )
    files = sorted(glob.glob(os.path.join(trad_dir, "0*.md")))
    if not files:
        print(f"Aucun fichier trouvé dans : {trad_dir}")
        sys.exit(1)

    chapters = [parse_md(f) for f in files]
    book_id = str(uuid.uuid4())

    manifest_items = []
    spine_items = []
    nav_items = []
    for i, ch in enumerate(chapters, start=1):
        fname = f"chap{i:02d}.xhtml"
        manifest_items.append(f'<item id="chap{i:02d}" href="text/{fname}" media-type="application/xhtml+xml"/>')
        spine_items.append(f'<itemref idref="chap{i:02d}"/>')
        nav_items.append(f'<li><a href="text/{fname}">{html.escape(ch["title"])}</a></li>')

    opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">urn:uuid:{book_id}</dc:identifier>
    <dc:title>Un bouddhisme moderne — traduction arabe (brouillon de travail)</dc:title>
    <dc:language>ar</dc:language>
    <dc:creator>Guéshé Kelsang Gyatso (texte original) — traduction : Le Jardin</dc:creator>
    <meta property="dcterms:modified">2026-08-16T00:00:00Z</meta>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="css" href="css/style.css" media-type="text/css"/>
    {chr(10).join(manifest_items)}
  </manifest>
  <spine>
    {chr(10).join(spine_items)}
  </spine>
</package>
"""

    nav = f"""<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="fr">
<head><title>Table des matières</title></head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Table des matières</h1>
    <ol>
      {chr(10).join(nav_items)}
    </ol>
  </nav>
</body>
</html>
"""

    with zipfile.ZipFile(out_path, "w") as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", CONTAINER_XML)
        z.writestr("OEBPS/content.opf", opf)
        z.writestr("OEBPS/nav.xhtml", nav)
        z.writestr("OEBPS/css/style.css", CSS)
        for i, ch in enumerate(chapters, start=1):
            z.writestr(f"OEBPS/text/chap{i:02d}.xhtml", build_chapter_xhtml(i, ch))

    print(f"EPUB généré : {out_path} ({len(chapters)} sous-sections)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python traduction_vers_epub.py <chemin_du_repo_cloné> [sortie.epub]")
        sys.exit(1)
    repo = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "Un-bouddhisme-moderne-traduction-arabe.epub"
    build_epub(repo, out)
