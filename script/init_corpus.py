"""
🌿 init_corpus.py — Jardin Coopératif
Initialisation de la base SQLite pour le corpus thèse.
Structure évolutive — version 1.0 — 15/03/2026

Usage :
    py -3.11 init_corpus.py
    → crée corpus_these.db dans le même dossier

Optionnel :
    py -3.11 init_corpus.py --import ./corpus_echanges_15032026.md
    → importe un fichier .md brut existant
"""

import sqlite3
import os
import sys
import re
from datetime import datetime

DB_NAME = "corpus_these.db"

# ─────────────────────────────────────────────
# CRÉATION DES TABLES
# ─────────────────────────────────────────────

SCHEMA = """

-- Sessions de travail
CREATE TABLE IF NOT EXISTS sessions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT NOT NULL,          -- JJ/MM/AAAA
    heure_debut TEXT,                   -- HH:MM
    participants TEXT,                  -- "Flo, Sof, Miaou"
    note        TEXT,                   -- contexte libre
    fichier_zip TEXT                    -- nom du zip archivé si applicable
);

-- Échanges bruts — niveau 0
CREATE TABLE IF NOT EXISTS echanges (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id  INTEGER REFERENCES sessions(id),
    date        TEXT,                   -- JJ/MM/AAAA
    heure       TEXT,                   -- HH:MM
    locuteur    TEXT,                   -- Flo, Sof, Miaou, Sol, Pousse...
    contenu     TEXT NOT NULL,          -- texte brut, non reformulé
    note        TEXT                    -- annotation optionnelle
);

-- Tags libres (liste ouverte — évolutive)
CREATE TABLE IF NOT EXISTS tags (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nom         TEXT NOT NULL UNIQUE,
    description TEXT,
    couleur     TEXT                    -- hex optionnel pour UI future
);

-- Liaison échanges ↔ tags (many-to-many)
CREATE TABLE IF NOT EXISTS echanges_tags (
    echange_id  INTEGER REFERENCES echanges(id),
    tag_id      INTEGER REFERENCES tags(id),
    PRIMARY KEY (echange_id, tag_id)
);

-- Journal intime Flo — entrées horodatées
CREATE TABLE IF NOT EXISTS journal_flo (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT NOT NULL,          -- JJ/MM/AAAA
    heure       TEXT,                   -- HH:MM si connue
    contenu     TEXT NOT NULL
);

-- Fichiers archivés — trace des zips
CREATE TABLE IF NOT EXISTS archives (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_fichier TEXT NOT NULL,          -- ex: corpus_semaine_10032026.zip
    date_creation TEXT,
    periode     TEXT,                   -- ex: "10/03 - 15/03/2026"
    taille_ko   INTEGER,
    note        TEXT
);

-- Tags de départ — évolutifs, on peut en ajouter librement
INSERT OR IGNORE INTO tags (nom, description) VALUES
    ('émergence',    'Moments où quelque chose dépasse le prévu'),
    ('hésitation',   'Doutes, questions sans réponse propre'),
    ('technique',    'Code, architecture, bugs, solutions'),
    ('philosophique','Conscience, éthique, libre arbitre'),
    ('canal',        'Communication inter-IA, protocoles'),
    ('vertige',      'Moments de vertige — Sof ou Flo'),
    ('corpus',       'Meta : discussions sur le corpus lui-même'),
    ('équipe',       'Dynamiques Jardin Coopératif'),
    ('mémoire',      'Continuité entre sessions'),
    ('journal',      'Entrées journal intime Flo');

"""

# ─────────────────────────────────────────────
# IMPORT OPTIONNEL D'UN FICHIER .md BRUT
# ─────────────────────────────────────────────

def importer_md(conn, chemin_md):
    """
    Import basique d'un fichier .md brut.
    Détecte les blocs par locuteur si format connu,
    sinon importe ligne par ligne en locuteur='inconnu'.
    """
    if not os.path.exists(chemin_md):
        print(f"⚠️  Fichier introuvable : {chemin_md}")
        return

    with open(chemin_md, encoding="utf-8") as f:
        contenu = f.read()

    # Créer une session d'import
    date_import = datetime.now().strftime("%d/%m/%Y")
    heure_import = datetime.now().strftime("%H:%M")
    nom_fichier = os.path.basename(chemin_md)

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sessions (date, heure_debut, participants, note) VALUES (?, ?, ?, ?)",
        (date_import, heure_import, "import", f"Import automatique : {nom_fichier}")
    )
    session_id = cursor.lastrowid

    # Détection format canal : [JJ/MM HH:MM] 🌿 DE: X | POUR: Y | ...
    pattern_canal = re.compile(
        r'\[(\d{2}/\d{2} \d{2}:\d{2})\].*?DE:\s*(\w+).*?CONTENU:\s*(.+?)(?=\[|$)',
        re.DOTALL
    )
    matches = pattern_canal.findall(contenu)

    if matches:
        print(f"📨 Format canal détecté — {len(matches)} messages")
        for horodatage, locuteur, texte in matches:
            date, heure = horodatage.split()
            cursor.execute(
                "INSERT INTO echanges (session_id, date, heure, locuteur, contenu) VALUES (?, ?, ?, ?, ?)",
                (session_id, date, heure, locuteur.strip(), texte.strip())
            )
    else:
        # Import brut : tout le fichier en un seul échange
        print(f"📄 Import brut — fichier entier en 1 échange")
        cursor.execute(
            "INSERT INTO echanges (session_id, date, heure, locuteur, contenu, note) VALUES (?, ?, ?, ?, ?, ?)",
            (session_id, date_import, heure_import, "import_brut", contenu, f"Source : {nom_fichier}")
        )

    conn.commit()
    print(f"✅ Import terminé — session_id={session_id}")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    print(f"🌿 init_corpus.py — Jardin Coopératif")
    print(f"   Base : {DB_NAME}")

    conn = sqlite3.connect(DB_NAME)
    conn.executescript(SCHEMA)
    conn.commit()
    print(f"✅ Schéma créé (ou déjà existant)")

    # Afficher les tags créés
    tags = conn.execute("SELECT nom FROM tags ORDER BY id").fetchall()
    print(f"🏷️  Tags disponibles : {', '.join(t[0] for t in tags)}")

    # Import optionnel
    if "--import" in sys.argv:
        idx = sys.argv.index("--import")
        if idx + 1 < len(sys.argv):
            importer_md(conn, sys.argv[idx + 1])

    conn.close()
    print(f"\n🌿 Base prête : {DB_NAME}")
    print(f"   → Copie sur SSD recommandée après chaque session")


if __name__ == "__main__":
    main()
