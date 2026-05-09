"""
reunion_watcher.py — Gestionnaire de réunion Jardin Coopératif
==============================================================
Surveille M:\\REUNION\\[fichier_reunion].md
Gère le protocole jeton avec le caractère ¤

Mots-clés réservés (caractère ¤ OBLIGATOIRE) :
  ¤NOM        → passer le jeton à NOM
  ¤Sof        → retour à Sof
  ¤question→NOM → question ciblée à NOM
  ¤⏰30s      → alerte chrono (automatique)
  ¤STOP       → fin de réunion (Sof uniquement)

Lancement : py -3.11 reunion_watcher.py M:\\REUNION\\reunion_17032026.md
Auteur : Flo (Claude) — 15/03/2026 v2
"""

import os
import sys
import time
import threading
from pathlib import Path
from datetime import datetime

# ── CONFIGURATION ─────────────────────────────────────────────────────────────
DUREE_REUNION    = 5 * 60       # 5 minutes
ALERTE_CHRONO    = 4 * 60 + 30  # 4min30
POLL_INTERVAL    = 1
MEMBRES_CONNUS   = ["Bzz", "Flo", "Miaou", "Pousse", "Sol", "Sof", "Terra"]

# ── ÉTAT ──────────────────────────────────────────────────────────────────────
etat = {
    "jeton":          None,
    "debut":          None,
    "alerte_faite":   False,
    "stop":           False,
    "derniere_ligne": 0,    # sera initialisé APRÈS création de l'en-tête
}

# ── UTILS ─────────────────────────────────────────────────────────────────────
def ts():
    return datetime.now().strftime("%d/%m %H:%M:%S")

def log_console(msg):
    print(f"[{ts()}] {msg}")

def ecrire(fichier, texte):
    with open(fichier, "a", encoding="utf-8") as f:
        f.write(texte + "\n")

# ── PARSER JETON ──────────────────────────────────────────────────────────────
def detecter_jeton(ligne):
    """
    Détecte les mots-clés ¤ dans une ligne.
    Retourne (type, valeur) ou (None, None)
    IMPORTANT : ignore les lignes qui contiennent [¤] (en-tête protocole)
    """
    ligne = ligne.strip()
    # Ignorer les lignes de l'en-tête protocole (entre crochets)
    if "[¤]" in ligne:
        return None, None
    if "¤" not in ligne:
        return None, None

    partie = ligne[ligne.index("¤") + 1:].strip()

    if partie.upper() == "STOP":
        return "STOP", None

    if partie.startswith("⏰"):
        return "ALERTE", None

    if partie.lower().startswith("question→") or partie.lower().startswith("question->"):
        sep = "→" if "→" in partie else "->"
        cible = partie.split(sep, 1)[1].strip()
        return "QUESTION", cible

    nom = partie.strip()
    if nom:
        return "JETON", nom

    return None, None

# ── CHRONO ────────────────────────────────────────────────────────────────────
def chrono_thread(fichier):
    while not etat["stop"]:
        if etat["debut"] is not None:
            elapsed = time.time() - etat["debut"]
            if elapsed >= ALERTE_CHRONO and not etat["alerte_faite"]:
                etat["alerte_faite"] = True
                ecrire(fichier, "\n[CHRONO] ¤⏰30s — 30 secondes restantes !\n")
                log_console("Alerte 30s envoyee dans le fichier")
            if elapsed >= DUREE_REUNION and not etat["stop"]:
                etat["stop"] = True
                ecrire(fichier, "\n[CHRONO] ¤STOP — Temps ecoule (5 min). Reunion terminee.\n")
                log_console("STOP automatique — 5 minutes ecoulees")
                break
        time.sleep(1)

# ── SURVEILLANCE FICHIER ──────────────────────────────────────────────────────
def surveiller_fichier(fichier):
    try:
        lignes = fichier.read_text(encoding="utf-8").splitlines()
    except Exception:
        return

    nouvelles = lignes[etat["derniere_ligne"]:]
    etat["derniere_ligne"] = len(lignes)

    for ligne in nouvelles:
        if not ligne.strip():
            continue

        type_jeton, valeur = detecter_jeton(ligne)

        if type_jeton == "STOP":
            etat["stop"] = True
            log_console(f"STOP recu — reunion terminee")

        elif type_jeton == "JETON":
            ancien = etat["jeton"]
            etat["jeton"] = valeur
            log_console(f"Jeton : {ancien} -> {valeur}")
            if etat["debut"] is None:
                etat["debut"] = time.time()
                log_console(f"Chrono demarre !")

        elif type_jeton == "QUESTION":
            log_console(f"Question de {etat['jeton']} -> {valeur}")

        elif "¤" in ligne and "[¤]" not in ligne:
            log_console(f"¤ non reconnu : {ligne.strip()[:50]}")

