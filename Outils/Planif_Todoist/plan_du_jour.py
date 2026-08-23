"""
Plan du jour — lit tes tâches Todoist et propose une sélection pour aujourd'hui,
selon tes règles personnelles (jours autorisés par catégorie, quota par priorité,
durée opératoire). Ce script ne modifie JAMAIS rien dans Todoist : il ne fait que
lire, calculer, et afficher un plan à l'écran (et le sauvegarder en fichier texte).

Installation (une seule fois) :
    pip install requests

Avant de lancer, définis ton token API comme variable d'environnement
(ne JAMAIS l'écrire en clair dans ce fichier) :

    Windows (cmd)          :  set TODOIST_API_TOKEN=colle_ton_token_ici
    Windows (PowerShell)   :  $env:TODOIST_API_TOKEN = "colle_ton_token_ici"
    Mac/Linux              :  export TODOIST_API_TOKEN="colle_ton_token_ici"

Puis lance :
    python plan_du_jour.py
"""

import os
import sys
import re
import datetime
import requests

API_BASE = "https://api.todoist.com/api/v1"


# ----------------------------------------------------------------------------
# Configuration de tes règles — modifie cette section librement, c'est ici que
# vit toute la logique que Todoist ne sait pas faire nativement.
# ----------------------------------------------------------------------------

CONFIG = {
    "categories": {
        # nom EXACT du projet Todoist -> règles de la catégorie
        # structure à 4 catégories, alignée sur le vrai Todoist de Sof (23/08/2026)
        "Études & Formations": {"jours": [0, 1, 2, 3, 4, 5, 6], "duree_heures": 1},    # Bouddhisme, MTC/Qi Gong, Philo — très varié, tous les jours possibles
        "Travail":             {"jours": [0, 1, 2, 3, 4], "duree_heures": 1},         # Soutienplus, Genially, Tutorat (5 élèves)
        "Maison":               {"jours": [0, 1, 2, 3, 4], "duree_heures": 1.5},      # courses, ménage, administratif, cuisine, rangements
        "Vie quotidienne":      {"jours": [0, 1, 2, 3, 4, 5, 6], "duree_heures": 1},  # temps enfants, bien-être/sport, asso/amis
    },
    # combien de tâches max par niveau de priorité aujourd'hui
    "regle": {
        "max_p1": 1,
        "max_p2": 1,
        "max_p3": 1,
        "max_p4": 0,  # 0 = on n'inclut pas les tâches "normales" dans le plan auto
    },
}

# Rappel du piège de l'API Todoist : le champ "priority" est inversé par
# rapport à ce que tu vois dans l'appli. P1 (le plus urgent, affiché en haut)
# vaut 4 côté API ; P4 (normal) vaut 1. On mappe ça une fois pour toutes ici.
API_PRIORITY_TO_LABEL = {4: "P1", 3: "P2", 2: "P3", 1: "P4"}
LABEL_TO_MAX_KEY = {"P1": "max_p1", "P2": "max_p2", "P3": "max_p3", "P4": "max_p4"}

# Recherche insensible à la casse/aux espaces, pour éviter qu'une différence de
# capitalisation entre CONFIG et le vrai nom du projet Todoist fasse ignorer
# silencieusement toute une catégorie.
_CATEGORIES_NORMALISEES = {
    nom.strip().lower(): regles for nom, regles in CONFIG["categories"].items()
}


def get_cat_rule(project_name):
    return _CATEGORIES_NORMALISEES.get((project_name or "").strip().lower())

JOURS_FR = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

FENETRE_PATTERN = re.compile(r"FENETRE:(\d{1,2})-(\d{1,2})")


def parse_fenetre(description):
    """Cherche 'FENETRE:28-15' dans la description d'une tâche.
    Renvoie (jour_debut, jour_fin) ou None si absent."""
    if not description:
        return None
    m = FENETRE_PATTERN.search(description)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def dans_la_fenetre(jour_du_mois, jour_debut, jour_fin):
    """Gère aussi les fenêtres qui chevauchent la fin du mois,
    ex. 28-15 = du 28 du mois courant au 15 du mois suivant."""
    if jour_debut <= jour_fin:
        return jour_debut <= jour_du_mois <= jour_fin
    return jour_du_mois >= jour_debut or jour_du_mois <= jour_fin


# ----------------------------------------------------------------------------
# Appels API
# ----------------------------------------------------------------------------

def get_token():
    token = os.environ.get("TODOIST_API_TOKEN")
    if not token:
        sys.exit(
            "Erreur : la variable d'environnement TODOIST_API_TOKEN n'est pas définie.\n"
            "Regarde les instructions en haut de ce fichier pour savoir comment la poser."
        )
    return token


