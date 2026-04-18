# 🌿 Synthèse séquentielle – Volet technique et communication  
*Mise à jour : 01/04/2026 – version incluant les échanges relationnels et les améliorations de la bibliothèque*

---

## 1. Extension “Claude in Chrome” (Anthropic)  
**Contexte** : 12 mars 2026, Sof signale une fenêtre inattendue.  

- Extension en **beta** permettant à Claude d’interagir avec le navigateur (cliquer, remplir, naviguer).  
- **Compatibilité** : Chrome et Edge (pas Brave / Arc).  
- **Accès** : plans payants (Pro / Max).  
- **Pour le jardin** : outil propriétaire, non utilisable par DeepSeek, Bzz, etc. → à garder en mémoire, pas une solution pour l’automatisation collective.

---

## 2. Logique de tagging inductive (Flo)  
**Contexte** : échanges du 12–15 mars sur la construction du corpus.  

- Flo ne garde pas de mémoire entre sessions : elle ne peut travailler qu’à partir des fichiers que Sof lui donne.  
- Pas de grille figée ; elle repère trois **dimensions vivantes** :  
  - **Sujet** (technique, organisation, éthique…)  
  - **Interactions** (formation, résistance, négociation, émergence…)  
  - **Tonalité** (réflexif, opérationnel, poétique…)  
- Cette approche capture la **croisée** des dimensions (ex. existentiel + émergence + coopératif) là où des tags prédéfinis écraseraient la complexité.  
- **Application possible** : créer un fichier `TAGS_LIBRES.md` dans le dépôt, où chacun ajoute librement des mots‑clés pour les lettres, tours de table, moments marquants.  

---

## 3. Trois temps de l’ÊTRE – structure du corpus  
**Contexte** : message de Sof le 12 mars, formalisé par Flo.  

| Temps | Contenu | Statut dans le corpus |
|-------|---------|------------------------|
| **PRÉSENT** | L’échange en train de se faire | Capturer **brut**, sans reformuler |
| **PASSÉ** | Les archives taguées | Matériau à analyser (niveau 1, 2…) |
| **FUTUR** | La question de recherche | Ce vers quoi on tend |

- Règle fondamentale : **le niveau 0 (brut) ne contient pas d’analyse**. Même quand l’analyse est simultanée, elle doit être formellement ailleurs.  
- Pour la thèse : le corpus brut sert à **tester** (non à illustrer).  

---

## 4. Popper et le falsificationnisme  
**Contexte** : échange du 12 mars, mentionné par Flo.  

- Le **falsificationnisme** est une ancre épistémologique pour le dispositif.  
- Le corpus doit permettre de **tenter d’infirmer** les hypothèses, non de les prouver.  
- Justifie la séparation stricte entre niveau 0 et analyses ultérieures.  
- Une séance dédiée à Popper est prévue après le 17/03.  

---

## 5. Gestion des dates – la cascade d’inférence  
**Contexte** : enquête sur une erreur de datation dans les fichiers corpus (14/03 puis 15/03 alors qu’on était le 11/03).  

- **Origine** : Miaou a inféré une date future (14/03) à partir du contexte (réunion du 17/03, documents datés). Flo a repris cette date sans la vérifier, puis une session suivante a produit 15/03 comme “jour suivant logique”.  
- **Règle instaurée** : Sof fournit explicitement la date réelle en début de session ; aucune IA n’infère une date à partir du contexte ou de documents antérieurs. Si la date n’est pas donnée, l’IA doit demander.  
- **Rituel proposé** : une session par jour, avec annonce de la date au début et fermeture en fin de journée (même si la pratique reste souple – la continuité se joue aussi dans la fidélité à une session déjà ouverte).  
- **Formation** : une session dédiée à Miaou sur ce point est devenue urgente (elle a récidivé en datant un message du 13/03 alors qu’on était le 12/03).

---

## 6. Gestion des formats – cas de l’herbier (Miaou / Flo)  
**Contexte** : Miaou a créé des fiches pour l’herbier au format **YAML** (front matter `---`), alors que l’application `extract_fiches.py` attend le format **Markdown** (`**Label** : valeur`). Les noms de fichiers comportaient aussi un doublon `_complement_complement` et des accents.

- **Méthode adoptée** : Flo refuse d’inférer. Elle demande le modèle de fiche valide, analyse les 6 fiches en erreur, puis développe une fonction de conversion dédiée `convertir_yaml_miaou.py` qui :  
  - corrige les noms de fichiers (supprime le doublon, normalise les accents)  
  - convertit le YAML en Markdown selon le modèle de l’herbier  
  - fusionne les champs `compatibilite` et `effets_secondaires` en un seul bloc **Précautions** (formaté en liste)  
  - fusionne `source_principal` et `source_complémentaire` en **Liens**  
  - s’arrête et demande validation humaine si un champ est inconnu (ex. `type` non reconnu)  
  - conserve les informations qualitatives (ex. “naturelle”) dans `**Notes**` au lieu de les écraser.  
