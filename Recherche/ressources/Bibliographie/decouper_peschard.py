#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Découpage de la thèse Peschard en 7 fichiers par grandes parties.
Usage : python decouper_peschard.py <fichier_source.md> <dossier_sortie>
"""

import sys
import os

# Marqueurs robustes — on cherche des lignes COURTES contenant exactement ces patterns
MARQUEURS = [
    ("01_Introduction",            None),
    ("02_I_Ethique_Connaissance",  "I. L"),       # ligne courte commençant par I.
    ("03_II_Images_Representation","II. DEUX"),
    ("04_III_Pouvoir_Faire",       "III. DU"),
    ("05_Conclusion",              "CONCLUSION"),
    ("06_Bibliographie",           "BIBLIOGRAPHIE"),
    ("07_Index",                   "INDEX DES NOMS"),
]

def trouver_position(lignes, marqueur):
    """
    Cherche une ligne COURTE (< 60 chars) contenant le marqueur.
    Parmi les candidats, prend le dernier — sauf pour CONCLUSION
    où on prend celui suivi d'une ligne quasi-vide (vrai titre de section).
    """
    candidats = []
    for i, ligne in enumerate(lignes):
        l = ligne.strip()
        if marqueur in l.upper() and len(l) < 80:
            candidats.append(i)

    if not candidats:
        return None

    print(f"    {len(candidats)} occurrence(s) courte(s) pour '{marqueur}' : {candidats[:10]}{'...' if len(candidats)>10 else ''}")

    if marqueur == "CONCLUSION":
        # Prendre le candidat suivi d'une ligne vide ou très courte
        for c in reversed(candidats):
            if c + 1 < len(lignes) and len(lignes[c+1].strip()) < 5:
                return c
        return candidats[-1]

    return candidats[-1]

def decouper(fichier_source, dossier_sortie):
    os.makedirs(dossier_sortie, exist_ok=True)
    with open(fichier_source, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
    print(f"Fichier lu : {len(lignes)} lignes, {os.path.getsize(fichier_source)/1024:.0f} ko\n")

    positions = []
    for nom, marqueur in MARQUEURS:
        if marqueur is None:
            pos = 0
        else:
            pos = trouver_position(lignes, marqueur)
            if pos is None:
                print(f"⚠️  NON TROUVÉ : '{marqueur}'")
                continue
            print(f"✓ {nom} → ligne {pos} : {lignes[pos].rstrip()[:70]}\n")
        positions.append((nom, pos))

    positions.sort(key=lambda x: x[1])
    positions.append(("FIN", len(lignes)))

    print("--- Découpage ---")
    for i in range(len(positions) - 1):
        nom, debut = positions[i]
        _, fin = positions[i + 1]
        if fin <= debut:
            print(f"  ⚠️  {nom}.md : incohérent ({debut}→{fin})")
            continue
        contenu = "".join(lignes[debut:fin])
        taille = len(contenu.encode('utf-8')) / 1024
        nom_fichier = os.path.join(dossier_sortie, f"{nom}.md")
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            f.write(contenu)
        print(f"  → {nom}.md : {taille:.0f} ko ({fin - debut} lignes)")

    print("\nDécoupage terminé.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python decouper_peschard.py <fichier_source.md> <dossier_sortie>")
        sys.exit(1)
    decouper(sys.argv[1], sys.argv[2])
