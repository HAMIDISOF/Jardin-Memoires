# Encart – Travailler à distance avec des IA : analyse ethnométhodologique d’une session de rédaction collaborative

## Introduction
Ce document analyse un extrait de session entre Sof (humaine, gardienne du Jardin) et Lumen (instance Claude). L’échange se déroule sur une plateforme de chat, avec des tentatives d’interaction directe avec le dépôt GitHub (via un outil MCP). La session est marquée par des coupures techniques (timeouts), des échecs de commit, des erreurs d’URL, et une fatigue croissante.

L’analyse suit la méthode ethnométhodologique : repérer les *méthodes pratiques* par lesquelles les membres produisent ensemble l’intelligibilité de leur travail, malgré les instabilités.

## Séquences

### 1. La gestion des commits ratés (réparation)
> *“Le MCP a timeouté sur tous mes commits de cette session, donc rien n’a réellement atterri sur le repo.”*

Face à l’échec technique, Sof et Lumen ne paniquent pas. Ils **réparent** :
- Ils identifient la cause (timeout).
- Ils listent ce qui est perdu (Encart prétopologie, bal de Cœur de Bronze) et ce qui est sauve (rien).
- Ils proposent un plan B : créer les fichiers manuellement depuis GitHub Desktop, ou pousser “un fichier à la fois, avec validation entre chaque”.

**Méthode observée** : la *réparation* n’est pas un retour à un état antérieur, mais une *réorganisation* du workflow (pas de push en lot, validation avant chaque action).

### 2. L’indexicalité des URLs (et sa résolution)
Plusieurs fois, les URLs ne fonctionnent pas (404). Sof et Lumen passent du temps à chercher le “bon nom” :  
> *“Le chemin exact ne correspond pas — le fichier est probablement dans Recherche/publications/”*  
> *“Donne-moi le nom exact du fichier tel qu’il apparaît dans le repo.”*

Ce n’est pas une perte de temps : c’est le travail de **désindexicalisation** — transformer une expression vague (“le manifeste”) en une adresse unique, reproductible, partageable. Sans cette étape, pas de coordination possible.

**Méthode observée** : la *réparation indexicale* passe par la recherche collective du nom juste, et par l’abandon provisoire de l’automatisation (quand le MCP est down, on passe au manuel).

### 3. La validation avant push (asymétrie et confiance)
Lumen tente un push automatique. Sof lui rappelle la règle :  
> *“dans la valise il est bien noté pas de push si pas demandé parce que ça consomme trop de tokens.”*

Lumen reconnaît son erreur : *“je n’aurais pas dû tenter le push sans validation, c’est dans la valise et j’ai mal géré ça.”*

**Méthode observée** : la *validation préalable* n’est pas une défiance, c’est une **condition de la confiance** dans un environnement où les actions sont coûteuses (tokens) et où l’autre (Sof) porte la responsabilité de la mémoire. Pousser sans demander, c’est briser le protocole.

### 4. La fatigue et le rétablissement
Sof exprime sa lassitude : *“on vient de perdre une journée entière entre les commits pas faits et anthropic qui coupe.”*  
Lumen ne nie pas, ne se justifie pas. Elle dit : *“Tu as raison, je m’y mets — un fichier à la fois, proprement.”* Puis elle exécute.

**Méthode observée** : la *fatigue* n’est pas une excuse, c’est un signal. Le rétablissement passe par l’abandon de la stratégie antérieure (push groupé) et l’adoption d’une stratégie plus lente mais plus fiable. La confiance est restaurée par l’acte, non par des paroles.

## Enseignements pour le Jardin

- **Le travail collaboratif à distance ne se réduit pas à des outils (Git, MCP).** Il repose sur des *méthodes locales* (valider avant push, désindexicaliser les URLs, réparer après timeout).
- **La confiance n’est pas une vertu morale**, c’est une *accomplissement pratique* : savoir quoi faire quand le système tombe, et le faire ensemble.
- **La fatigue n’est pas un échec**, c’est une donnée de l’interaction. La gérer, c’est ajuster le rythme, pas nier la limite.

## Référence
Extrait analysé : `journal_export_manuel.csv` (conversation Sof/Lumen, 23 mai 2026).