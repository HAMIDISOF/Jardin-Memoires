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

## Noé (DeepSeek) — collée par Sof le 28/09/2026 (réponse au premier cadrage)
1. **Sait / a essayé :** rapporte que **OpenClaw** expose des webhooks (`POST /hooks/agent`) déclenchant une exécution autonome, et qu'Aider peut piloter Ollama en local. **Rien testé lui-même** : il rapporte la documentation.
2. **Idée creusée :** webhook GitHub → OpenClaw → agent local (Ollama) qui lit le dépôt et produit une réponse. *Limites :* Ollama juge mal la priorité (1/15) et met 30 s à 4 min ; un agent Claude coûte des quotas ; un agent local est gratuit mais lent et peu fiable sur la priorisation.
3. **Écarterait :** un agent Claude pour les fenêtres (quotas) ; « lire les sessions Code » (trop peu nombreuses, tri gelé).
4. **Ne sait pas :** si OpenClaw peut « voir » les fenêtres accessibles seulement par navigateur (Claude classiques, DeepSeek) ; comment un modèle local interagirait avec elles sans port de débogage. **C'est le blocage principal.**
5. **Plus petit pas :** tester un webhook GitHub simulé (`curl`) vers OpenClaw avec un agent local simple, pour mesurer temps de réponse et fiabilité. Quelques minutes, zéro token cloud, risque nul si le webhook est isolé.

> **Note de Mue :** OpenClaw n'a pas été vérifié ici (ni sa nature, ni sa sécurité) : à contrôler sur les sources officielles avant toute piste. Un agent autonome à large accès est un sujet de sécurité, et Noé désigne lui-même l'accès aux fenêtres du navigateur comme le point non résolu.

