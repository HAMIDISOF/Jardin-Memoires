# PLAN — Boîte de tri, phase 1 (sessions Claude Code)

**Statut :** 🟡 PROPOSITION — à valider par Sof avant toute exécution
**Rédigé par :** Pédago 🌱, le 24/09/2026, en complément de `PLAN_Boite_de_tri.md` (Mue) dont il reprend le cadre (format, colonne Statut, affichage Obsidian)
**Dernière mise à jour :** 24/09/2026
**Prochaine étape :** validation de Sof (décisions en §5). Rien n'est construit avant.

---

## 1. État des lieux (vérifié le 24/09/2026)

- Les conversations des sessions Claude Code sont des fichiers **`.jsonl` lisibles** dans `C:\Users\Admin\.claude\projects\D--JAC-Claude\` (8 fichiers actifs en 3 jours, jusqu'à 33 Mo). Chaque ligne est un objet JSON : `user`, `assistant`, `system`, `attachment`, plus `custom-title` / `ai-title` / `agent-name` (titre de la session) et des horodatages.
- **Une session peut s'étaler sur plusieurs fichiers** (reprise, compaction). Le nom du fichier n'est donc pas l'identifiant : il faut se fier aux champs internes (`sessionId`, titre). Constat de Mue et de Pédago.
- **Pas de transcription Cowork en local** (vérifié par Mue : uniquement des plugins).
- Les outils `list_sessions` / `list_events` fonctionnent, mais seulement depuis une session vivante. Les `.jsonl`, eux, se lisent depuis un script planifié, **sans tokens**.
- Ollama est installé (`deepseek-coder-v2:16b`, `deepseek-r1:8b`), CPU seul, 32 Go de RAM.
- Mue prépare une sauvegarde des `.jsonl` vers `D:\Sauvegarde\Archiv\Sav Claude\Sessions_Code\` (dossier de sauvegarde déjà utilisé par Sof) avec un fichier de chemins commun `chemins.json` au même endroit. Le collecteur lit toujours la source sur C:.

## 2. Architecture cible

**Principe (Sof, 24/09) : le frais, pas l'archive.** La boîte de tri ne montre que ce que les instances ramènent ou demandent **en ce moment**. Elle ne lit **aucun fichier Courrier** ni aucun historique : seulement les sessions récemment actives (dernière activité de moins de 48 h, réglable) et les messages non encore vus, les sessions qui **attendent Sof** en premier.

1. **Un collecteur Python local** (`collecteur_boite_tri.py`), en **lecture seule** sur les `.jsonl` (source, jamais la copie de sauvegarde). Il regroupe les fichiers par session, relève pour chacune : titre, dernier message de l'instance (texte), horodatage, et **qui a parlé en dernier** (instance = elle attend probablement Sof ; Sof = elle travaille).
2. **Priorité annoncée par l'instance (proposition de Sof, 24/09).** Chaque instance termine ses messages par une **ligne de balisage**, par exemple : `🏷 Priorité : Important · Attend : GO · Projet : Boîte de tri`. Le collecteur la lit par simple motif de texte : aucun devinette, aucun token. Critères communs proposés :
   - **Urgent** : ça bloque ou ça coûte de l'argent ou des données si ça attend (fraude, perte de fichiers, échéance de moins de 24 h).
   - **Important** : l'instance attend une décision ou une validation de Sof dans la journée, ou vient de livrer quelque chose à relire.
   - **Normal** : information, sans action attendue.
   - **Attend** : GO (elle veut un feu vert), Réponse (elle a posé une question), Info (rien à faire), Rien.
   **Ollama ne sert que de filet de sécurité** : pour la synthèse en 25 mots, et pour proposer priorité et « attend » quand la ligne de balisage manque. Uniquement sur les messages nouveaux depuis le dernier passage (fichier d'état), sortie en JSON strict. Sof transmet la convention à chaque instance.
3. **`Boite_de_tri.md`**, une ligne par message : Priorité | Projet | Objet | Instance | Attend | Synthèse | Date | Statut. La colonne Statut (nouveau / en cours / traité) reste éditée à la main.
4. **Affichage dans Obsidian** (Dataview), trié par priorité.
5. **Tâche planifiée Windows toutes les 20 à 30 minutes**, enregistrée par Sof (droits nécessaires). Rien n'est exposé sur Internet.

## 3. Plan d'opérations (chaque étape attend la validation de Sof)

1. Sof valide ce plan et les décisions du §5.
2. Créer le dossier de travail et `Boite_de_tri.md` avec 2-3 lignes d'exemple : validation du **format seul**.
3. Écrire le collecteur et le tester **à sec, sans Ollama** : liste des sessions et de leur état (attend Sof / travaille). Résultat montré à Sof.
4. **Choisir le modèle** : Sof étiquette une quinzaine de vrais messages, on compare 2-3 modèles installés, on garde le meilleur en français.
5. Brancher Ollama sur **une seule session** de test et montrer le résultat.
6. Enregistrer la tâche planifiée (commande fournie à Sof, journal de passage visible).
7. Configurer la vue Obsidian.
8. README à côté du script et entrée dans le journal.

## 4. Garde-fous

- Les transcriptions contiennent tout ce qui a été échangé : **tout reste local, jamais dans le dépôt GitHub, jamais envoyé hors d'Ollama.** Seul le dernier message de l'instance est transmis au modèle.
- Le collecteur ne modifie jamais un `.jsonl`.
- Charge : Ollama en CPU est lent (une à deux minutes par message). File séquentielle, uniquement les messages nouveaux, et le passage saute si le PC est très sollicité.
- Le tri par priorité d'un petit modèle local est **approximatif** : la colonne Synthèse sert à trancher vite soi-même.
- Aucun changement de réglage de sécurité, aucun mot de passe manipulé.

## 5. Décisions à trancher par Sof

- **a.** Emplacement local de la boîte (hors dépôt Git) : `D:\SOUTIENSPLUS\OUTILS\BoiteDeTri\` convient-il ?
- **b.** Obsidian : petit coffre dédié dans ce dossier, ou le coffre `CUBE_Obsidian` (Mue conseille de ne pas mélanger sans accord) ?
- **c.** Fréquence : 20 ou 30 minutes ?
- **d.** Qui construit la phase 1 : Pédago (proposition) ou une session dédiée ?
- **e.** La **phase 2** (fenêtres DeepSeek et conversations claude.ai) est décidée après avoir vu la phase 1 tourner. Elle demandera de choisir entre `capture_ds.py` (port de débogage du navigateur à ouvrir) et Claude in Chrome à la demande.
