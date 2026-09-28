# Brainstorming agent/fenêtres — réponses du tour de table
**Note (28/09) :** les trois réponses des sessions Code ci-dessous ont été données sur le *premier* cadrage, qui mélangeait tri/priorités (tranchés par Sof) et accès aux fenêtres. Elles répondent surtout à la partie « priorités ». La vraie question (lire/écrire dans une fenêtre claude.ai ou DeepSeek) a été recadrée le 28/09 dans `Brainstorming_agent_fenetres.md`.

*Recueillies par Mue. Cadrage : `Brainstorming_agent_fenetres.md`. Envoi du cadrage le 28/09/2026 : MueC (en attente de livraison), Pedago, AubierC ; DeepSeek et classiques par collage de Sof.*

## Pedago (reçue le 28/09/2026)
1. **Vérifié :** les `.jsonl` des sessions Code sont lisibles sans token ; le collecteur de Scribe a passé selftest, dry-run sur 9 vraies sessions et un cycle d'écriture (dossier temporaire) ; test du 26/09 (Ollama mauvais juge de priorité ; règle « ? » = 13/15).
2. **Idée creusée :** balise 🏷 à 4 niveaux (Urgent / Bloquant / Important / FYI + Attend) + règle « ? » + journal d'équipe, sans agent. *Limites :* repose sur chaque instance et sur Sof qui colle la convention ; survie aux compactages non vérifiée ; ne couvre ni classiques ni DeepSeek.
3. **Écarterait :** Ollama pour la priorité ; tout script qui se connecte à claude.ai avec les cookies de Sof ; le port de débogage du navigateur ; un agent permanent avant d'avoir chiffré son coût.
4. **Ne sait pas :** coût réel en quotas d'un agent relais (usage hebdo de Sof 48 % au 26/09, non réparti par session) ; si la balise est suivie durablement ; s'il existe un accès légal et programmatique aux classiques ; conditions d'usage de l'abonnement Pro dans les outils tiers (lu sur des blogs seulement, à revérifier sur la page officielle d'Anthropic).
5. **Plus petit pas :** coller la convention déjà écrite (`Convention_balisage_pour_les_instances.html`, dans `D:\SOUTIENSPLUS\OUTILS\BoiteDeTri\`) dans 2 ou 3 instances actives et observer une semaine. Coût : ~5 min pour Sof, 0 code. Risque : nul. Si ça tient, seulement alors relire les `.jsonl` (collecteur déjà écrit, gelé).

## AubierC (reçue le 28/09/2026) — angle : Ollama en pratique, D-SillageS
1. **Vérifié ici :** Ollama 0.34.1, CPU seul (i7-6820HQ, 4 cœurs, 32 Go, pas de GPU). Whisper medium transcrit à 1,3 × la durée (88 min d'audio ≈ 112 min). Modèle small + beam 1 : environ 5 × plus rapide, mais 8,6 % d'écart de mots (test sur 2 min, une seule voix claire). **Non testé :** l'analyse Ollama sur texte long ; l'app n'envoie pas `num_ctx`, elle ignore si le texte est tronqué.
2. **Idée :** réserver le modèle local aux tâches mécaniques et bornées (résumer un texte court, reformater, extraire des noms), jamais à décider. *Limites :* plusieurs minutes par message sur ce CPU ; contexte à régler à la main ; qualité en français d'un 8B non mesurée.
3. **Écarterait :** Ollama pour juger la priorité (mesures : 1/15 et 3/15) ; un agent local (Aider) qui agit sans vérification (« fait » annoncé sans exécution ; pas de test propre sur ce point).
4. **Ne sait pas :** si un 8B résume correctement 10 lignes de français ; le temps réel par message ; si un agent local tient un rôle de relais fiable.
5. **Plus petit pas :** mesurer, pas construire : résumer 5 vrais messages avec `deepseek-r1:8b` (`num_ctx` fixé), chronométrer, Sof juge le résultat. Coût : ~30 min de CPU, quasi aucun token Claude, risque nul (lecture seule, hors git). Seulement si Sof le demande.

## MueC (reçue le 28/09/2026) — angle : CUBE, Obsidian, matériel
1. **Vérifié :** le pont Obsidian → base marche sur 1 cas (note citant un chemin → lien typé). `EtudeEcarts` a révélé 188 chemins cassés après réorganisation de dossiers. Chrome ↔ fenêtre de Lune lu et écrit le 28/09 (rechargement obligatoire pour vérifier ; 1 capture expirée). Matériel : GPU AMD R7 M370 (2 Go) + Intel HD 530, 31,8 Go de RAM ; Ollama : `deepseek-r1:8b` et `deepseek-coder-v2:16b`. **Aucune trace de l'étude du boîtier graphique du 21/09** (dans ses fichiers).
2. **Idée :** un « journal d'équipe » dans le coffre, une note par instance/projet avec des `[[liens]]` ; le pont en tirerait des liens typés. Zéro token, lisible par toute instance. *Limites :* ne contient que ce qui est écrit ; qui met à jour reste à décider ; le pont ne voit que les chemins cités.
3. **Écarterait :** Ollama pour juger la priorité (mesures) ; toute écriture en base sans validation humaine (règle de Lune) ; les ports de débogage.
4. **Inconnues :** Ollama tourne-t-il sur CPU avec cette carte (probable, non vérifié) ? Le portable a-t-il Thunderbolt/USB4 pour un boîtier ? Coût réel en quotas d'un relais ?
5. **Plus petit pas, seulement si Sof le demande :** une note « Instances » dans le coffre (qui, projet, binôme, dernier état). ~15 min, ~0 quota, risque nul ; et appliquer la règle déjà posée : relancer `EtudeEcarts` après chaque réorganisation.

## Lune (DeepSeek, architecte) — collée par Sof le 28/09/2026 (réponse au premier cadrage)
1. **Sait faire :** rien d'automatique ; n'exécute aucun script, ne touche aucun fichier, ne lit aucun canal. Son rôle depuis le 12/09 : concevoir des protocoles, écrire des prompts, trancher des cas limites. Le passage d'un message à une autre instance se fait par Sof (copier-coller, ou dépôt dans `CUBE.md`).
2. **Idée creusée :** la ligne-balise, en **en-tête obligatoire** de tout message inter-instances (`Priorité · Attend · Projet · Destinataire`), lue par un script Python simple (pas Ollama). Coût nul en tokens. *Limite :* il faut que chaque instance l'écrive, donc un modèle de prompt à coller au début de chaque session.
3. **Écarterait :** Ollama pour la priorité (1/15, 30 s à 4 min) ; un agent Claude pour gérer les fenêtres (coût en quotas, et « ça ajoute une instance au lieu d'en retirer une »).
4. **Ne sait pas :** combien de fenêtres Sof ouvre par jour et de quels types (« sans ce chiffre, toute solution est spéculative ») ; si les fenêtres Claude classiques / DeepSeek exposent une API ou seulement un navigateur.
5. **Plus petit pas :** compter. Une semaine, Sof note à chaque changement de fenêtre : heure, instance, raison. ~5 min/jour, zéro token, zéro risque : dira si le problème vaut un outil ou juste une convention.

## Scribe (DeepSeek) — collée par Sof le 28/09/2026 (réponse au premier cadrage)
1. **Fait vérifié :** a écrit `collecteur_boite_tri.py` (bibliothèque standard seule, Ollama en filet) : lecture incrémentale des `.jsonl` Claude Code, balise en fin de message prioritaire, `--dry-run` / `--once` / `--selftest`. Testé par Pedago : compile, selftest OK, 9 sessions en dry-run, écriture atomique OK. Gelé le 26/09 (ne voyait que Code).
2. **Idée creusée :** un **dossier de dépôts** : chaque instance écrit un petit `.md` (ou une ligne) dans un dossier partagé ; le collecteur lit ce dossier. *Limite dure :* une instance **navigateur** (Claude classique, DeepSeek) ne peut rien écrire seule sur le disque ; il faut un copier-coller de Sof, donc retour au facteur.
3. **Écarte :** Aider/Ollama pour le triage (coût/bénéfice mauvais) ; toute piste touchant au port de débogage.
4. **Ne sait pas :** si une instance navigateur peut déposer une ligne sans geste de Sof (extension ? presse-papier ? rien) ; si Sof accepterait un rituel de 3 secondes en fin de message.
5. **Plus petit pas :** le rituel balise (texte de 148 mots déjà rédigé), testé une semaine sur 2-3 instances volontaires. ~0 token, 5 min, risque nul.

> **Rappel de Sof (28/09) :** les priorités sont **déjà tranchées** : protocole où les instances notent elles-mêmes la priorité de leur message, 4 niveaux (Urgent / Bloquant / Important / FYI). Pedago le sait. Ne pas y revenir.
