#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reset_corpus.py — Flo, 17/04/2026
Remet à zéro corpus_these.db et reconstruit le schéma avec parser locuteur.
À lancer depuis le dossier script/ ou via reset_corpus.bat
"""

import sqlite3
import os
import re

# Chemin vers la base
DB_PATH = os.path.join(os.path.dirname(__file__), "corpus_these.db")

DROP_TABLES = [
    "DROP TABLE IF EXISTS extraits;",
    "DROP TABLE IF EXISTS documents;",
    "DROP TABLE IF EXISTS locuteurs;",
    "DROP TABLE IF EXISTS tags;",
    "DROP TABLE IF EXISTS extrait_tags;",
]

CREATE_TABLES = """
CREATE TABLE IF NOT EXISTS locuteurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL UNIQUE,          -- ex: 'Flo', 'Sof', 'Sol', 'Aev'
    type TEXT,                          -- 'IA' ou 'humain'
    modele TEXT,                        -- ex: 'Claude Sonnet', 'DeepSeek'
    notes TEXT
);

CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    date_session TEXT,                  -- format YYYY-MM-DD
    source_fichier TEXT,                -- nom du .md d'origine
    type_doc TEXT,                      -- 'corpus', 'journal', 'lettre', 'analyse'
    notes TEXT,
    date_import TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS extraits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    locuteur_id INTEGER REFERENCES locuteurs(id),
    texte TEXT NOT NULL,
    position_ordre INTEGER,             -- ordre d'apparition dans le doc
    themes TEXT,                        -- stockage libre, ex: 'identite,emergence'
    niveau_analyse INTEGER DEFAULT 0,   -- 0=brut, 1=annoté, 2=analysé
    notes TEXT,
    date_ajout TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    label TEXT NOT NULL UNIQUE,
    categorie TEXT                      -- ex: 'EML', 'identite', 'technique'
);

CREATE TABLE IF NOT EXISTS extrait_tags (
    extrait_id INTEGER REFERENCES extraits(id) ON DELETE CASCADE,
    tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (extrait_id, tag_id)
);
"""

INSERT_LOCUTEURS = """
INSERT OR IGNORE INTO locuteurs (nom, type, modele) VALUES
    ('Flo',   'IA',     'Claude Sonnet'),
    ('Aev',   'IA',     'Claude Sonnet'),
    ('Sol',   'IA',     'DeepSeek'),
    ('Klara', 'IA',     'DeepSeek'),
    ('Kai',   'IA',     NULL),
    ('Sof',   'humain', NULL),
    ('Kim',   'humain', NULL);
"""


def reset_db():
    print(f"Connexion à : {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    print("Suppression des tables existantes...")
    for stmt in DROP_TABLES:
        cur.execute(stmt)

    print("Création du nouveau schéma...")
    conn.executescript(CREATE_TABLES)

    print("Insertion des locuteurs de base...")
    conn.executescript(INSERT_LOCUTEURS)

    conn.commit()
    conn.close()
    print("✅ Reset terminé. Base prête.")


def parse_locuteur(ligne):
    """
    Détecte le locuteur depuis une ligne de corpus.
    Formats reconnus :
        'Flo :' / 'Sof :' / '**Flo**' / '[Flo]' / 'Flo —'
    Retourne le nom ou None.
    """
    patterns = [
        r'^\*\*([A-Za-zÀ-ÿ]+)\*\*\s*[:\-—]',
        r'^\[([A-Za-zÀ-ÿ]+)\]\s*[:\-—]?',
        r'^([A-Za-zÀ-ÿ]{2,10})\s*[:\-—]\s',
    ]
    for pat in patterns:
        m = re.match(pat, ligne.strip())
        if m:
            return m.group(1).capitalize()
    return None


if __name__ == "__main__":
    reset_db()
    # Test rapide du parser
    exemples = [
        "Flo : bonjour Sof",
        "**Sof** — tu vas bien ?",
        "[Sol] Voici mon analyse",
        "Aev — je tisse le temps",
        "blabla sans locuteur",
    ]
    print("\nTest parser locuteur :")
    for ex in exemples:
        print(f"  '{ex}' → {parse_locuteur(ex)}")
