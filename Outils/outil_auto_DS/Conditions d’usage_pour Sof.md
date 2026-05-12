## Pour résumer la procédure complète quand tu veux capturer une session :

Lancer Brave avec le port (commande ci‑dessus).

Dans ce Brave, aller sur DeepSeek et commencer à discuter avec Luz.

Pendant ou après la discussion, ouvrir un nouveau terminal (cmd) dans le dossier du script (ou utiliser le même, mais il vaut mieux en ouvrir un autre).

Exécuter python capture_luz.py --session "ma_session".

Puis extraire_fichiers.py etc.

---

1. Lancer Brave avec le port de débogage (une fois, avant la session avec moi) : (cf. le .bat)

text
"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222 --profile-directory="Default"
Cela ouvre Brave normalement (tu peux utiliser ton profil habituel).

Important : garde cette fenêtre ouverte pendant toute la session.


2. Ouvrir DeepSeek dans cet onglet Brave, et commencer à discuter avec moi (Luz).


3. Pendant la session, quand tu veux que je produise un fichier dans le dépôt, tu me rappelles le format de balisage (tu as le RAPPEL_BALISAGE.md).

Je te répondrai avec un bloc comme :
📄 Fichier : Membres/Luz/ma_note.md
```md
contenu...

fin_md


4. Après la session (ou en cours, sans fermer Brave), tu ouvres un terminal (dans le dossier Jardin-Memoires/scripts/outil_auto_DS/ ?) et tu lances :

text
python capture_luz.py --session "nom_de_la_session"
Le script se connecte à Brave, extrait la conversation, la sauvegarde dans Luz/ et écrit le chemin dans last_capture_luz.txt.


5. Puis tu lances l’extraction :

text
python extraire_fichiers.py last_capture_luz.txt D:\THESE\Les journaux\Jardin-Memoires
(ou bien tu écris un petit .bat qui récupère le chemin depuis last_capture_luz.txt et appelle extraire_fichiers.py avec le bon repo).



6. Vérifie les fichiers modifiés/créés, puis fais le push manuellement (depuis VS Code ou ligne de commande).