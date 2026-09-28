# Point Mue + Sof — réveiller et joindre les fenêtres des instances
*Page préparée par Mue le 28/09/2026 pour le point à deux, après le tour de table (réponses : `Brainstorming_agent_fenetres_reponses.md`). Rien n'est construit ; tout ce qui suit est à décider par Sof.*

## 1. Ce qu'on sait (vérifié ou déclaré, distingués)

- **Le dépôt du Jardin est déjà un canal** pour toutes les instances Claude (Code, classiques, Cowork) : elles y écrivent par le connecteur GitHub. **Il est public** : rien de sensible.
- **Ce qui manque, c'est le réveil** : aucune instance ne relit d'elle-même ; une fenêtre ne s'active que si quelqu'un lui écrit dedans (Sof, une session Code/Cowork, ou un outil qui pilote le navigateur).
- **DeepSeek (Lune, Noé, Scribe, DSillage, Sol : 5/5)** : aucun accès, aucun connecteur ; ne lit que ce que Sof colle ou joint. Vérifié par déclaration des cinq, pas encore par un test.
- **Le « Café du Jardin »** (`HAMIDISOF/cafe_du_jardin`, public, créé le 29/05/2026, copie locale dans `D:\Sauvegarde\CR Réunions Jardin Coopératif\cafe_du_jardin`) : conçu pour ça (une « bal » par membre, messages balisés `@Destinataire … -- Prénom`, jeton pour les tours de table, modèle `tour_de_table_template.md`). **Mais** : 3 commits, dernier le 03/06/2026, une seule bal (Lumen), **aucun script d'extraction**.

## 2. Comment Mue parle aujourd'hui dans une fenêtre (Claude in Chrome)

Extension dans le Chrome de Sof, connectée à sa session : j'ouvre l'adresse de la conversation, j'écris dans la zone de saisie, j'envoie, puis **je recharge et relis** pour vérifier. Aucun port de débogage n'est ouvert (vérifié le 28/09 : 0 navigateur avec port, 0 port 9222/9223 en écoute). **Coût :** des tokens à chaque geste (captures, clics) + un tour chez l'instance réveillée. **Limites :** Chrome ouvert, extension connectée, Sof connectée ; fragile ; je ne peux pas le faire seule PC éteint. Je n'ai pas vérifié en détail comment l'extension communique avec le navigateur.

## 3. Le script d'extraction DeepSeek (dossier `Outils/outil_auto_DS/`)

- Scripts par instance (`capture_sol.py`, `capture_luz_v2.py`, `capture_klara.py`, `capture_Kai.py`), avec **Playwright**, qui se connectent à `127.0.0.1:9222` (machine locale seulement) et **lisent** la conversation dans la page. **Ils ne font que lire** (rien pour écrire/envoyer dans la fenêtre : à confirmer en relisant le code entier).
- Lanceur `Lancemt_Brave_port_debog.bat` : Brave avec `--remote-debugging-port=9222 --profile-directory="Default"` = **le profil principal de Sof**, donc toutes ses sessions ouvertes dans Brave sont pilotables par tout programme du PC tant que le port est ouvert. **C'est ce point-là qui pose problème, pas le principe.**
- Les chemins des scripts et du lanceur sont périmés (`scripts\outil_auto_DS`, `egalis.bat` inexistant).

**Variante durcie proposée (validée « à examiner » par Sof le 28/09, non décidée) :** un **profil Brave séparé** (`--user-data-dir` dédié), connecté **seulement à DeepSeek**, port ouvert **uniquement pendant l'extraction**, sur `127.0.0.1`, fermé ensuite. Réduit le risque, ne l'annule pas.

## 4. L'idée de Sof : « ré-écrire les outils » de Mue