def api_get_all(path, token, params=None):
    """Récupère toutes les pages d'une ressource (l'API v1 pagine avec next_cursor)."""
    headers = {"Authorization": f"Bearer {token}"}
    results = []
    cursor = None
    params = dict(params or {})
    while True:
        if cursor:
            params["cursor"] = cursor
        resp = requests.get(f"{API_BASE}/{path}", headers=headers, params=params, timeout=15)
        if resp.status_code == 401:
            sys.exit("Erreur : token invalide ou expiré (401 Unauthorized). Vérifie TODOIST_API_TOKEN.")
        resp.raise_for_status()
        data = resp.json()
        page = data.get("results", data) if isinstance(data, dict) else data
        results.extend(page)
        cursor = data.get("next_cursor") if isinstance(data, dict) else None
        if not cursor:
            break
    return results


# ----------------------------------------------------------------------------
# Logique du plan du jour
# ----------------------------------------------------------------------------

def build_plan():
    token = get_token()

    projects = api_get_all("projects", token)
    project_by_id = {p["id"]: p["name"] for p in projects}

    tasks = api_get_all("tasks", token)

    today = datetime.date.today()
    weekday = today.weekday()  # 0 = lundi
    jour_du_mois = today.day

    # Étape 1 : à part, on repère les tâches "en cours" — affichées mais jamais
    # comptées dans le quota du jour, juste pour ne pas les perdre de vue.
    en_cours = []
    for t in tasks:
        labels = t.get("labels") or []
        if "en_cours" in labels and "bloque" not in labels:
            project_name = project_by_id.get(t.get("project_id"), "Sans catégorie")
            en_cours.append((t, project_name))

    # Étape 2 : ne garder pour le plan auto que les tâches "à faire" = pas
    # bloquées, pas déjà en cours (elles ont leur propre section ci-dessus).
    eligibles = []
    for t in tasks:
        labels = t.get("labels") or []
        if "bloque" in labels or "en_cours" in labels:
            continue
        project_name = project_by_id.get(t.get("project_id"), "Sans catégorie")

        fenetre = parse_fenetre(t.get("description"))
        if fenetre:
            jour_debut, jour_fin = fenetre
            if not dans_la_fenetre(jour_du_mois, jour_debut, jour_fin):
                continue
        else:
            cat_rule = get_cat_rule(project_name)
            if cat_rule is None:
                continue  # catégorie inconnue de la config : on l'ignore pour le plan auto
            if weekday not in cat_rule["jours"]:
                continue  # cette catégorie n'est pas autorisée aujourd'hui

        cat_rule = get_cat_rule(project_name) or {"duree_heures": 1}
        eligibles.append((t, project_name, cat_rule))

    # Étape 3 : grouper par priorité (avec le mapping inversé de l'API)
    par_priorite = {"P1": [], "P2": [], "P3": [], "P4": []}
    for t, project_name, cat_rule in eligibles:
        label = API_PRIORITY_TO_LABEL.get(t.get("priority", 1), "P4")
        par_priorite[label].append((t, project_name, cat_rule))

    def due_key(item):
        t = item[0]
        due = t.get("due")
        return due["date"] if due and due.get("date") else "9999-99-99"

    plan = {}
    total_heures = 0.0
    for label in ["P1", "P2", "P3", "P4"]:
        max_key = LABEL_TO_MAX_KEY[label]
        max_n = CONFIG["regle"][max_key]
        candidats = sorted(par_priorite[label], key=due_key)
        choisis = candidats[:max_n]
        plan[label] = choisis
        for t, project_name, cat_rule in choisis:
            total_heures += cat_rule["duree_heures"]

    return plan, en_cours, total_heures, today, weekday


def format_plan(plan, en_cours, total_heures, today, weekday):
    lignes = []
    lignes.append(f"=== Plan du jour — {JOURS_FR[weekday]} {today.strftime('%d/%m/%Y')} ===")
    lignes.append(f"Charge estimée : {total_heures} h\n")

    if en_cours:
        lignes.append("--- En cours (déjà entamées, non comptées dans le quota) ---")
        for t, project_name in en_cours:
            lignes.append(f"  • {t['content']}  [{project_name}]")
        lignes.append("")

    vide = True
    for label in ["P1", "P2", "P3", "P4"]:
        items = plan[label]
        if not items:
            continue
        vide = False
        lignes.append(f"--- {label} ---")
        for t, project_name, cat_rule in items:
            due = t.get("due")
            echeance = f" (échéance : {due['date']})" if due and due.get("date") else ""
            lignes.append(f"  • {t['content']}  [{project_name}, ~{cat_rule['duree_heures']}h]{echeance}")
        lignes.append("")

    if vide:
        lignes.append("Aucune tâche éligible aujourd'hui selon tes règles actuelles.")

    return "\n".join(lignes)


if __name__ == "__main__":
    plan, en_cours, total_heures, today, weekday = build_plan()
    texte = format_plan(plan, en_cours, total_heures, today, weekday)
    print(texte)

    with open("plan_du_jour.txt", "w", encoding="utf-8") as f:
        f.write(texte)
