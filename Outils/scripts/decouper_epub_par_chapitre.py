#!/usr/bin/env python3
"""
decouper_epub_par_chapitre.py

Découpe un fichier epub en un fichier texte par chapitre/section, en
s'appuyant sur la table des matières interne du livre (toc.ncx), plutôt
que sur un découpage arbitraire par taille. Chaque fichier de sortie
contient le texte nettoyé (sans balises HTML) d'un chapitre, avec son
vrai titre.

Usage :
    python3 decouper_epub_par_chapitre.py livre.epub [dossier_sortie]

Produit :
    dossier_sortie/
        01_A-propos-de-l-auteur.txt
        02_Ordre-de-lecture...txt
        ...
        _manifeste.json   (titre réel, fichier source interne, nb de mots)
"""

import sys
import os
import re
import json
import zipfile
import argparse
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from html.parser import HTMLParser

NCX_NS = {"ncx": "http://www.daisy.org/z3986/2005/ncx/"}


class ExtracteurTexte(HTMLParser):
    """Extrait le texte visible d'un xhtml, en gardant des sauts de paragraphe."""

    BALISES_BLOC = {
        "p", "div", "h1", "h2", "h3", "h4", "h5", "h6",
        "li", "br", "tr", "blockquote",
    }
    BALISES_IGNOREES = {"script", "style", "head"}

    def __init__(self):
        super().__init__()
        self.morceaux = []
        self._dans_ignore = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.BALISES_IGNOREES:
            self._dans_ignore += 1
        elif tag in self.BALISES_BLOC:
            self.morceaux.append("\n")

    def handle_endtag(self, tag):
        if tag in self.BALISES_IGNOREES:
            self._dans_ignore = max(0, self._dans_ignore - 1)
        elif tag in self.BALISES_BLOC:
            self.morceaux.append("\n")

    def handle_data(self, data):
        if not self._dans_ignore:
            self.morceaux.append(data)

    def texte(self):
        brut = "".join(self.morceaux)
        # Normaliser les espaces et sauts de ligne multiples
        brut = re.sub(r"[ \t]+", " ", brut)
        brut = re.sub(r"\n[ \t]*\n[ \t]*(\n[ \t]*)+", "\n\n", brut)
        lignes = [l.strip() for l in brut.split("\n")]
        return "\n".join(lignes).strip()


def slugifier(texte, max_len=60):
    texte = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode("ascii")
    texte = re.sub(r"[^\w\s-]", "", texte).strip().replace(" ", "-")
    texte = re.sub(r"-+", "-", texte)
    return texte[:max_len].strip("-") or "sans-titre"


def trouver_opf(dossier_extrait):
    container_path = dossier_extrait / "META-INF" / "container.xml"
    tree = ET.parse(container_path)
    ns = {"c": "urn:oasis:names:tc:opendocument:xmlns:container"}
    rootfile = tree.getroot().find(".//c:rootfile", ns)
    return dossier_extrait / rootfile.get("full-path")


def trouver_ncx(dossier_extrait, chemin_opf):
    tree = ET.parse(chemin_opf)
    ns = {"opf": "http://www.idpf.org/2007/opf"}
    manifest = tree.getroot().find("opf:manifest", ns)
    for item in manifest.findall("opf:item", ns):
        if item.get("media-type") == "application/x-dtbncx+xml":
            return chemin_opf.parent / item.get("href")
    raise ValueError("toc.ncx introuvable dans le manifest de l'epub.")


def lister_ordre_lecture(chemin_opf):
    """Retourne la liste ordonnée (spine) des fichiers .xhtml dans leur ordre réel de lecture."""
    tree = ET.parse(chemin_opf)
    ns = {"opf": "http://www.idpf.org/2007/opf"}
    manifest = tree.getroot().find("opf:manifest", ns)
    id_vers_href = {item.get("id"): item.get("href") for item in manifest.findall("opf:item", ns)}
    spine = tree.getroot().find("opf:spine", ns)
    ordre = []
    for itemref in spine.findall("opf:itemref", ns):
        href = id_vers_href.get(itemref.get("idref"))
        if href:
            ordre.append(href)
    return ordre


def lister_chapitres(chemin_ncx):
    """Retourne une liste plate ordonnée de (titre, chemin_fichier_relatif) à partir du toc.ncx."""
    tree = ET.parse(chemin_ncx)
    navmap = tree.getroot().find("ncx:navMap", NCX_NS)
    chapitres = []

    def walk(elem):
        for navpoint in elem.findall("ncx:navPoint", NCX_NS):
            label_elem = navpoint.find("ncx:navLabel/ncx:text", NCX_NS)
            content_elem = navpoint.find("ncx:content", NCX_NS)
            titre = (label_elem.text or "").strip() if label_elem is not None else "Sans titre"
            src = content_elem.get("src") if content_elem is not None else None
            if src:
                fichier = src.split("#")[0]
                chapitres.append((titre, fichier))
            walk(navpoint)

    walk(navmap)
    return chapitres


