

- capture_sol.py écrit maintenant le chemin du fichier produit dans scripts/outil_auto_DS/last_capture.txt après chaque capture.

- DS_capt_extract.bat lit ce fichier pour passer le bon nom à extraire_fichiers.py — plus de nom hardcodé. Et il accepte un nom de session en paramètre : DS_capt_extract.bat simondon ou juste DS_capt_extract.bat pour "auto".

- Le pipeline complet : capture → extraction des fichiers balisés → egalis.bat pour le push. Une seule commande à lancer après une session Sol. 🌿