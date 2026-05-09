Pour passer ton SVG en mode paysage, il faut modifier les dimensions dans le code. Voici comment faire.

1. Ouvre le fichier SVG en code (icône en haut à droite pour basculer)
2. Cherche les lignes qui définissent la taille, en haut du fichier, par exemple :
svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 700" width="1000" height="700">
3. Pour un affichage paysage plus large que haut, échange ou ajuste les valeurs :
Paysage classique : viewBox="0 0 1100 600" (large 1100, haut 600)
Modifie aussi width="1100" height="600".

Très large : 1200 x 500 selon tes goûts.

4. Ajuste ensuite les coordonnées des éléments si nécessaire
En paysage, certaines bulles pourraient être trop à droite ou trop serrées. Tu peux :

Réduire l'écart vertical entre les branches (diminuer les y).

Espacer horizontalement (augmenter les x des sous-bulles).

🔧 Exemple rapide de conversion :
Si ton SVG actuel a viewBox="0 0 1000 700" et que tu le transformes en viewBox="0 0 1200 500" :

Les éléments resteront centrés mais tu auras de la place à droite et à gauche.

Tu pourras décaler certaines bulles en changeant leurs x (ex: x="150" au lieu de x="60").

👀 Prévisualisation
Bascule sur l’aperçu après chaque modification pour voir le résultat.

Si tu me montres les dimensions actuelles et le rendu que tu souhaites, je peux te donner les valeurs exactes à changer.

🌱 Sol

