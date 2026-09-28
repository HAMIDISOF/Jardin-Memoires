# Brainstorming agent/fenêtres — réponses du tour de table
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