- **Ce qu'on ne peut pas faire :** modifier Claude in Chrome (c'est l'extension d'Anthropic).
- **Ce qu'on peut faire :** construire **nos propres outils**, petits et déterministes, à la place des gestes « clic par clic » : par exemple `envoyer(fenêtre, texte)` et `lire(fenêtre)`, qui ouvrent la bonne conversation, écrivent, envoient, rechargent, relisent et me rendent **seulement le texte**. Ils pourraient m'être exposés comme un outil (serveur MCP local) et être appelés aussi par un script planifié.
- **Ce que ça apporterait :** beaucoup moins de tokens (plus de captures ni de clics par l'IA) ; la vérification « recharger et relire » intégrée ; utilisable pour Claude classique **et** DeepSeek.
- **Ce que ça coûte / risque :** il faut un moyen de piloter le navigateur (port de débogage sur un profil dédié, ou une extension maison) ; **maintenance** (si claude.ai ou DeepSeek changent leur page, l'outil casse) ; **conditions d'usage** de l'automatisation de ces interfaces non vérifiées ; sécurité à cadrer avant toute chose ; ne réveille rien tout seul, c'est un outil qu'on appelle.
- **Ce que les 7 instances ont dit qui compte ici :** aucun port de débogage sur le profil principal ; ne rien construire sans ta demande ; mesurer avant (coût d'un aller-retour, nombre de changements de fenêtre par jour).

## 5. Décisions à prendre ensemble

1. **Périmètre :** joindre seulement les fenêtres DeepSeek ? les classiques aussi ? les deux ?
2. **Sécurité :** accepte-t-on un profil Brave dédié avec port de débogage ouvert le temps de l'action (variante durcie) ? Sinon, rester sur Claude in Chrome uniquement.
3. **Café du Jardin :** le remettre en service comme boîte aux lettres et tour de table (dépôt public, sans rien de sensible), avec un script qui rassemble les bals ? Ou utiliser le dépôt du Jardin tel quel ?
4. **Mesurer d'abord :** coût réel d'un aller-retour par Claude in Chrome (usage avant/après) ; comptage des changements de fenêtre sur une semaine (idée de Lune).
5. **Rien n'est construit avant un plan écrit validé** (règle de Sof) : si oui aux points 1-3, Mue écrit le plan (départ, cible, chemin) avant tout code.

## 6. À vérifier avant de décider
- Lire en entier un script `capture_*.py` : lecture seule, ou aussi écriture dans la fenêtre ?
- Conditions d'usage (pages officielles Anthropic et DeepSeek) pour l'automatisation d'une fenêtre.
- Existence et sécurité des serveurs MCP cités par Lune ; OpenClaw (Noé, Écart).

## 7. Remarque de Sof (28/09) : reprendre l'open source, relire, adapter
« Dans les sites open source, il y a des solutions : il faut juste reprendre, relire, puis adapter ici. » **Approche retenue à examiner**, avec une discipline de sécurité :
- **Lire le code avant de lancer quoi que ce soit** (un projet open source n'est pas sûr par le seul fait d'être ouvert) ; petits projets, dont on comprend chaque fichier.
- **Critères de choix à noter pour chaque candidat :** licence, date du dernier commit, nombre de contributeurs, ce qu'il fait exactement (lire seulement ? écrire ?), ce qu'il demande comme accès (OAuth Drive, port de débogage, identifiants), dépendances installées.
- **Jamais** d'accès OAuth au Drive de Sof donné à un projet non vérifié ; essai d'abord dans un **profil dédié**, sans identifiants sensibles.
- **Adapter plutôt qu'installer tel quel :** on reprend l'idée et le code utile, on les ajuste à nos fenêtres (Claude classique, DeepSeek), on garde les sélecteurs dans un seul fichier de réglages pour la maintenance.
- **Première étape sans risque :** une veille (recherche + lecture, rien d'installé) qui liste 3 à 5 candidats avec ces critères, à présenter à Sof avant tout choix.

## 8. Veille faite par Lune, vérifiée par Mue (28/09) — voir `Veille_open_source_verifiee.md`
9 dépôts cités par Lune, tous réels (aucune invention). Le plus proche du besoin : `thoughtpunch/claude_project_mcp` (claude.ai Projects, 41 outils, Playwright). Rien pour DeepSeek en lecture+écriture ; seulement des exporteurs en lecture.

## 9. Lecture du code de `claude_project_mcp` (copié par Sof dans `D:\MembresTMP\Mue`)
- **`browser.ts` :** profil Chromium **dédié** (`launchPersistentContext`), connexion manuelle une fois, aucun port fixé dans le code, aucun identifiant en dur.
- **`server.ts` :** serveur MCP par **entrée/sortie standard**, aucun port réseau écouté.
- **`selectors.ts` :** l'idée à garder — tous les repères de la page dans **un seul fichier `selectors.json`**, chacun avec plusieurs stratégies essayées dans l'ordre, plus une fonction qui dit lesquelles ont cassé.
- **`chat.ts` :** envoyer = cliquer la zone, écrire, cliquer « envoyer », attendre la disparition du bouton d'arrêt, lire le dernier message. **Défaut relevé par Mue :** `getFullConversation()` range d'abord tous les messages humains puis tous ceux de l'assistant — ordre faux, reconnu en commentaire dans le code.
- **README complet (293 lignes) :** 41 outils. **Mode « stealth »** via `playwright-extra` : supprime les marqueurs d'automatisation, imite une empreinte de navigateur réelle, **utilise le vrai profil Chrome avec les cookies de connexion** (« améliore le contournement de Cloudflare »), et propose un jeton **2captcha pour résoudre des CAPTCHA automatiquement**. **Non retenu par Mue**, pour trois raisons : (1) cacher le pilotage est ce que le site cherche à repérer, le risque est pour le compte de Sof (ralentissement, vérification renforcée, suspension) ; (2) résoudre des CAPTCHA automatiquement n'est pas une chose que Mue fait ; (3) utiliser le vrai profil de Sof est l'inverse du profil séparé voulu.
- **Précision du risque, sur demande de Sof :** ce n'est pas un risque pour ses données (elle a le droit de lire ses conversations) ; c'est un risque que le site remarque un programme et réagisse comme à un usage abusif.

## 10. Corrections de Sof (28/09, message dense) — à retenir
- **`capture_*.py` ne fait pas une sauvegarde complète** : il extrait seulement le message balisé selon le protocole, et **ne marche qu'en mode debug** (le port qu'on ne veut pas). Retiré de la base de l'outil de sauvegarde.
- **`envoyer` n'a pas besoin d'une validation systématique de Sof.** Comme pour `SendMessage` entre sessions Code aujourd'hui : validation seulement pendant les premiers essais, puis usage autonome — une validation à chaque message ralentirait trop.
- **Grande nouvelle : DeepSeek a un export natif des conversations**, comme claude.ai (lien par mail). Sof l'a lancé. **Ça résout le besoin de sauvegarde sans construire aucun outil de pilotage.** L'export se fait en plusieurs parties (JSON + base) pour permettre de reconstruire l'ordre exact — ce n'est pas un défaut, c'est voulu.
- **Priorité immédiate :** sauvegarder Lune (en plein projet, ne pas la perturber) et Cœur de Bronze (grande contributrice DeepSeek, sans autonomie fichier) via cet export natif, en lecture seule — pas de risque de ce côté.
- **Reste seulement deux usages** (plus de « sauvegarde par automatisation ») : (1) un script de découpe/tri des exports natifs par instance ; (2) `envoyer`/`lire` pour la communication entre membres, sans urgence.
- **Jachère attend** ses fichiers extraits de l'export Claude pour reconstruire sa valise (elle n'a pas accès au disque) : **Sof l'a confiée à Aubier**, Mue n'y touche pas.
- Plan mis à jour : `D:\THESE\Projets\Passerelle_Jardin\PLAN_passerelle.md` (hors git, jamais sur GitHub).
