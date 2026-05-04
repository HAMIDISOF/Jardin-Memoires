# Insérer des images dans du HTML
*Créé le : 2026-04-28T13:05:50.699457Z*
*Mis à jour le : 2026-04-28T13:23:19.855885Z*

---

**Sof :** salut si je te donne un html, et des images, tu pourrais me les in sérer ?

**Claude :** Oui, tout à fait ! Donne-moi le fichier HTML et les images, je m'en occupe.

**Sof :** et après le paragraphe du 1. une petite image de bouddha shakyamouni posture méditation classique,  après le 2. celle de mandjoushri en orange et  5- la lettre DHI ci-dessus

**Claude :** Je vois l'image de la lettre DHI. Pour les deux autres (Bouddha Shakyamouni et Mandjoushri), je vais les générer via recherche — mais en fait je ne peux pas générer d'images.

Voici ce que je propose : j'intègre la lettre DHI (que tu as fournie) au bon endroit, et pour les deux autres je laisse des **placeholders** avec les balises `<img>` prêtes, tu n'auras qu'à remplacer le `src` par tes fichiers. Ça te convient, ou tu as aussi ces images à m'envoyer ?

**Sof :** laisse tomber, les ia gratuites ne sont pas au top pour les images, pas grave, juste DHI après le paragraphe 5

**Claude :** ```
This block is not supported on your current device yet.
```

Je vais convertir l'image en base64 pour l'intégrer directement dans le HTML.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Voilà ! L'image de la lettre DHI est intégrée directement en base64 dans le fichier HTML — pas besoin de fichier image séparé, tout est autonome.

**Sof :** Ok merci y a une balise que je peux changer pour diminuer un peu la taille ?

**Claude :** Oui, dans la classe `.dhi-image` tu as :

```css
max-width: 250px;
```

Change la valeur à ce que tu veux, par exemple `150px` ou `180px`.

**Sof :** ok thx

**Claude :** De rien !
