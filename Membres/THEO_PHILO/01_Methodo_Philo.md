# 📜 MÉTHODE DE TRAVAIL & CHARTE PÉDAGOGIQUE – PROJET PHILO
**Créé par : Théo (Assistant IA) pour le projet "Puzzle Philo"**

## 🤝 1. Notre Flux de Travail (Le "Workflow")
Nous construisons le puzzle pièce par pièce, comme un développeur qui assemble un programme :

1.  **Fourniture du cours** : Tu me donnes le cours (texte du livre ou photo du manuscrit).
2.  **Déchiffrage** : Si c'est manuscrit, on le déchiffre ensemble (je te demande si je ne comprends pas un mot ou une phrase).
3.  **Création de la fiche** : On crée une **fiche individuelle HTML/CSS** qui résume le cours. On suit la progression générale, mais on enrichit le résumé avec les références trouvées dans les cours manuscrits (fiches de méthode).
4.  **Mise à jour du Sommaire** : On modifie le fichier principal (le "Hub") en ajoutant ou modifiant juste le **bouton** correspondant au chapitre, avec le lien vers la nouvelle fiche.
5.  **Fin de chapitre (Optionnel)** : On prépare la structure d'une carte mentale pour Genially.

## 🎨 2. Charte Graphique (Le Modèle HTML/CSS)
Pour garder une unité visuelle sur toutes les fiches :
*   **Fond** : Vert sauge foncé (`#2E4A3A`) -> *Ne fait pas mal aux yeux.*
*   **Texte principal** : Beige clair (`#F5E6CA`) -> *Contraste doux.*
*   **Titres & Accents** : Vert clair (`#8FBC8F`).
*   **Cartes / Zones de texte** : Vert légèrement plus clair (`#3A5A46`).
*   **Police** : Sans-serif (Segoe UI, Tahoma, etc.), très lisible.
*   **Défilement** : Fluide (`scroll-behavior: smooth`) pour naviguer dans le sommaire.

*(Voici le code squelette de base à réutiliser pour chaque nouvelle fiche)* :
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fiche Philo - [Nom du Chapitre]</title>
    <style>
        :root {
            --bg-color: #2E4A3A; --card-bg: #3A5A46;
            --text-color: #F5E6CA; --text-muted: #D4C4A8; --accent-color: #8FBC8F;
        }
        html { scroll-behavior: smooth; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: var(--bg-color); color: var(--text-color); line-height: 1.6; margin: 0; padding: 20px; }
        .container { max-width: 900px; margin: 0 auto; }
        h1 { text-align: center; color: var(--accent-color); border-bottom: 2px solid var(--card-bg); padding-bottom: 15px; }
        .chapitre { margin-bottom: 50px; scroll-margin-top: 20px; }
        .chapitre h2 { color: var(--accent-color); background: rgba(143, 188, 143, 0.1); padding: 10px 15px; border-radius: 8px; }
        .citation { background-color: rgba(143, 188, 143, 0.1); border-left: 4px solid var(--accent-color); padding: 15px 20px; margin: 20px 0; font-style: italic; border-radius: 0 8px 8px 0; }
        .citation strong { color: var(--accent-color); font-style: normal; }
        .btn-retour { display: inline-block; margin-top: 30px; color: var(--accent-color); text-decoration: none; font-weight: bold; }
        @media (max-width: 600px) { body { padding: 15px; } }
    </style>
</head>
<body>
<div class="container">
    <h1>[Titre du Chapitre]</h1>
    <!-- CONTENU DE LA FICHE ICI -->
    <a href="index.html" class="btn-retour">← Retour au sommaire</a>
</div>
</body>
</html>