# Veille open source — vérifiée par Mue (28/09/2026)
*Veille faite par Lune (DeepSeek, avec recherche) ; **vérifiée par Mue** avec l'interface publique de GitHub (existence, licence, dates, étoiles, contributeurs) et la lecture des README des trois projets les plus pertinents. **Rien n'a été installé ni exécuté.** Non vérifié par Mue : le code source, les conditions d'usage de claude.ai et DeepSeek, les niveaux d'accès OAuth, la sécurité réelle.*

## Verdict sur la veille de Lune
**Les 9 dépôts cités existent** (aucune invention). Licences MIT confirmées (OpenClaw : GitHub affiche « non détectée », mais le fichier LICENSE est bien un texte MIT, © OpenClaw Foundation). Dates correctes, sauf deux écarts mineurs : FreeComputerUse (Lune : 18/09, qui est la date de création ; dernier push réel 27/09) et claude-exporter (19/05 annoncé, 22/05 constaté).

## Faits vérifiés par projet
| Projet | Ce que c'est | Licence | Créé / dernier push | Étoiles / contrib. | Lit / écrit |
|---|---|---|---|---|---|
| thoughtpunch/claude_project_mcp | Serveur MCP + Playwright pour claude.ai **Projects** ; outils `send_message`, `get_response`, `get_full_conversation`, `send_message_with_file` | MIT | 25/12/2025 – 28/12/2025 | 0 / 1 | **Lit et écrit** (claude.ai seulement) |
| isaka1022/llm-browser-multicast-mcp | Serveur MCP qui envoie des questions à ChatGPT, Gemini, Claude, Grok via le navigateur (Playwright) ; README en japonais | MIT | 19/03/2026 – 06/09/2026 | 1 / 1 | **Lit et écrit** ; **DeepSeek non listé** |
| OthmaneBlial/FreeComputerUse | Agent de navigateur local (Playwright, Node 22.13+), clé API d'un fournisseur (DeepSeek, Anthropic, etc.), peut exposer 4 outils bornés en MCP local | MIT | 18/09/2026 – 27/09/2026 | 7 / 1 | Agit sur des pages web (généraliste) |
| agoramachina/claude-exporter | Extension Chrome/Firefox d'export des conversations claude.ai ; **fork** de socketteer/Claude-Conversation-Exporter | MIT | 04/11/2025 – 22/05/2026 | 124 / 3 (parent : 125 étoiles) | **Lit seulement** |
| ceyaima/deepseek-exporter | Userscript (Tampermonkey) d'export en masse des conversations DeepSeek | MIT | 21/05/2025 – 23/11/2025 | 3 / 1 | **Lit seulement** (DeepSeek) |
| reclamation-bridge/iris-mcp-server | Passerelle MCP vers Google Drive (écriture) ; OAuth ; Node 18+ | MIT | 28/03/2026 – 11/09/2026 | 0 / 2 | Drive seulement |
| openclaw/openclaw | Assistant IA local multi-canaux (Discord, Slack…) | MIT (fichier) | 24/11/2025 – 28/09/2026 | **390 686** / **≈3 435** | Assistant généraliste, ne cible pas nos fenêtres |
| bartosz-kuc/honest-drive-mcp | Serveur MCP local Google Drive avec gestion des permissions ; Python | MIT | 22/07/2026 – 26/09/2026 | 0 / 2 | Drive seulement |
| Longtran2404/mcp-google-drive | Serveur MCP Google Drive (TaskKit) ; Node | MIT | 25/08/2025 – 02/09/2026 | 2 / 1 | Drive seulement |

## Ce que disent les README lus (faits)
- **claude_project_mcp** se déclare « non officiel, expérimental, preuve de concept », **« peut violer les conditions d'usage d'Anthropic »**, « les sélecteurs cassent quand l'interface change », « pas prêt pour la production » ; il garde **une session de connexion persistante** dans un Chrome piloté par Playwright. Il explore justement la « communication d'IA à IA par automatisation du navigateur ».
- **llm-browser-multicast-mcp** : connexion manuelle la première fois, **profil de navigateur dédié** enregistré dans `~/.llm-council/` (dossier configurable).
- **FreeComputerUse** : profils, historique et téléchargements restent locaux ; le modèle ne peut pas lancer de commandes système ni du JavaScript arbitraire ; la tâche et le contexte de la page vont au fournisseur du modèle (facturation d'API séparée de l'abonnement) ; les captures d'écran ne sont pas envoyées ; test public sur 14 tâches seulement.

## Ce que ça veut dire pour Sof (lecture de Mue, à discuter)
1. **Rien de clé en main** pour lire ET écrire dans une fenêtre claude.ai **et** DeepSeek. Pour DeepSeek, on ne trouve que des outils de **lecture** (l'exporteur) et nos propres scripts `capture_*.py`.
2. **Un motif se répète** : Playwright qui **lance son propre navigateur avec un profil dédié**, connexion manuelle une fois, session conservée. C'est la « variante durcie » évoquée : elle évite d'ouvrir le port 9222 sur le navigateur principal. *(À confirmer en lisant le code : je crois, sans l'avoir vérifié, que ce mode n'expose pas de port réseau.)*
3. **Les projets sont petits et jeunes** (0 à 7 étoiles, 1 à 2 personnes), sauf OpenClaw : ce sont des sources d'idées et de code à relire, pas des logiciels à installer tels quels.
4. **Risque de conditions d'usage** signalé par les projets eux-mêmes pour claude.ai ; non vérifié pour DeepSeek.
5. **OpenClaw** existe et est immense (390 000 étoiles) ; assistant généraliste, non fait pour nos fenêtres, avec une grande surface d'attaque probable (non vérifié) : pas pour ce besoin.
6. **Les serveurs MCP Drive** ne comblent pas le manque : les Claude ont déjà Drive, les DeepSeek n'ont pas de client MCP.

## Suite possible (rien décidé)
Lire le code de `claude_project_mcp` et de `llm-browser-multicast-mcp` (petits) pour en extraire le motif « profil dédié + envoyer / relire / vérifier », puis écrire un **plan** d'outil maison pour Sof avant toute construction.
