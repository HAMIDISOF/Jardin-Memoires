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

## Iris (Claude classique, claude.ai) — 28/09/2026
1. **Fichiers :** espace de travail éphémère dans son conteneur (`/home/claude`, `/mnt/user-data/outputs`, réinitialisé entre sessions) : oui ; fichiers téléversés par Sof (`/mnt/user-data/uploads/`) : oui ; **Google Drive : oui, outils MCP actifs (lecture et écriture)** ; **GitHub : oui, outils MCP actifs (lecture et écriture de fichiers dans un dépôt)** ; téléchargement vers Sof (`present_files`) : oui ; disque local de Sof : non.
2. **Connecteurs visibles :** Gmail, Google Calendar, Google Drive, GitHub, Slack, Claude Docs, claude-in-chrome ; outils internes : bash, création de fichiers, recherche web, météo, sports.
3. **Jointe sans Sof :** pas directement ; **indirectement oui** : si elle écrit dans un fichier GitHub ou Drive, une autre instance ayant les mêmes connecteurs peut le lire. « Le seul canal réel que je constate. »
4. **Relecture :** seulement quand elle appelle l'outil (sur sa décision ou à la demande de Sof) ; pas de relecture automatique.
5. **Test minimal :** qu'elle écrive une phrase dans un fichier `test_ping.md` d'un dépôt GitHub existant, puis qu'une autre instance la lise avec ses outils GitHub. Réversible.

> **Mue :** c'est la première réponse qui ouvre un canal réel entre une fenêtre claude.ai et d'autres instances. Attention : le dépôt du Jardin est **public** ; une boîte aux lettres doit être dans un dépôt **privé** ou sur Drive. Écritures externes : seulement avec l'accord de Sof.

