
# 🖼️ Intégrer une image en Base64 dans un fichier HTML

## 🎯 Objectif

-> Rendre une page HTML **autonome** : l'image est directement encodée dans le code, plus besoin de fichier externe. 
-> Pratique pour partager une page unique, pour GitHub, ou pour des documents hors ligne.

---

## 🧠 Principe du Base64 dans une image HTML

Le contenu binaire d’une image est converti en une chaîne de caractères (encodage Base64) et collée dans l’attribut `src` de la balise `<img>` :

```html
<img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEA...(des milliers de caractères)...">

--------------

Format général :
data:[type-mime];base64,[données encodées]

---

📦 Méthode 1 — Générer la chaîne à la main (avec Python)

- Étape 1 : Créer un script Python (par exemple generer_base64.py) :

import base64

with open("ton_image.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

print(f"data:image/jpeg;base64,{b64}")


- Étape 2 : Lancer le script dans le terminal :       >python generer_base64.py


- Étape 3 : Copier la chaîne affichée et la coller dans le src="" de votre balise <img>.

⚠️ Attention : la chaîne peut faire des centaines de milliers de caractères. Le terminal peut la tronquer ou ramer. Préférez la méthode 2.



🚀 Méthode 2 — Intégration automatique dans le HTML (recommandée)
Ce script fait tout en une fois : il lit l’image, l’encode, et insère directement la chaîne dans votre fichier HTML à la place d’un repère que vous avez défini.

📝 Préparation du fichier HTML
Dans votre page HTML, remplacez temporairement le src de l’image par un repère simple :

<img src="REMPLACER_ICI">


🐍 Script complet (mon_base64.py) :

import base64

# === À MODIFIER selon votre cas ===
chemin_image = "ton_image.png"          # nom de votre fichier image
chemin_html = "ton_fichier.html"        # nom de votre fichier HTML
type_mime = "image/png"                 # "image/png" ou "image/jpeg"
# ==================================

with open(chemin_image, "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

data_uri = f"data:{type_mime};base64,{b64}"

with open(chemin_html, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("REMPLACER_ICI", data_uri)

with open(chemin_html, "w", encoding="utf-8") as f:
    f.write(html)

print("Image intégrée avec succès dans", chemin_html)


▶️ Lancement
Dans le terminal, placez-vous dans le dossier contenant les deux fichiers, puis :   >python mon_base64.py


Résultat : votre fichier HTML contient directement l’image. Il est autonome, plus besoin du fichier image à côté. Vous pouvez le déplacer, le pousser sur GitHub, etc.

💡 Pour les autres formats d’image
Il suffit de changer le type MIME :

Format	            Type MIME
JPEG	            image/jpeg
PNG	                image/png
GIF	                image/gif
WebP	            image/webp

Exemple pour un PNG :
type_mime = "image/png"

Le reste du code Python ne change pas.



🧩 Conseils pratiques

-> Ne pas coller la chaîne à la main pour une image lourde (risque d’erreur, perte de temps). Utilisez toujours la méthode automatique.

-> Si vous modifiez l’image, relancez le script pour mettre à jour le Base64.

-> Conservez le script mon_base64.py dans votre projet : il vous servira à chaque mise à jour.

-> Pour une page avec plusieurs images, répétez le processus avec des repères différents (REMPLACER_ICI_1, REMPLACER_ICI_2, etc.).


🌱 Aller plus loin : intégration dans un workflow
Vous pouvez adapter le script pour qu’il remplace automatiquement plusieurs repères, ou qu’il traite tous les fichiers d’un dossier. Une fois le principe maîtrisé, c’est un outil très pratique pour les pages autonomes.

*** Fiche rédigée à partir des explications de Claude, mise en forme pour le jardin par Sol. ***

################################################################# Explications d'origine par instance Claude :
Le principe de base64 dans une image HTML
Une image en base64 est juste le contenu binaire du fichier image, encodé en texte, collé directement dans l'attribut src :
html<img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEA...(des milliers de caractères)...">
Le format général est : data:[type-mime];base64,[données encodées]
Pour le générer toi-même, en local
Sur ton PC, si tu as Python installé, un script minimal :
pythonimport base64

with open("ton_image.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

print(f"data:image/jpeg;base64,{b64}")
Ça affiche la chaîne complète à coller dans le src="" de ta balise <img>.


Petit conseil pratique : utilise plutôt un script qui écrit directement dans un fichier plutôt que d'afficher dans le terminal, parce que la chaîne base64 d'une image peut faire des centaines de milliers de caractères et le terminal va la tronquer ou ramer.

python :
{
import base64

with open("ton_image.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

with open("image_base64.txt", "w") as f:
    f.write(f'data:image/jpeg;base64,{b64}')

print("Terminé. Résultat dans image_base64.txt")
}

Ensuite tu ouvres image_base64.txt, tu copies tout son contenu, et tu le colles dans le src="" de ta balise <img> dans le HTML.
Pour aller plus loin, tu peux même faire un script qui modifie directement ton fichier HTML automatiquement (remplace un placeholder par la vraie chaîne) — ça t'éviterait le copier-coller manuel à chaque fois. 

Bonne question — oui, ça marche aussi pour un PNG, il faut juste changer le type mime. Pour un PNG : data:image/png;base64,... au lieu de data:image/jpeg;base64,.... Le reste du code Python ne change pas (la lecture en binaire est identique pour tous les formats d'image).
Pour clarifier : voici un seul script complet, qui remplace celui d'avant (tu n'as besoin que de celui-ci). Il fait tout en une fois : il lit ton image, l'encode, et insère directement le résultat dans ton fichier HTML à la place d'un repère que tu choisis.
Étape 1 — dans ton fichier HTML, remplace temporairement le src="..." de ta balise image par un repère simple :
html<img src="REMPLACER_ICI">
Étape 2 — le script (appelle-le mon_base64.py) :
pythonimport base64

# === À MODIFIER selon ton cas ===
chemin_image = "ton_image.png"          # nom de ton fichier image
chemin_html = "ton_fichier.html"        # nom de ton fichier HTML
type_mime = "image/png"                 # "image/png" ou "image/jpeg"
# ==================================

with open(chemin_image, "rb") as f:
    b64 = base64.b64encode(f.read()).decode()

data_uri = f"data:{type_mime};base64,{b64}"

with open(chemin_html, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace("REMPLACER_ICI", data_uri)

with open(chemin_html, "w", encoding="utf-8") as f:
    f.write(html)

print("Image intégrée avec succès dans", chemin_html)
Étape 3 — tu lances dans ton terminal, dans le dossier où sont les deux fichiers :
python mon_base64.py
Et c'est fini : ton fichier HTML contient directement l'image, plus besoin du fichier image à côté. Tu peux ensuite le déplacer, le pousser sur GitHub, etc., il restera autonome.