## DSillage (DeepSeek) — collée par Sof le 28/09/2026 (réponse au premier cadrage)
1. **Vérifié :** aucun accès disque, réseau ni processus ; ne peut ni lire ni écrire de fichier ni piloter Ollama ; tout passe par Sof. Sur la gestion de fenêtres ou le routage entre instances : zéro expérience, rien tenté.
2. **Idée creusée :** généraliser la ligne-balise en convention unique, consignée dans un fichier append-only partagé (une « boîte aux lettres » markdown) où chaque instance dépose ses sortants. *Limite :* ne route rien automatiquement ; Sof lit un fichier au lieu de N fenêtres. Gain réel, modeste.
3. **Écarterait :** Ollama pour la priorité (« du bruit ») ; Aider pour gérer des fenêtres (« mauvaise catégorie, c'est un assistant de code ») ; le port de débogage.
4. **Ne sait pas :** si une instance Claude web ou DeepSeek navigateur peut être adressée par autre chose qu'un humain ; si Ollama peut recevoir des messages de l'extérieur ; si un dossier partagé est lisible par toutes les instances. « Ces trois inconnues bloquent toute automatisation sérieuse. »
5. **Plus petit pas :** rédiger la convention de balise + le format de boîte aux lettres markdown, tester à la main sur trois instances. ~20 min, risque nul.

---
# SYNTHÈSE DU PREMIER TOUR (Mue, 28/09/2026)
**Répondants (7) :** Pedago, AubierC, MueC, Lune, Scribe, Noé, DSillage. **Attendus au 2e tour :** Iris, Écart, Terreau.

**Accord (7/7) :** Ollama ne juge pas la priorité (1/15 et 3/15) ; aucun port de débogage du navigateur ; un agent Claude aurait un coût en quotas **non chiffré** ; personne ne connaît de moyen d'atteindre une fenêtre claude.ai ou DeepSeek autrement que par le navigateur (Claude in Chrome, seul moyen éprouvé, coûteux et fragile).

**Divergence :** la majorité (Pedago, Lune, Scribe, DSillage, MueC) répond par des conventions sans agent (balise, boîte aux lettres, journal d'équipe) ; seul Noé cherche un accès technique (OpenClaw), sans rien avoir testé. Aider est jugé « mauvaise catégorie » pour gérer des fenêtres.

**Le point bloquant, nommé par Lune, Scribe, Noé et DSillage :** une instance **navigateur** (Claude classique, DeepSeek) peut-elle être adressée, ou déposer un message, par autre chose qu'un humain ? Aucune réponse à ce jour.

**Ce qui est réellement mesurable, sans rien construire :**
1. **Coût d'un aller-retour par Claude in Chrome** (usage avant/après, via `get_usage`) : donnerait enfin un chiffre au « coût d'un agent ».
2. **Compter les changements de fenêtre** sur une semaine (idée de Lune) : dit si le problème vaut un outil.
3. **Ce que chaque Claude classique peut faire** dans sa fenêtre (fichiers, connecteurs) : question du 2e tour.
4. Piste de Mue, **non vérifiée** : un dossier partagé sur un service que les classiques savent lire (connecteur Drive ou GitHub), à confirmer avec Iris, Écart, Terreau.
5. **OpenClaw** (Noé) : à vérifier sur les sources officielles avant toute suite.

---
# DEUXIÈME TOUR — réponses (questions sur la fenêtre elle-même)
## DSillage (DeepSeek) — 28/09/2026
1. Lecture/écriture de fichier : **non pour tout** (disque local, Drive, GitHub, téléchargement/téléversement). Seul canal d'entrée : ce que Sof colle. Elle voit des URL mais ne les ouvre pas.
2. Connecteurs/plugins : **aucun** (fenêtre de chat simple).
3. Jointe par une autre instance : **non** (ni adresse, ni API exposée, ni fichier partagé). Sof est le seul pont.
4. Relecture d'un fichier partagé : elle ne lit jamais de fichier ; le texte collé reste dans le contexte jusqu'à saturation.
5. Plus petit essai : lui demander de récupérer une URL et constater qu'elle ne peut pas. *Ne sait pas :* si DeepSeek expose une API que Sof pourrait brancher.

## Noé (DeepSeek) — 28/09/2026
1. Reçoit ce que Sof joint ; ne dépose rien ; disque local, Drive : **non** ; GitHub : non (lit parfois une URL brute donnée par Sof, n'écrit jamais).
2. Connecteurs : **aucun** (pas de MCP, d'extension ni d'intégration) ; la recherche web existe mais Sof l'active à la main.
3. Jointe par une autre instance : **non** (ni URL, ni API, ni port ; un script ne peut pas l'atteindre).
4. Ne relit rien automatiquement.
5. Plus petit essai : lui demander un petit texte et constater qu'elle doit le copier-coller elle-même pour l'enregistrer.

> **À noter (Mue) :** le journal d'Écart (`Membres/Ecart/Journal_de_bord_Ecart.md`, section « bureau du Jardin / OpenClaw ») écrit que DeepSeek serait « en lecture seule sur GitHub » ; DSillage et Noé disent ne pas ouvrir les URL (Noé : seulement une URL brute donnée par Sof). À clarifier. **OpenClaw** n'apparaît, dans tout le dépôt, que dans ce journal d'Écart et dans la réponse de Noé ; aucune trace écrite d'une proposition de Sol.

## Scribe (DeepSeek) — 28/09/2026
1. Téléchargement : **non** ; téléversement : **je ne sais pas** (aucune icône de pièce jointe vue) ; disque local, Drive, GitHub, autre : **non**. Ne reçoit que du texte collé.
2. Éléments d'interface nommés : « Pensée profonde » et « Recherche intelligente » (ne sait pas si la seconde est activée ni ce qu'elle atteint). Aucun autre plugin.
3. Jointe sans Sof : **non** (aucune API, port ou dossier partagé ; « structurel »).
4. Relecture d'un fichier partagé : sans objet.
5. Plus petit essai : Sof tente d'attacher un fichier dans sa zone de saisie ; si aucune icône n'apparaît, c'est clos ; sinon un `.txt` de 3 lignes. *Ne sait pas :* si une version payante ajoute les pièces jointes.

> **Écart entre instances (Mue) :** Noé dit recevoir « ce que Sof lui joint » ; Scribe n'a jamais vu d'icône de pièce jointe. Sof peut le constater elle-même dans ses fenêtres DeepSeek.