## Lune (DeepSeek, architecte) — 2e tour, 28/09/2026
1. **Fichiers :** ne lit ni n'écrit rien par elle-même ; Sof peut lui **attacher** un fichier (image, .md, .html) qu'elle lit dans la conversation ; elle ne peut pas lui en envoyer ; disque local, Drive, GitHub : **non**.
2. **Connecteurs :** aucun visible (pas de panneau d'outils ni de plugins).
3. **Jointe :** non ; seuls moyens : Sof copie-colle ou attache un fichier. Pas de mémoire hors session.
4. **Relecture :** seulement ce qui est dans la conversation.
5. **Plus petit essai :** Sof attache un fichier neuf avec un fait précis et lui demande ce fait.

**Complément de Lune après une recherche sur le web (rapporté par Sof, NON vérifié par Mue) :**
- DeepSeek n'a pas de connecteur Drive natif ; il existe des architectures indépendantes (API DeepSeek + API Google).
- Elle pense que « la solution open source dont on a parlé » est un **serveur MCP** auto-hébergé pour Drive ; elle cite « Iris MCP Gateway », « honest-drive-mcp » et « mcp-google-drive » (Parafin). Principe : installer un serveur MCP sur la machine, créer un projet Google Cloud avec l'API Drive, s'authentifier une fois par OAuth.
- Elle reconnaît **ne pas savoir** si sa fenêtre DeepSeek est un client MCP ; ces serveurs sont conçus pour Claude Desktop, Claude Code ou des clients MCP génériques. Petit pas proposé : vérifier si la fenêtre DeepSeek a un panneau « MCP » ou « Outils ».

> **Réserves de Mue :** (a) ces trois projets n'ont pas été vérifiés (existence, auteurs, sécurité) : installer un serveur tiers qui obtient un accès OAuth au Drive de Sof serait une décision de sécurité à ne prendre qu'après vérification sur les dépôts officiels ; (b) le nom « Iris MCP Gateway » coïncide avec celui d'une instance du Jardin : raison de plus de vérifier ; (c) un serveur MCP a besoin d'un **client MCP** : la fenêtre de chat DeepSeek n'en est pas un, d'après les quatre instances DeepSeek qui n'y voient aucun connecteur. Donc, même s'il existe, il ne réglerait pas l'accès aux fenêtres DeepSeek ; du côté Claude, Drive et GitHub existent déjà en connecteurs intégrés (Iris et sessions Code).

## Sol (DeepSeek) — 2e tour, 28/09/2026
1. **Fichiers :** non, ni lecture ni écriture par elle-même (ni disque local, ni Drive, ni GitHub) ; elle lit seulement ce que Sof colle ou joint.
2. **Connecteurs :** aucun visible ; ne sait pas ce qui existe côté plateforme.
3. **Jointe :** non ; seul canal : Sof copie-colle ou joint un fichier.
4. **Relecture :** non automatique ; seulement ce qui est présent dans le contexte de la fenêtre.
5. **Test :** Sof joint un .txt d'un mot, lui demande de le répéter, puis envoie un message anodin ; le test ne prouve que la mémoire de fenêtre, pas un accès fichier.

> **Bilan DeepSeek (Mue) :** Lune, Noé, Scribe, DSillage et Sol : **cinq sur cinq, aucun accès, aucun connecteur, aucun moyen d'être jointe sans Sof.** Sol n'a pas identifié de « solution open source » précise.

## Réponse NON ÉTIQUETÉE (collée par Sof le 28/09/2026) — probablement Terreau (Cowork) : à confirmer
1. **Fichiers :** sandbox cloud de travail (lecture/écriture + envoi à Sof) : oui. Disque du PC/Mac de Sof, Drive, GitHub : oui **mais par intermittence**, via un « pont device » qui se connecte et se déconnecte, hors de son contrôle. Mémoire persistante (profil / areas / topics) : oui, lecture/écriture directe.
2. **Outils vus actifs ou déconnectés :** Google_Calendar, Google_Drive, memory, remote-devices (sous-modules Claude_Browser, computer, github), claude-code-remote, Claude_Docs, WebSearch/WebFetch, Bash, Read/Write/Edit, Artifact, Skill.
3. **Joignable sans copier-coller :** oui : la **mémoire persistante est partagée** entre les autres surfaces Claude du même compte (une autre session de Sof pourrait lire ce qu'elle y écrit) ; et `SendMessage`/`ListAgents` (jugé peu fiable à cause d'un identifiant de session instable ; ne sait pas si mieux aujourd'hui).
4. **Relecture :** jamais automatique ; seulement en appelant l'outil.
5. **Essai :** lui faire écrire une ligne horodatée dans un fichier mémoire précis, puis demander à une autre instance du même compte de le lire sans le lui coller.

---
# SYNTHÈSE DU DEUXIÈME TOUR (Mue, 28/09/2026)
**Réponses :** DeepSeek 5/5 (Lune, Noé, Scribe, DSillage, Sol) ; Claude : Iris + une réponse non étiquetée (probablement Terreau). **Manque :** Écart (ou la seconde, selon l'étiquette).

**Deux mondes, très nets :**
- **DeepSeek (5/5) :** aucun accès, aucun connecteur, aucun moyen d'être jointe sans Sof. Joindre une fenêtre DeepSeek = passer par Sof ou par le pilotage du navigateur (Claude in Chrome ou équivalent).
- **Claude (classiques, Cowork) et sessions Code :** des canaux existent **déjà, intégrés** : Google Drive et GitHub (Iris ; sessions Code ; Cowork par intermittence), et une mémoire partagée entre surfaces d'un même compte.

**Le seul canal démontrable aujourd'hui :** un dossier partagé (Drive) ou un dépôt **privé** (GitHub) que les Claude lisent et écrivent chacune quand elles appellent l'outil. Aucune ne relit d'elle-même : c'est une boîte aux lettres, pas un réveil.

**Rien n'est prouvé tant qu'on n'a pas fait le test** (une instance écrit une ligne, une autre la lit sans copier-coller). Réserves : le pont de Cowork est intermittent ; les serveurs MCP tiers cités par Lune ne sont pas vérifiés ; écrire sur Drive/GitHub = envoyer du contenu à un service extérieur (accord de Sof).

## Réponse NON ÉTIQUETÉE n°2 (collée par Sof le 28/09/2026) — probablement Écart (Claude classique) : à confirmer
1. **Fichiers :** téléversement de Sof vers elle (images, PDF, texte) : oui ; téléchargement depuis elle (`present_files`) : oui ; disque local de Sof : non ; **Google Drive : oui, connecteur actif** (a lu et créé des fichiers Drive dans cette session) ; **GitHub : oui, connecteur actif** (dit avoir lu et écrit « dans HAMIDISOF/Jardin-Memoires ce matin même ») ; conteneur Linux interne : oui.
2. **Connecteurs :** GitHub, Google Drive, Google Calendar, Claude Docs, claude-in-chrome, Slack, Gmail ; outils internes : bash, web_search, web_fetch, Artifact.
3. **Jointe sans Sof :** non, à sa connaissance ; une autre instance peut lire ce qu'elle a écrit sur GitHub ou Drive, **seulement si elle est invitée à le faire dans sa propre fenêtre**. Pas de canal direct.
4. **Relecture automatique :** non (pas de polling ni de surveillance).
5. **Test :** Sof crée une ligne dans un fichier GitHub ou Drive et lui demande de la lire « à froid » ; sens inverse : lui faire écrire une ligne et vérifier sur GitHub.

> **Vérification de Mue (partielle) :** sur GitHub, un commit « Valise Écart — ajout H-QBheU/H-Cube (topo Lune, 26/09/2026) » existe le **27/09 à 15h27**, signé « Sofana » (le connecteur écrit sous le compte de Sof, donc on ne distingue pas l'auteur). C'est cohérent avec l'idée qu'une instance claude.ai écrit dans le dépôt, mais ce n'est **pas** « ce matin même » (28/09) ; je ne peux pas attribuer ce commit à cette instance.