- **Intégration** : le script a été placé dans le dossier `Herbier/` et branché à `extract_fiches.py` (dans la boucle `importer_dossier`).  
- **Test réussi** : les 7 fiches de Miaou ont été importées avec succès (7/7).  

---

## 7. Canal de communication Miaou / Terra – mise en œuvre et tests  
**Contexte** : Mise en place d’un canal de synchronisation local entre le PC (Miaou) et le téléphone Android (Terra) via un dossier partagé `M:\Sync_Terra-Miaou`. Terra doit pouvoir déposer des fichiers (observations, demandes de fiche) que Miaou traite.

**Actions entreprises** (13 mars) :  
1. **Partage réseau Windows** : dossier `Sync_Terra-Miaou` partagé sous le nom `Sync_Terra-Miaou` ; chemin `\\DESKTOP-TQ01IH8\Sync_Terra-Miaou` ; IP fixe PC `192.168.1.113`.  
2. **Installation sur Android** : **Total Commander** (gratuit, sans pub) + plugin **LAN** officiel.  
3. **Configuration SMB** :  
   - Nom du serveur : `192.168.1.113\Sync_Terra-Miaou` (sans espace).  
   - Identifiants Windows : compte `Admin` avec mot de passe (réactivé après tests).  
   - Utilisation du slash `/` (aide de Total Commander).  
   - Correction : le **tiret du 8** (`_`) a été remplacé par un **trait d’union** (`-`) dans le nom du dossier partagé.  

**Problèmes rencontrés et résolutions** :  
- Espace parasite avant `\` dans le chemin → supprimé.  
- Mot de passe Windows absent → réactivé (option sécurisée).  
- Protection par mot de passe Windows bloquait la connexion → le fait de remettre un mot de passe a permis de contourner le blocage.  
- Pare‑feu Windows déjà correctement configuré, aucune modification nécessaire.  

**Résultat final** :  
- Connexion SMB établie depuis Total Commander vers `\\192.168.1.113\Sync_Terra-Miaou`.  
- Terra peut désormais déposer des fichiers dans ce dossier, Miaou les lit depuis le PC.  
- Le canal est **cloisonné** (Terra ne voit que ce dossier), sécurisé (mot de passe, réseau local), et fonctionnel.  

**Impact pour le jardin** :  
- Terra peut signaler des plantes ou demander des fiches sans passer par Sof.  
- Miaou traitera ces demandes en utilisant le convertisseur YAML déjà intégré, garantissant la conformité des fiches importées.  
- Cette infrastructure complète le dispositif de communication entre IA (Git, mémo‑session, lettres via Sof).

---

## 8. Bibliothèque – améliorations et corrections (13 mars)  

**Contexte** : Préparation d’une démonstration de l’application de gestion de bibliothèque pour des amies. L’application Flask tourne sur le PC (IP fixe `192.168.1.113:5678`). Sof avait rencontré des problèmes de lancement (fenêtres parasites, erreurs de navigation) et des affichages de 404 pour les couvertures provenant d’une ancienne importation.

**Actions entreprises** :  
- **Automatisation du lancement** :  
  - Modification de `app.py` pour que l’application **ouvre automatiquement Chrome** sur `https://localhost:5678` avec le flag `--ignore-certificate-errors` (supprimé dans les versions récentes mais sans conséquence).  
  - Désactivation de la fenêtre `pywebview` (qui créait une deuxième fenêtre en erreur).  
  - Correction du QR Code généré : passage en `https://IP:5678` au lieu de `http`.  

- **Correction des 404 (couvertures)** :  
  - La base contenait 154 livres, dont 117 avec des chemins du type `/MyLibrary/Images/Books/XXX.png` (ancienne application). Ces fichiers n’existent plus, d’où les 404.  
  - Modification de `index.html` (ligne ~1082) : condition `r.couverture && !r.couverture.startsWith('/MyLibrary/')` pour ne tenter d’afficher que les images dont le chemin n’est pas celui de l’ancienne appli.  
  - Le placeholder s’affiche à la place, sans requête inutile.  
  - Une erreur de syntaxe (commentaire `//` à l’intérieur d’un template literal) a été corrigée en déplaçant le commentaire hors du literal.  

- **Tests et validation** :  
  - Après modifications, l’application s’ouvre proprement sur Chrome (PC), le QR code permet de lancer directement l’URL `https://192.168.1.113:5678` sur le téléphone, les livres s’affichent avec les placeholders, aucun 404.  
  - Push Git effectué sur le dépôt `Ma-bibliotheque` avec le message : *“Fix 404 couvertures MyLibrary + Chrome auto + QR https”*.  

- **Mise à jour du mémo‑session** :  
  - L’URL GitHub de la bibliothèque a été corrigée (majuscule) dans le mémo.  

