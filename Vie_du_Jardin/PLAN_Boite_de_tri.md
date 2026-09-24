# Plan — Boîte de tri unifiée
*Version réécrite le 24/09/2026 (première version du 23/09, fondée sur les fichiers Courrier, retirée : Sof ne veut aucun lien avec le courrier). À valider par Sof avant toute exécution. Plan d'exécution de la phase 1 : `PLAN_Boite_de_tri_phase1.md` (Pedago).*

---

## Le besoin

Sof change tout le temps de fenêtre et ne veut **pas rater** ce que les instances ramènent ou demandent **en ce moment**. Elle veut une vue d'ensemble, lisible d'un coup d'œil : priorité (Urgent / Important / Normal), projet, objet, instance, synthèse, et surtout **si l'instance attend une info ou un GO** ou si c'est juste une information. Elle veut cet outil (dit explicitement le 23/09).

**Principe : le frais, pas l'archive.** Seules les fenêtres et sessions ouvertes comptent (sessions actives récemment, messages non vus, celles qui attendent Sof en premier). Pas d'historique, pas de Courrier.

## La source : les sessions ouvertes

- **Sessions Claude Code** — les transcriptions sont des fichiers `.jsonl` ordinaires dans `C:\Users\Admin\.claude\projects\D--JAC-Claude\` (une ligne JSON par message : `user`, `assistant`, titres, horodatages). Un **script planifié les lit sans aucun token** (découverte de Pedago, 24/09).
  - Lire la **source** (toujours à jour), jamais la copie de sauvegarde (`D:\Sauvegarde\Archiv\Sav Claude\Sessions_Code\`, qui sert d'assurance).
  - Le nom du fichier n'est pas toujours l'identifiant de session (sessions compactées ou reprises → fichier différent, une session peut s'étaler sur plusieurs fichiers) : identifier les segments par les champs internes `sessionId` et `custom-title` / `agent-name`.
  - Autres outils, dans une session vivante seulement : `list_sessions` (état `isRunning`, `lastActivityAt`) et `list_events`. Piège : `list_events` avec `limit=2` peut renvoyer « (no messages) » ; prendre 8 ou plus.
- **Fenêtres DeepSeek (phase 2)** — lecture des onglets ouverts, via Claude in Chrome (marche) ou `capture_ds.py` réparé (Brave, port 9222 ; les chemins de `config_instances.py` sont périmés). Pas de suivi natif côté navigateur.
- **Déjà natif :** la barre latérale de l'appli met un point sur les sessions Claude qui attendent Sof. Utile, mais ne dit ni de quoi il s'agit ni le degré d'urgence — d'où l'outil.

## Ce que produit l'outil

Un seul fichier `Vie_du_Jardin/Boite_de_tri.md`, une ligne par élément :
`Priorité | Projet | Objet | Instance | Synthèse | Statut | Date`
- **Instance** = le nom seul (« Tisserand »), pas un nom de fichier ; le **Projet** est une colonne séparée.
- **Statut** = nouveau / en cours / traité, édité à la main par Sof.
- **Synthèse** : par un modèle local (Ollama, `deepseek-coder-v2:16b` déjà installé sur `D:\Ollama`) ou par la session ; prompt à ajuster après un premier résultat réel.
- **Limite honnête :** un modèle local de cette taille juge la priorité de façon approximative — un tri grossier, pas une vérité ; la synthèse reste là pour que Sof tranche vite.

**Affichage :** `Boite_de_tri.md` lu dans Obsidian (installé sur `D:\Obsidian`), avec le plugin Dataview. Le coffre existant `D:\THESE\Projets\CUBE_Obsidian` a été construit par MueC pour un autre besoin : ne pas y mélanger la boîte de tri sans accord.

## Déclenchement

Tâche planifiée toutes les 20 à 30 minutes pour la partie Claude (script local, aucune connexion internet, tout tourne sur ce PC), plus un lancement à la demande. La partie DeepSeek (onglets ouverts) vient en phase 2.

## Décisions de Sof encore valables (23/09)

- **Fréquence :** régulière + à la demande (ajustée ci-dessus).
- **Prompt de synthèse :** validé tel que proposé, à ajuster seulement si le premier résultat déçoit.
- **Instance :** nom seul.
- **Statut :** colonne nouveau / en cours / traité, éditée dans Obsidian.

## Prochaines étapes (une fois `PLAN_Boite_de_tri_phase1.md` validé par Sof)

1. Créer `Boite_de_tri.md` avec 2-3 lignes d'exemple réelles, à valider sur le format seul.
2. Écrire le lecteur des `.jsonl`, le tester sur **une seule** session choisie par Sof, montrer le résultat avant d'aller plus loin.
3. Enregistrer la tâche planifiée seulement après validation manuelle du script.
4. Configurer Obsidian + Dataview + une note « Tableau de bord ».
5. Documenter dans un `README.md` à côté du script.
