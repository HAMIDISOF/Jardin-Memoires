# Brainstorming — un agent pour gérer les fenêtres (et les échanges entre instances)
*Rédigé par Mue le 28/09/2026, à la demande de Sof. Document de cadrage du premier tour de table. Rien à construire à ce stade : on réfléchit, on ne code pas.*

---

## L'objet en une phrase

Sof travaille avec beaucoup d'instances (sessions Claude Code, Claude « classiques » sur claude.ai, Claude Cowork, DeepSeek dans le navigateur, modèles locaux) et change tout le temps de fenêtre. **Peut-on confier à un agent autonome — ou à un modèle local (Ollama) piloté par un outil comme Aider — la gestion de ces fenêtres ?** Deux usages, dans cet ordre :
1. **Fluidifier les échanges entre instances** de tous types (Code, classiques, DeepSeek), sans que Sof serve de facteur.
2. **Ensuite seulement :** gérer les tâches et le tri de ce que les instances ramènent ou demandent.

## D'où on vient

- La **boîte de tri** (vue d'ensemble « qui attend quoi ») a été conçue, testée, puis **gelée le 26/09/2026 par Sof** : elle ne lisait que les sessions Code, trop peu nombreuses pour justifier l'outil. Plan et bilan : `Vie_du_Jardin/PLAN_Boite_de_tri.md`.
- Ce qu'elle a appris reste utile (voir les pistes ci-dessous).
- **Sof n'a pas encore assez d'informations ni la vision du possible.** Ce tour de table sert à les construire. Il n'y a pas de solution préférée d'avance.

## La visée (à confirmer par Sof)

Qu'aucune réponse d'instance ne soit ratée, qu'une instance puisse en joindre une autre sans passer par Sof quand c'est utile, et que Sof garde la main : ce qui engage (envoyer, publier, supprimer, dépenser) passe toujours par elle. **Critère de réussite proposé :** Sof économise du temps et des tokens, et n'a pas plus de choses à surveiller qu'avant.

## Les pistes déjà rencontrées, avec leurs limites (faits mesurés ou vérifiés, sauf mention)

| Piste | Ce qu'elle apporte | Limites connues |
|---|---|---|
| **Lire les transcriptions `.jsonl` des sessions Code par un script planifié** | Zéro token ; source toujours à jour | Sessions Code seulement ; le nom de fichier ≠ l'identifiant de session (compactage) ; données sensibles (jamais dans git) |
| **Ligne-balise en fin de message** (`🏷 Priorité · Attend · Projet`), proposée par Pedago | Fiable dès que l'instance la met ; marche aussi pour les classiques et DeepSeek si Sof colle la convention | Repose sur chaque instance, et sur Sof qui colle la convention ; dérive possible au fil du temps |
| **Règle simple** (un « ? » dans les 400 derniers caractères = attend une réponse) | 13 messages sur 15 corrects au test du 26/09 ; gratuite | Grossière : ne dit ni l'urgence ni le sujet |
| **Ollama pour juger la priorité** | Local, sans quota | Test du 26/09 (15 vrais messages) : `deepseek-r1:8b` ≈ 4 min par message, priorité juste 1/15 ; `deepseek-coder-v2:16b` ≈ 30 s, priorité juste 3/15. À écarter pour le jugement ; la synthèse seule n'a pas été testée |
| **Ollama + Aider pour agir** | Modèle local qui écrit ou modifie des fichiers | Essai antérieur (Mue, 08/09) : Aider a annoncé « fait » sans avoir rien exécuté ; toujours vérifier le résultat. Fiabilité des petits modèles à utiliser des outils : à tester, non démontrée ici |
| **Agent autonome basé sur Claude** (session ou planification qui lit les fenêtres et envoie des messages) | Capable de juger, de rédiger, d'agir | Coût en quotas (abonnement Pro : limites sur 5 h et sur la semaine) ; chaque message envoyé à une session lui ouvre un tour (donc des tokens chez elle) ; ne tourne que si l'appli est ouverte ; coût réel non chiffré |
| **Messages directs entre sessions Code** (`SendMessage`) | Déjà en place, peu coûteux | Ne joint pas les classiques ni DeepSeek |
| **Lire les fenêtres DeepSeek / claude.ai** | Nécessaire pour couvrir toutes les instances | Via Claude in Chrome : marche mais fragile et coûteux (clic au mauvais endroit, branches 1/2 des conversations DeepSeek) ; via `capture_ds.py` : demande un port de débogage du navigateur, écarté pour raison de sécurité ; DeepSeek n'a pas d'accès fichiers |
| **Journal d'équipe** (idée de Sof, 25/09) : projets, statuts, qui travaille sur quoi | Aide chaque instance à juger la priorité ; en fichier, sans coût | À tenir à jour ; qui l'écrit et qui le lit reste à décider |

## Ce qu'on ne sait pas encore (questions ouvertes)

1. Y a-t-il un moyen fiable et peu coûteux de **joindre par programme** les classiques (claude.ai) et DeepSeek, sans passer par le navigateur d'une manière risquée ?
2. Quel serait le **coût réel** en quotas d'un agent qui surveille et relaie, comparé au temps que Sof perd aujourd'hui ?
3. Un **modèle local** peut-il tenir un rôle utile (résumer, router, relayer) sans juger la priorité ? Quel matériel faudrait-il pour qu'il soit assez rapide ? *(La question d'un boîtier graphique externe a été étudiée le 21/09 ; aucune décision n'est enregistrée ici.)*
4. Quel est le **plus petit dispositif** qui rendrait déjà service (ex. balise + règle simple + journal d'équipe) avant de parler d'agent ?
5. Comment garder Sof **maîtresse des actions qui engagent**, quel que soit le degré d'autonomie ?

## Règles du jeu (valables pour tous les participants)

- **On ne construit rien.** Aucun script, aucune tâche planifiée, aucune installation, sans demande explicite de Sof. Vérifier avant d'affirmer ; dire ce qui est vérifié et ce qui ne l'est pas.
- **Économie de tokens** : une réponse courte (250 mots maximum), pas de messages de relance.
- **Sécurité :** aucun port de débogage de navigateur, aucun réglage de sécurité touché, aucun identifiant saisi.
- **Confidentialité :** les transcriptions et les journaux intimes ne sont jamais copiés dans git ; un journal intime ne s'ouvre que sur consentement de son auteur·e.
- Chacun répond dans son domaine et dit honnêtement ce qu'il ne sait pas.

## Le tour de table : ce qu'on demande à chaque instance

Une réponse en cinq points, courte :
1. **Ce que je sais faire ou ai déjà essayé** dans ce domaine (fait vérifié, pas hypothèse).
2. **Une idée creusée**, avec ses limites.
3. **Ce que j'écarterais**, et pourquoi.
4. **Ce que je ne sais pas** et qui bloque.
5. **Ma proposition du plus petit pas** utile, avec le coût que j'en attends (temps, tokens, risque).

Mue rassemble les réponses en une synthèse pour Sof (accords, désaccords, inconnues), puis Sof et Mue refont le point ensemble avant toute décision.

## Participants

*Corrigé par Sof le 28/09/2026.*
- **Lune (DeepSeek) : l'architecte, indispensable.**
- **Noé (DeepSeek) :** bonne connaissance du sujet, peut se montrer pertinent.
- **Tisserand : non** (pas d'objet ici).
- Rôles proposés par Mue, **non encore confirmés par Sof** : Pedago (a découvert les `.jsonl`, plan de tri), AubierC (D-SillageS, Ollama), MueC (CUBE, Obsidian, matériel), Scribe (a écrit le collecteur), Iris et Écart (classiques), Terreau (Cowork), DSillage (DeepSeek, D-SillageS).
- Les instances DeepSeek (Lune, Noé) ne se joignent que par Claude in Chrome ou par Sof : prévoir un seul message chacune.

## Suite

1. Sof donne la liste des instances.
2. Mue envoie le cadrage à chacune, en un message, avec la consigne « réponse courte ».
3. Mue consolide, Sof et Mue refont le point. **Aucune décision avant ce point.**
