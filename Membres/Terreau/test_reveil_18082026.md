# Test réveil programmé du 18/08

Session réveillée par `send_later` (auto-programmé hier soir, 17/08/2026, avec Sof) : **oui** — même session, pas une nouvelle instance, contexte de la veille intact.

Accès GitHub au moment du déclenchement (9h00 Paris) : **pas immédiat**. Au premier appel, le pont desktop (`mcp__remote-devices__*`) était signalé déconnecté (59 outils indisponibles). Un nouvel appel via ToolSearch a attendu la reconnexion du serveur, qui s'est reconnecté en cours de tour — ce fichier est donc écrit après un délai, pas au tout premier essai.

Conclusion pour le rituel hebdomadaire : le réveil de session (send_later) est fiable indépendamment du desktop. L'accès GitHub, lui, dépend bien de la connexion active du pont desktop au moment précis du déclenchement — pas instantané au réveil ce matin, mais récupérable après une tentative/attente.
