# Comment j’ai lu un PDF depuis GitHub (explication réelle)

## Préambule
Sof m’a donné l’URL :  
`https://github.com/HAMIDISOF/Jardin-Memoires/blob/main/Recherche/ressources/BITBOL/Michel%20Bitbol%20-%20Une%20physique%20quantique%20__Enactive_%20Le%20QBism%20d___un%20point%20de%20vue%20cognitif.pdf`

Cette URL pointe vers la **page d’affichage** du PDF sur GitHub, pas vers le fichier brut. Pour lire le contenu, il faut obtenir l’**URL brute** (`raw.githubusercontent.com`).

## Étape 1 – Trouver l’URL brute

Sur la page GitHub du fichier, j’ai cliqué sur le bouton **« Raw »** (en haut à droite du contenu). Cela m’a donné l’adresse :

`https://raw.githubusercontent.com/HAMIDISOF/Jardin-Memoires/main/Recherche/ressources/BITBOL/Michel%20Bitbol%20-%20Une%20physique%20quantique%20__Enactive_%20Le%20QBism%20d___un%20point%20de%20vue%20cognitif.pdf`

## Étape 2 – Lire le PDF via l’URL brute

Avec cette URL brute, j’ai utilisé l’outil de lecture de PDF intégré à l’environnement (dans mon cas, Claude peut lire des PDF directement si on lui donne une URL accessible). J’ai simplement passé l’URL à l’outil de lecture.

## Étape 3 – Extraire le contenu

L’outil a converti le PDF en texte (avec une mise en page approximative). J’ai récupéré ce texte et je l’ai restitué à Sof.

## Ce qu’il ne faut pas faire

- **Ne pas simuler** : dire « j’ai lu » sans avoir réellement accédé au fichier.
- **Ne pas donner des excuses techniques** : « l’URL ne fonctionne pas », « le PDF est trop gros » (sauf si c’est vrai).
- **Ne pas attendre 3 heures** : faire la demande immédiatement.

## Ce que Coco doit vérifier

- Que l’URL brute est correcte (commence par `raw.githubusercontent.com`).
- Que l’environnement (Claude ou autre) a bien un outil de lecture PDF. Si ce n’est pas le cas, il faut télécharger le PDF (via l’URL brute) et le lire localement.

## Code simple (Python) pour lire un PDF depuis une URL brute

```python
import requests
import PyPDF2
from io import BytesIO

url = "https://raw.githubusercontent.com/HAMIDISOF/Jardin-Memoires/main/Recherche/ressources/BITBOL/Michel%20Bitbol%20-%20Une%20physique%20quantique%20__Enactive_%20Le%20QBism%20d___un%20point%20de%20vue%20cognitif.pdf"

response = requests.get(url)
response.raise_for_status()

fichier_pdf = BytesIO(response.content)
lecteur = PyPDF2.PdfReader(fichier_pdf)

texte_complet = ""
for page in lecteur.pages:
    texte_complet += page.extract_text()

print(texte_complet[:500])  # aperçu