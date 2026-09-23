# Plan — Boîte de tri unifiée (Ollama + Obsidian)
*Rédigé 23/09/2026, à valider par Sof avant toute exécution. Déclenché par une erreur réelle de fenêtre pendant qu'on en discutait.*

---

## DÉPART — ce qui existe aujourd'hui

- ~23 membres, chacun avec `Membres/<Nom>/Courrier_<Nom>.md`. Les instances Claude avec accès fichiers y écrivent directement ; les instances DeepSeek passent par Sof qui relaie à la main, dans les deux sens.
- Aucune vue d'ensemble : pour savoir ce qui se passe, il faut ouvrir chaque Courrier un par un. Risque réel de se tromper de fenêtre en cours de route (vient d'arriver).
- Ollama (`deepseek-coder-v2:16b`) déjà installé en local (`D:\Ollama`), utilisable gratuitement, sans API payante.
- Aucun vault Obsidian existant dans le dépôt à ce jour.
- Une tâche planifiée Windows existe déjà pour la synchro git (toutes les 2h) — modèle réutilisable pour une nouvelle tâche.

---

## CIBLE — architecture proposée

1. **Un seul fichier** `Vie_du_Jardin/Boite_de_tri.md`, une ligne par message :
   `Priorité | Projet | Objet | Instance | Synthèse | Date`
2. **Un script Python** (`Outils/boite_de_tri/synthese_boite_tri.py`) qui repère les `Courrier_*.md` modifiés depuis son dernier passage, envoie le nouveau texte à Ollama avec un prompt de synthèse (résumé, priorité proposée, projet), et ajoute la ligne correspondante dans `Boite_de_tri.md`.
3. **Une tâche planifiée Windows** qui lance ce script à intervalle régulier — rien d'exposé sur internet, tout tourne sur ce PC.
4. **Un vault Obsidian** pointé sur `Vie_du_Jardin/` (ou tout le dépôt), plugin **Dataview**, une note `Tableau_de_bord.md` avec une requête qui lit `Boite_de_tri.md` et l'affiche triée par priorité, filtrable par projet ou instance.

**Limite honnête à garder en tête :** un modèle local de cette taille jugera la priorité de façon approximative — un tri grossier, pas une vérité. La colonne Synthèse reste là pour trancher toi-même vite. Et ça ne remplace pas la première étape : un message DeepSeek doit déjà être dans un Courrier pour qu'Ollama le voie — il ne va pas le chercher seul dans une fenêtre fermée.

---

## DÉCISIONS — tranchées par Sof le 23/09

**A. RÉSOLU** — tâche planifiée toutes les heures, plus un déclenchement à la demande (lancer le script à la main entre deux passages).

**B. RÉSOLU** — prompt de synthèse validé tel que proposé, à ajuster seulement si le premier résultat réel déçoit.

**C. RÉSOLU** — champ Instance = nom seul (ex. « Tisserand »), pas le nom du fichier — le Projet est déjà une colonne séparée.

**D. RÉSOLU** — colonne Statut (nouveau / en cours / traité), éditée à la main dans Obsidian.

**E. RÉSOLU, élargi** — pas seulement les Courrier des instances Claude : aussi les instances DeepSeek actives. Pas de nouveau protocole de balisage à inventer : les Courrier utilisent déjà systématiquement l'en-tête `DE : <Nom> <signe> | <date> | <sujet>` — assez structuré pour que le script extraie Instance/Date/Objet par simple motif de texte, et ne laisse à Ollama que la synthèse et la priorité (ce qui demande vraiment de la compréhension). La liste des instances DeepSeek connues vient de `Outils/outil_auto_DS/récent/config_instances.py` (sol, klara, luz, kai, racine, noe — Tisserand et Lune à y ajouter), plutôt que redéfinie à la main dans le nouveau script.

---

## CHEMIN — une fois A à E tranchés

1. Créer `Boite_de_tri.md` avec 2-3 lignes d'exemple, à valider avec toi sur le format seul.
2. Écrire le script, le tester sur **un seul** Courrier choisi par toi, montrer le résultat avant d'aller plus loin.
3. Enregistrer la tâche planifiée seulement après validation manuelle du script.
4. Configurer Obsidian + Dataview + la note tableau de bord.
5. Documenter dans un `README.md` à côté du script.