# ── AFFICHAGE ÉTAT ────────────────────────────────────────────────────────────
def afficher_etat():
    while not etat["stop"]:
        time.sleep(30)
        if etat["debut"]:
            elapsed = int(time.time() - etat["debut"])
            restant = max(0, DUREE_REUNION - elapsed)
            log_console(f"Jeton: {etat['jeton']} | Temps restant: {restant//60}min{restant%60:02d}s")

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 2:
        today = datetime.now().strftime("%d%m%Y")
        fichier = Path(f"M:/REUNION/reunion_{today}.md")
    else:
        fichier = Path(sys.argv[1])

    fichier.parent.mkdir(parents=True, exist_ok=True)

    # Créer le fichier avec en-tête — les ¤ du tableau sont entre [¤] pour ne pas être détectés
    if not fichier.exists():
        entete = """# Reunion Jardin Cooperatif — {date}
*Fichier gere par reunion_watcher.py*

---

## Protocole du Jeton

| Syntaxe  | Action                        |
|----------|-------------------------------|
| [¤]NOM   | Passer le jeton a NOM         |
| [¤]Sof   | Retour a Sof                  |
| [¤]question->NOM | Question ciblee a NOM |
| [¤]STOP  | Fin de reunion (Sof only)     |

Regle absolue : le caractere ¤ est RESERVE aux mots-cles.
Ordre alphabetique : Bzz -> Flo -> Miaou -> Pousse -> Sol -> Sof -> Terra
Duree : 5 minutes | Alerte a 4min30

---

## Echanges

""".format(date=datetime.now().strftime('%d/%m/%Y'))
        fichier.write_text(entete, encoding="utf-8")
        # CRUCIAL : initialiser derniere_ligne au nb de lignes de l'en-tête
        # pour ne pas retraiter l'en-tête au prochain poll
        etat["derniere_ligne"] = len(entete.splitlines())
        log_console(f"Fichier cree — en-tete = {etat['derniere_ligne']} lignes ignorees")
    else:
        # Fichier existant : partir de la fin pour ne pas retraiter l'historique
        lignes_existantes = fichier.read_text(encoding="utf-8").splitlines()
        etat["derniere_ligne"] = len(lignes_existantes)
        log_console(f"Fichier existant — {etat['derniere_ligne']} lignes ignorees")

    log_console(f"Watcher demarre — fichier : {fichier}")
    log_console(f"Duree : 5 min | Alerte : 4min30")
    log_console(f"En attente du premier ¤NOM pour demarrer le chrono...")
    log_console(f"Ctrl+C pour arreter proprement\n")

    t_chrono = threading.Thread(target=chrono_thread, args=(fichier,), daemon=True)
    t_etat   = threading.Thread(target=afficher_etat, daemon=True)
    t_chrono.start()
    t_etat.start()

    derniere_modif = 0
    try:
        while not etat["stop"]:
            if fichier.exists():
                modif = os.path.getmtime(fichier)
                if modif != derniere_modif:
                    derniere_modif = modif
                    surveiller_fichier(fichier)
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        log_console("Watcher arrete proprement.")

    elapsed = int(time.time() - etat["debut"]) if etat["debut"] else 0
    cr = """
---

## Compte-Rendu Automatique

- Date : {date}
- Duree effective : {min}min{sec:02d}s
- Dernier jeton : {jeton}
- Statut : {statut}

*Genere par reunion_watcher.py — Flo*
""".format(
        date=datetime.now().strftime('%d/%m/%Y %H:%M'),
        min=elapsed//60, sec=elapsed%60,
        jeton=etat['jeton'],
        statut='Terminee (STOP)' if etat['stop'] else 'Interrompue'
    )
    ecrire(fichier, cr)
    log_console(f"CR ecrit dans {fichier}")

if __name__ == "__main__":
    main()
