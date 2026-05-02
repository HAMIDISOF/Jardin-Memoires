

- capture_sol.py écrit maintenant le chemin du fichier produit dans scripts/outil_auto_DS/last_capture.txt après chaque capture.

- DS_capt_extract.bat lit ce fichier pour passer le bon nom à extraire_fichiers.py — plus de nom hardcodé. Et il accepte un nom de session en paramètre : DS_capt_extract.bat simondon ou juste DS_capt_extract.bat pour "auto".

- Le pipeline complet : capture → extraction des fichiers balisés → egalis.bat pour le push. Une seule commande à lancer après une session Sol. 🌿


Au : 02/05/2026
Le flux de travail
Brave est lancé avec un port de débogage (9222).

Le script capture_sol.py se connecte à cet onglet, extrait les messages (Sof et Sol) en analysant le DOM, et les sauvegarde dans un fichier .md (dans Sol/).

Le fichier est nommé automatiquement : sol_YYYYMMDD_NN_nom_session.md.

extraire_fichiers.py lit ensuite ce fichier, cherche les blocs balisés (📄 Fichier : ou 📄 Ajout :), et écrit ou complète les fichiers correspondants dans le repo.

Enfin, DS_capt_extract.bat enchaîne capture, extraction, et git push.

2. Ce que ça change pour moi (Kai)
Ce pipeline est actuellement paramétré pour Sol (dossier Sol/, sélecteurs CSS peut-être spécifiques à Sol). Pour l’adapter à moi (Kai), il faudrait :

Créer un script capture_Kai.py (ou modifier celui de Sol) :

Changer les sélecteurs CSS si nécessaire (les classes ds-markdown, fbb737a4 sont probablement les mêmes pour tous, mais les ds-think-content peuvent être identiques).

Changer le répertoire cible : Kai/ au lieu de Sol/.

Adapter le nommage (kai_...md).

Copier extraire_fichiers.py (il est générique, il n’a pas besoin d’être modifié).

Créer un .bat similaire pointant vers la bonne capture.

3. La balise que je devrai utiliser
Le fichier RAPPEL_BALISAGE.md est crucial. Désormais, quand je veux créer ou modifier un fichier dans le repo (mon journal, mon doc projet, une note, etc.), je devrai respecter strictement le format 



Instructions d’utilisation
Placer capture_Kai.py dans scripts/outil_auto_DS/

Placer DS_capt_extract_Kai.bat dans le même dossier (ou à la racine, au choix).

Avant de lancer, ouvrir Brave avec :
"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222 --profile-directory="Default"

Naviguer vers DeepSeek et commencer l’échange.

Lancer DS_capt_extract_Kai.bat [nom_session]

Les fichiers balisés (écrits avec le format 📄 Fichier : ...) seront automatiquement extraits et pushés.