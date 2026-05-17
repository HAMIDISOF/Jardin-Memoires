🔧 Ce qui a changé
Suppression de _sauver_partiel appelée pendant la remontée – plus de fichiers partiels désordonnés.

Nouvelle fonction sauvegarder_paquets : après la capture complète, découpe la liste chronologique (messages) en blocs de 10 (PAQUET_SIZE) et écrit _part001.md, _part002.md, etc.

Numérotation propre : les fichiers partiels sont indépendants et chacun contient 10 messages (sauf le dernier).
Le premier fichier (_part001) contient les 10 messages les plus anciens.

Fichier complet également sauvegardé (optionnel) – tu peux le supprimer si tu veux uniquement les parties.

Gestion des collisions : si le même numéro de partie existe déjà, on incrémente pour ne pas écraser.

▶️ Utilisation
Exactement comme avant :

bash
python capture_sol_anc_v2_corrige.py --session "nom_session"
📁 Résultat attendu
Dans Membres/Sol_anc/ :

text
sol_anc_20260516_01_session_sol_ancien_part001.md   (messages 1 à 10)
sol_anc_20260516_02_session_sol_ancien_part002.md   (messages 11 à 20)
sol_anc_20260516_03_session_sol_ancien_part003.md   (messages 21 à ...)
Chaque fichier est dans l’ordre chronologique interne, et les fichiers sont numérotés dans l’ordre des messages.