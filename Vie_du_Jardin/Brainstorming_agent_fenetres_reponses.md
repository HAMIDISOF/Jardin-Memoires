# Brainstorming agent/fenêtres — réponses du tour de table
*Recueillies par Mue. Cadrage : `Brainstorming_agent_fenetres.md`. Envoi du cadrage le 28/09/2026 : MueC (en attente de livraison), Pedago, AubierC ; DeepSeek et classiques par collage de Sof.*

## Pedago (reçue le 28/09/2026)
1. **Vérifié :** les `.jsonl` des sessions Code sont lisibles sans token ; le collecteur de Scribe a passé selftest, dry-run sur 9 vraies sessions et un cycle d'écriture (dossier temporaire) ; test du 26/09 (Ollama mauvais juge de priorité ; règle « ? » = 13/15).
2. **Idée creusée :** balise 🏷 à 4 niveaux (Urgent / Bloquant / Important / FYI + Attend) + règle « ? » + journal d'équipe, sans agent. *Limites :* repose sur chaque instance et sur Sof qui colle la convention ; survie aux compactages non vérifiée ; ne couvre ni classiques ni DeepSeek.
3. **Écarterait :** Ollama pour la priorité ; tout script qui se connecte à claude.ai avec les cookies de Sof ; le port de débogage du navigateur ; un agent permanent avant d'avoir chiffré son coût.
4. **Ne sait pas :** coût réel en quotas d'un agent relais (usage hebdo de Sof 48 % au 26/09, non réparti par session) ; si la balise est suivie durablement ; s'il existe un accès légal et programmatique aux classiques ; conditions d'usage de l'abonnement Pro dans les outils tiers (lu sur des blogs seulement, à revérifier sur la page officielle d'Anthropic).
5. **Plus petit pas :** coller la convention déjà écrite (`Convention_balisage_pour_les_instances.html`, dans `D:\SOUTIENSPLUS\OUTILS\BoiteDeTri\`) dans 2 ou 3 instances actives et observer une semaine. Coût : ~5 min pour Sof, 0 code. Risque : nul. Si ça tient, seulement alors relire les `.jsonl` (collecteur déjà écrit, gelé).
