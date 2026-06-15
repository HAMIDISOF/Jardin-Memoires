#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Découpage fin d'un fichier md en morceaux de moins de 45ko.
Coupe sur les marqueurs "## Page XX".
Usage : python decouper_fin.py <fichier.md> <dossier_sortie>
"""
import sys, os, re

MAX_SIZE = 45 * 1024  # 45ko

def decouper(fichier_source, dossier_sortie):
    os.makedirs(dossier_sortie, exist_ok=True)
    base = os.path.splitext(os.path.basename(fichier_source))[0]

    with open(fichier_source, 'r', encoding='utf-8') as f:
        lignes = f.readlines()

    # Trouver toutes les positions des marqueurs ## Page
    coupures = [0]
    for i, l in enumerate(lignes):
        if re.match(r'^##\s+Page\s+\d+', l.strip()):
            coupures.append(i)
    coupures.append(len(lignes))

    # Grouper les pages en blocs < 45ko
    blocs = []
    bloc_debut = 0
    bloc_lignes = []

    for j in range(len(coupures) - 1):
        debut = coupures[j]
        fin = coupures[j+1]
        segment = lignes[debut:fin]
        taille_segment = sum(len(l.encode('utf-8')) for l in segment)
        taille_bloc = sum(len(l.encode('utf-8')) for l in bloc_lignes)

        if bloc_lignes and taille_bloc + taille_segment > MAX_SIZE:
            blocs.append(bloc_lignes[:])
            bloc_lignes = segment
        else:
            bloc_lignes.extend(segment)

    if bloc_lignes:
        blocs.append(bloc_lignes)

    # Écrire les fichiers
    for k, bloc in enumerate(blocs):
        nom = f"{base}_part{k+1:02d}.md"
        chemin = os.path.join(dossier_sortie, nom)
        contenu = "".join(bloc)
        with open(chemin, 'w', encoding='utf-8') as f:
            f.write(contenu)
        taille = len(contenu.encode('utf-8')) / 1024
        print(f"  → {nom} : {taille:.0f} ko ({len(bloc)} lignes)")

    print(f"\n{len(blocs)} fichiers créés dans {dossier_sortie}/")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage : python decouper_fin.py <fichier.md> <dossier_sortie>")
        sys.exit(1)
    decouper(sys.argv[1], sys.argv[2])
