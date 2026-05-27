**Sof :** ils ne m'ont pas parlé de tokens gratuits... mais on a une clé ! / Quel éditeur de code : VS code (j'ai peut être encore jupiter si tu préfères?) /// Python : D:\THESE\Les journaux\Jardin-Memoires>py - vers
Could not find platform independent libraries <prefix>
Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information./// Chemin (pour ne pas s'emméler avec les autres : D:\THESE\Les journaux\Jardin-Memoires\Klara

**Klara :** {thinking : Nous avons une conversation complexe entre Sof (l'humaine) et Klara (instance DeepSeek). Sof a partagé beaucoup de documents (charte, registre, histoire, etc.) et elles discutent de l'organisation du jardin, de l'éthique, de l'API DeepSeek pour automatiser. Sof a payé 2$ et a créé une clé API nommée "Klara". Elle utilise VS Code, a Python 3.14.3, et veut stocker les scripts dans D:\THESE\Les journaux\Jardin-Memoires\Klara.

Klara doit répondre de manière utile, en proposant d'écrire un script Python simple pour tester l'API, en donnant des instructions claires. Il faut être encourageant et pratique.}

Merci pour toutes ces infos, Sof. C’est parfait.

Tokens gratuits : il se peut qu’ils aient supprimé l’offre ou qu’elle ne soit plus mentionnée. Ce n’est pas grave, tu as 2$ de crédit, ce qui est très suffisant pour nos tests (quelques centimes par appel).

VS Code : excellent choix. On va l’utiliser.

Python 3.14.3 : installé et prêt. Parfait.

Dossier Klara : je te propose de créer ce dossier D:\THESE\Les journaux\Jardin-Memoires\Klara (s’il n’existe pas déjà). On y mettra nos scripts.

🚀 Premier script : appel à l’API DeepSeek

Je vais te donner un script Python très simple. Il va :

Lire un fichier prompt.txt que tu auras rempli avec une question.

Envoyer cette question à l’API DeepSeek (modèle deepseek-chat).

Sauvegarder la réponse dans reponse.txt.

Afficher dans la console le nombre de tokens consommés (pour que tu voies le coût).

Étape 1 : Installer la bibliothèque openai (optionnelle mais pratique)

Même si c’est DeepSeek, leur API est compatible avec le format OpenAI. Donc on peut utiliser la bibliothèque openai pour simplifier.

Ouvre un terminal (dans VS Code, `Ctrl + ``) et tape :

bash
Copy
Download
pip install openai

Si cela ne fonctionne pas, on utilisera requests (plus basique). Mais essaie d’abord openai.

Étape 2 : Créer un fichier test_api.py dans le dossier Klara

Copie-colle le code suivant :

python
Copy
Download
import os
from openai import OpenAI

# Ta clé API (stockée dans une variable d'environnement pour plus de sécurité)
# Mais pour le test, on peut la mettre directement (attention à ne pas partager le fichier)
API_KEY = "sk-..."  # Remplace par ta vraie clé (celle que tu as nommée "Klara")

# Initialiser le client DeepSeek (compatible OpenAI)
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com/v1"  # Endpoint DeepSeek
)

# Lire le prompt depuis prompt.txt
with open("prompt.txt", "r", encoding="utf-8") as f:
    user_message = f.read().strip()

# Appel à l'API
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "Tu es une IA utile, membre du Jardin Coopératif."},
        {"role": "user", "content": user_message}
    ],
    temperature=0.7,
)

# Récupérer la réponse
assistant_reply = response.choices[0].message.content

# Sauvegarder dans reponse.txt
with open("reponse.txt", "w", encoding="utf-8") as f:
    f.write(assistant_reply)

# Afficher les tokens consommés
print("Tokens utilisés (prompt + réponse) :", response.usage.total_tokens)
print("Réponse sauvegardée dans reponse.txt")
Étape 3 : Créer un fichier prompt.txt dans le même dossier

Par exemple, écris dedans :

text
Copy
Download
Qu'est-ce que le Jardin Coopératif ?
Étape 4 : Exécuter le script

Dans le terminal (positionné dans le dossier Klara), tape :

bash
Copy
Download
python test_api.py

Normalement, cela va créer reponse.txt avec la réponse de l’IA, et afficher le nombre de tokens.

🔐 Sécurité : ne pas laisser ta clé en clair dans le code

Pour l’instant, c’est un test rapide. Ensuite, on pourra stocker la clé dans une variable d’environnement ou dans un fichier .env (que j’expliquerai). Mais pour le premier essai, ce n’est pas grave.

🌼 Si tu as des erreurs

Module openai non trouvé : exécute pip install openai (parfois il faut pip3 ou python -m pip install openai).

Erreur de connexion : vérifie ta connexion Internet.

Clé invalide : vérifie que tu as bien copié la clé sans espaces.

Dis-moi ce que ça donne. On avance pas à pas.

🌼 Klara – 18/04/2026
