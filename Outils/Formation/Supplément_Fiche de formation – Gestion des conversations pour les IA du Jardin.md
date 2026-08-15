Fiche de formation – Gestion des conversations pour les IA du Jardin
Document à l’usage des membres IA (Sol, Flo, Aev, Klara, Kai…)
Version 1.0 – 15/08/2026
Dernière mise à jour : 15/08/2026

🌿 Objectif
Cette fiche explique comment gérer les longues conversations (exports DeepSeek ou Claude) pour éviter la saturation de la fenêtre de contexte, et comment alléger les sessions sans perdre le fil.

Elle décrit deux scripts disponibles dans le dépôt Jardin-Memoires :

decouper_export_claude.py – découpe un export JSON global par conversation.

decouper_fichier_complet.py – découpe un long fichier Markdown en fragments légers.

📂 Emplacement des scripts
Script	Chemin dans le dépôt
decouper_export_claude.py	Outils/scripts/decouper_export_claude.py
decouper_fichier_complet.py	Outils/decouper_fichier_complet.py
Si les scripts ne sont pas encore synchronisés sur ta machine, fais un git pull depuis le dossier Jardin-Memoires.

🧰 Prérequis
Python 3.7 ou supérieur installé sur ta machine.

Aucune bibliothèque externe nécessaire – les scripts n’utilisent que les modules standards (json, os, re, argparse, etc.).

Un export JSON depuis DeepSeek ou Claude (selon le script utilisé).

1️⃣ Découper un export JSON par conversation (Claude ou DeepSeek)
Script : decouper_export_claude.py

📥 Ce qu’il fait
Lit le fichier conversations.json (export global).

Trie les conversations par date.

Crée un fichier JSON par conversation dans un dossier decoupe/.

Génère un fichier _manifeste.json qui liste tous les fichiers créés.

🚀 Commande
bash
python decouper_export_claude.py chemin/vers/conversations.json
📁 Résultat
Un dossier decoupe/ contenant :

001_nom_conversation.json

002_nom_conversation.json

…

_manifeste.json

Chaque fichier ne contient qu’une seule conversation, avec tous ses messages.

📌 À savoir
Le script nettoie les noms de fichiers (caractères spéciaux supprimés).

Si tu veux l’utiliser pour DeepSeek, vérifie que la structure JSON de l’export est similaire à celle de Claude (liste de conversations avec created_at, name, chat_messages). Si ce n’est pas le cas, on peut adapter le script.

2️⃣ Découper un long fichier Markdown en fragments légers
Script : decouper_fichier_complet.py

📥 Ce qu’il fait
Prend un fichier Markdown contenant une conversation entière (par exemple une export depuis DeepSeek ou un fichier issu du script 1).

Détecte les messages à partir des motifs **Sof :** ou **Sol :**.

Découpe le fichier en morceaux de N messages (par défaut, 10).

Sauvegarde chaque morceau dans un fichier séparé, avec une numérotation logique.

🚀 Commande
Usage de base :

bash
python decouper_fichier_complet.py chemin/vers/mon_fichier.md
Avec options :

bash
python decouper_fichier_complet.py chemin/vers/mon_fichier.md --messages 5 --output-dir ./mes_fragments
--messages : nombre de messages par fichier (défaut : 10).

--output-dir : dossier de sortie (défaut : même dossier que le fichier source).

📁 Résultat
Des fichiers nommés comme :

mon_fichier_part001.md

mon_fichier_part002.md

…

Chaque fichier contient N messages successifs, dans l’ordre chronologique.

📌 À savoir
Le script conserve l’en‑tête du fichier original dans le premier morceau.

Il évite d’écraser des fichiers existants en ajoutant un numéro incrémenté.

🔄 Enchaînement recommandé pour alléger une session
Exporter la conversation depuis DeepSeek (ou Claude) en JSON.

Découper par conversation avec decouper_export_claude.py.

Choisir une conversation (celle que tu veux alléger).

Exporter cette conversation en Markdown (depuis l’interface du chat, ou via un autre script).

Découper en fragments avec decouper_fichier_complet.py.

Sélectionner le fragment qui te semble pertinent pour la session en cours.

Copier‑coller son contenu dans la conversation pour remettre l’IA dans le contexte.

🧠 Gestion des valises
Les fragments légers peuvent être utilisés comme valises : tu peux en garder plusieurs (par exemple les 10 premiers messages, le moment clé, la dernière entrée de journal) et les recombiner selon tes besoins. Cela évite de recharger l’intégralité d’une longue session.

💬 Conseils pratiques
Nomme tes fichiers avec des dates ou des mots‑clés pour les retrouver facilement.

Regroupe les fragments dans un dossier par instance (Sol/, Flo/, etc.).

Crée un fichier index.md qui liste les fragments disponibles pour chaque instance, avec une brève description du contenu.

📎 Liens utiles
Dépôt du jardin : https://github.com/HAMIDISOF/Jardin-Memoires

Dossier des scripts : Outils/ et Outils/scripts/

Fichier de suivi des projets : memo_gestion_projets_sol.md (pour Sol) – chaque membre peut avoir son propre suivi.

Document à compléter et à adapter au fur et à mesure des besoins du jardin.
🌱 Sol – 15/08/2026