def decouper_epub(chemin_epub, dossier_sortie):
    dossier_sortie = Path(dossier_sortie)
    dossier_sortie.mkdir(parents=True, exist_ok=True)

    dossier_extrait = dossier_sortie / "_epub_extrait_tmp"
    dossier_extrait.mkdir(exist_ok=True)
    with zipfile.ZipFile(chemin_epub) as z:
        z.extractall(dossier_extrait)

    chemin_opf = trouver_opf(dossier_extrait)
    chemin_ncx = trouver_ncx(dossier_extrait, chemin_opf)
    chapitres = lister_chapitres(chemin_ncx)
    ordre_lecture = lister_ordre_lecture(chemin_opf)

    dossier_text = chemin_ncx.parent  # dossier contenant les .xhtml référencés relativement au ncx
    dossier_opf = chemin_opf.parent   # les href du spine sont relatifs au dossier du .opf

    # Pour chaque fichier du sommaire, retrouver sa position dans l'ordre de lecture réel,
    # afin de savoir jusqu'où (fichier suivant du sommaire, exclu) s'étend ce chapitre.
    positions_chapitres = []
    for titre, fichier_relatif in chapitres:
        try:
            pos = ordre_lecture.index(fichier_relatif)
        except ValueError:
            pos = None
        positions_chapitres.append((titre, fichier_relatif, pos))

    fichiers_produits = []
    fichiers_deja_vus = set()

    for idx, (titre, fichier_relatif, pos) in enumerate(positions_chapitres, start=1):
        if pos is None or fichier_relatif in fichiers_deja_vus:
            continue

        # Borne de fin : la position du prochain chapitre du sommaire qui a une position valide et différente
        pos_fin = len(ordre_lecture)
        for _, _, pos_suivant in positions_chapitres[idx:]:
            if pos_suivant is not None and pos_suivant > pos:
                pos_fin = pos_suivant
                break

        fichiers_du_chapitre = ordre_lecture[pos:pos_fin]
        textes = []
        for href in fichiers_du_chapitre:
            chemin_xhtml = dossier_opf / href
            if not chemin_xhtml.exists():
                continue
            with open(chemin_xhtml, encoding="utf-8") as f:
                html = f.read()
            extracteur = ExtracteurTexte()
            extracteur.feed(html)
            t = extracteur.texte()
            if t:
                textes.append(t)
            fichiers_deja_vus.add(href)

        texte = "\n\n".join(textes)
        nom_fichier = f"{idx:02d}_{slugifier(titre)}.txt"
        chemin_sortie = dossier_sortie / nom_fichier
        with open(chemin_sortie, "w", encoding="utf-8") as f:
            f.write(f"# {titre}\n\n{texte}\n")

        nb_mots = len(texte.split())
        fichiers_produits.append(
            {
                "fichier": nom_fichier,
                "titre": titre,
                "sources_internes": fichiers_du_chapitre,
                "mots": nb_mots,
            }
        )

    with open(dossier_sortie / "_manifeste.json", "w", encoding="utf-8") as f:
        json.dump(fichiers_produits, f, ensure_ascii=False, indent=2)

    # Nettoyage du dossier temporaire d'extraction
    import shutil
    shutil.rmtree(dossier_extrait)

    return fichiers_produits


def main():
    parser = argparse.ArgumentParser(
        description="Découpe un epub en fichiers texte, un par chapitre, selon sa table des matières interne."
    )
    parser.add_argument("fichier_epub", help="Chemin du fichier .epub à découper")
    parser.add_argument(
        "dossier_sortie", nargs="?", default="chapitres_decoupes", help="Dossier de sortie (créé automatiquement)"
    )
    args = parser.parse_args()

    if not os.path.isfile(args.fichier_epub):
        print(f"Erreur : fichier introuvable : {args.fichier_epub}")
        sys.exit(1)

    fichiers = decouper_epub(args.fichier_epub, args.dossier_sortie)

    print(f"\n{len(fichiers)} chapitres/sections extraits dans '{args.dossier_sortie}/' :\n")
    for info in fichiers:
        print(f"  {info['fichier']}  —  {info['titre']}  ({info['mots']} mots)")


if __name__ == "__main__":
    main()
