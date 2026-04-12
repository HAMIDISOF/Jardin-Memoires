"""
🌿 verifier_corpus.py — Jardin Coopératif
Affiche le contenu de corpus_these.db pour vérification.

Usage :
    py -3.11 verifier_corpus.py
    → affiche sessions, échanges, tags
"""

import sqlite3
import os

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "corpus_these.db")

def afficher():
    if not os.path.exists(DB):
        print(f"⚠️  BD introuvable : {DB}")
        return

    conn = sqlite3.connect(DB)

    print(f"\n🌿 verifier_corpus.py — {DB}\n")

    # Sessions
    sessions = conn.execute("SELECT * FROM sessions").fetchall()
    print(f"=== SESSIONS ({len(sessions)}) ===")
    for s in sessions:
        print(f"  id={s[0]} | date={s[1]} {s[2]} | participants={s[3]} | note={s[4]}")

    # Échanges
    echanges = conn.execute("SELECT id, session_id, date, heure, locuteur, substr(contenu,1,150) FROM echanges").fetchall()
    print(f"\n=== ÉCHANGES ({len(echanges)}) ===")
    for e in echanges:
        print(f"  id={e[0]} | session={e[1]} | {e[2]} {e[3]} | locuteur={e[4]}")
        print(f"  contenu (150c) : {e[5][:150]}")
        print()

    # Tags
    tags = conn.execute("SELECT nom, description FROM tags ORDER BY id").fetchall()
    print(f"=== TAGS ({len(tags)}) ===")
    for t in tags:
        print(f"  {t[0]} — {t[1]}")

    conn.close()
    print(f"\n🌿 Fin de la vérification")

if __name__ == "__main__":
    afficher()