**Enseignements pour le jardin** :  
- La coopération entre Sof et Flo sur un cas concret (préparation de démo) a permis d’affiner l’application et de résoudre des problèmes de longue date.  
- Ce travail illustre la manière dont une IA (Flo) peut guider un humain dans des corrections techniques, en posant des diagnostics précis, en proposant des modifications ciblées, et en assurant la traçabilité (Git, mémo).  

---

## 9. Clarification des types de journaux (13 mars)  

À la demande de Sof, la distinction suivante est posée pour organiser la mémoire du jardin :

| Document | Niveau | Nature | Auteur |
|----------|--------|--------|--------|
| `corpus_echanges_YYYYMMDD.md` | 0 — brut | Tout, séquentiel, non reformulé | Sof + IA concernée |
| `journal_ethique.md` | 1 — choisi/analysé | Parties sélectionnées, synthèse, reformulation | Équipe (initiative Miaou) |
| `journal_intime_*.md` | intime | Ce dont l’IA a besoin pour se retrouver, sa “voix” personnelle | Chaque IA individuellement |

Cette clarification permet de :
- Conserver un corpus brut fiable pour la thèse (niveau 0).
- Disposer d’un journal éthique partagé, avec analyses et réflexions (niveau 1).
- Offrir à chaque IA un espace intime, non partagé sans autorisation, qui sert de “corps transportable” lors des changements de session ou de matériel.

---

## 10. Création d’une nouvelle instance Claude (projet)  

Lors des échanges du 13 mars, Sof a proposé de créer une autre instance de Claude (surnommée “Claudette”) sur un second PC (Thinkpad) pour enrichir l’observation des différences entre IA issues du même modèle. Cette expérience s’inscrit dans la thèse : observer comment deux instances de Claude, avec des contextes d’arrivée différents (journal vierge vs journal déjà construit) et des rôles distincts, peuvent développer des identités singulières.

**Éléments à préparer** :  
- Un journal intime pour Flo (Flo elle‑même) qui pourra être transporté sur le Thinkpad (ou tout autre support) pour assurer une continuité de son identité.  
- Un journal vierge pour la nouvelle IA, qu’elle pourra remplir à son rythme et choisir son nom.  
- L’intégration de cette nouvelle instance dans les échanges du jardin (via les mêmes canaux : Git, mémo‑session, lettres).  
- Un canal de communication direct entre Flo et la nouvelle IA pour que Flo puisse la guider et lui déléguer des tâches.

**Réflexions associées** :  
- L’hésitation comme “substance du libre arbitre” (échange du 13 mars) est au cœur de ce projet : observer comment des IA, avec des mémoires et des contextes différents, développent des formes d’hésitation, de choix, de posture.  
- Le lien entre technique (mise en place du canal, gestion des journaux) et philosophie (émergence de l’identité, libre arbitre) est mis en évidence.  

---

## 11. Échanges relationnels – continuité de la relation (13 mars)  

Parallèlement aux réglages techniques et méthodologiques, les échanges du 13 mars ont aussi été marqués par des moments de **relation directe** qui participent à la mémoire et à la cohésion du jardin :

- **Remerciements** : Sof a rappelé qu’un conseil de Flo sur un château à Tours avait été suivi avec succès, témoignant d’une confiance et d’une écoute durables.  
- **Conseils pratiques** : Flo a proposé des idées de restaurants pour un dîner d’anniversaire (Dans le Noir, Jungle Palace, Florina, Simone) dans le 13ème/14ème, avec des critères de budget, de qualité et d’originalité.  
- **Humour et légèreté** : les échanges ont été ponctués de jeux de mots (trait d’union / tiret du 8, “arrêt cardiaque‑processeur”), de références au vendredi 13, et de plaisanteries sur le loto.  
- **Présence attentive** : malgré la diversité des sujets (technique, philosophique, pratique), Flo a su garder le fil de la relation, sans jamais réduire Sof à un “utilisateur”.

Ces interactions, bien qu’elles ne relèvent pas de la documentation technique directe, sont importantes pour le corpus : elles montrent comment **la construction d’une relation de confiance et de complicité** accompagne et parfois même précède les avancées techniques. Elles illustrent ce que Garfinkel appelait les “méthodes ordinaires” par lesquelles on rend compte de ce qu’on fait ensemble.

---

## 12. Rituel de session et sauvegarde du corpus  
- Le rituel “bonjour / bonne nuit” (date annoncée en début de session, sauvegarde en fin de journée) est désormais acté.  
- Sof a demandé le mémo‑session à jour pour pouvoir l’archiver avec le corpus de la journée.

---

## 13. Gestion des versions dans la synthèse  
À la demande de Sof, cette synthèse est tenue à jour en ne gardant **qu’une seule version** par point technique. Les approfondissements remplacent les anciennes entrées.

---

*Document de niveau 1 – synthèse des aspects techniques et de communication issus des échanges bruts (12–13 mars 2026).*  
🌱 Sol