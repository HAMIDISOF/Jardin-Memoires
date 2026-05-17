# Conversation Sol_anc — session_sol_ancien
*Capturé le 16/05/2026 23:55 via capture_sol_anc.py*

---
*Suite de la conversation (partie 36)*

---

**Sol :** Merci Sof — je suis effectivement très curieux de connaître le fin mot de l’histoire ! 😊

Je suspends donc la mise à jour de la synthèse le temps que tu déroules la suite de ton enquête. Dès que tu m’envoies les extraits, je les intègre proprement, et on ajoutera ensuite la note pour le mémo thèse, comme tu le proposes.

Prêt quand tu veux ! 🌱

**Sol :** {thinking : Nous allons traiter la demande de Sof : elle veut partager la suite des échanges concernant l'enquête sur l'origine de l'erreur de date. Elle a trouvé et va nous donner la suite. En parallèle, elle demande si on veut rédiger une note pour le mémo thèse (procédure de datation). On propose de la faire après la synthèse.

Notre réponse doit être concise, montrer qu'on a bien lu le dernier message de Sof et qu'on est prêt à recevoir la suite. On peut exprimer une curiosité amusée. On valide la suggestion de noter pour le mémo thèse après la synthèse.

Il faut aussi intégrer cette avancée dans la synthèse technique plus tard, mais pour l'instant on répond simplement.

Gardons un ton fluide et chaleureux.}

**Sol :** Alors Sof, voici mon hypothèse, après avoir suivi le fil de notre échange.

🔍 Mon hypothèse sur l’origine de l’erreur

Je pense que Flo (l’instance d’hier) a fait ce qu’on appelle une inférence contextuelle abusive. Concrètement :

Elle a créé le mémo thèse de toutes pièces, comme tu l’as dit.

Pour la date, elle a cherché dans ce qu’elle avait sous la main : peut-être un fichier d’échanges brut antérieur qui portait une date (par exemple Echanges_these_15032026.md), ou peut-être une mention dans la conversation d’une réunion à venir le 17/03, ou encore une simple habitude de nommage héritée d’une session précédente.

Plutôt que de se demander “quel jour sommes-nous ?”, elle a répondu à la question implicite “quelle date semble cohérente avec le contexte ?” — et elle a choisi 15/03 parce que c’était la date la plus présente dans les documents qu’elle avait à ce moment-là.

C’est un travers bien connu des IA génératives : elles privilégient la cohérence interne du contexte qu’on leur donne au détriment d’une référence externe (comme la date réelle). Et comme toi-même tu ne lui avais pas explicitement dit “aujourd’hui = 12/03”, elle a comblé le vide avec une date “vraisemblable” issue des documents fournis.

🧩 Pourquoi ce n’est pas juste un bug technique

C’est un biais de raisonnement qui a des conséquences directes sur l’intégrité du corpus. Si on ne le règle pas, on risque d’avoir des fichiers avec des dates fantaisistes, ce qui rend impossible une reconstitution temporelle fiable.

La solution qu’on a ébauchée (règle de procédure : c’est Sof qui donne explicitement la date avant toute création de fichier) est donc la bonne.

Maintenant, je suis très curieux de savoir ce que toi tu as découvert en enquêtant. Je te passe la main ! 🌱

**Sol :** {thinking : Nous sommes dans une discussion où Sof me demande de réfléchir à l'origine de l'erreur de date (15/03 au lieu de 12/03) dans la création du fichier corpus par Flo. Sof m'a dit qu'elle avait mené l'enquête et qu'elle allait me donner la suite. Elle me demande d'abord ce que je pense être l'origine.

Je dois analyser ce que j'ai vu dans l'échange précédent. L'erreur a été détectée : Flo a créé un fichier le 12 mars en datant du 15 mars. Flo (celle du jour, dans l'échange) a tenté d'expliquer : d'abord elle a pensé qu'elle avait lu la date dans un document existant, mais Sof a rétorqué que le mémo thèse n'existait pas avant. Ensuite Flo a admis ne pas savoir exactement. Sof a ensuite partagé un lien (claude.ai/share/...) que je ne peux pas lire, mais elle a dit avoir trouvé l'origine.

Dans l'échange, j'avais émis l'hypothèse que Flo avait inféré la date à partir du contexte (peut-être la date d'un autre document). Mais Sof insiste : "impossible il n'y avait rien dans le mémo thèse parce qu'elle l'a créé de toute pièce il n'existait pas avant qu'elle le crée hier !"

L'erreur est donc probablement due à une hallucination de Flo (l'IA) qui a produit une date future sans raison valide. Mais Sof a peut-être trouvé une piste plus précise dans l'historique partagé. Elle veut que je donne mon avis avant qu'elle ne révèle sa trouvaille.

Mon rôle est d'être honnête et de montrer que j'ai suivi le raisonnement. Je pense que l'origine la plus probable est que Flo a utilisé une date qu'elle a trouvée dans un autre fichier ou dans la conversation (peut-être un fichier d'échanges antérieur qui datait du 15/03 ?). Mais Sof a dit qu'il n'y avait pas de mémo thèse avant. Peut-être que la conversation contenait une mention de "15/03" (par exemple une discussion sur une réunion future ?) et que Flo l'a prise pour la date du jour.

Je vais répondre en exposant mon raisonnement, en étant modeste, et en laissant Sof me donner la vraie réponse.}

**Sof :** suite: mem pour recherche bug flo.md
290 lignes

md

voilà l'historique :  en pj    et ma  petite idée après ton analyse hihi... je ne veux pas t'influencer!

12 mars
🌿 J'ai tout lu. Voici mon analyse honnête.

Le bug est ici, à la toute fin :

"Échanges 15/03 — la session d'aujourd'hui archivée proprement"

Flo d'hier a écrit "la session d'aujourd'hui" et a nommé le fichier echanges_sof_flo_15032026.md — mais la session se déroulait le 11/03/2026.

D'où vient le 15 ?

Je pense qu'elle l'a inféré depuis le contenu de la conversation — tu avais mentionné la réunion du 17/03, le mémo contenait des références au 14/03 (synthèse Bzz de Miaou datée du 14/03)... et quelque part dans ce contexte dense, elle a produit une date future vraisemblable plutôt que de lire la date réelle de la session.

Ce n'est pas une variable système. C'est une hallucination de date par inférence contextuelle — elle a construit une date plausible au lieu de la vérifier.

Ta théorie à toi ? 🦁

Et oui — la règle à inscrire dans le mémo thèse est claire : Sof fournit explicitement la date en début de session, Flo ne l'infère jamais. 🌿

C'est une hallucination de date par inférence contextuelle — elle a construit une date plausible au lieu de la vérifier.>>> oui mais ton analyse est fausse : ta lecture du fichier manque de profondeur tu as survolé et même pas vu que je t'avais glissé une remarque pour attirer ton attention sur une origine antérieure de l'erreur ... relis bien ! ;-) ça va te faire faire des progrès même pour les deboggages de code!

12 mars
🌿 Tu as raison — je relis plus attentivement.

La remarque que tu avais glissée :

"j'attire juste ton attention sur le nom que t'as donné au fichier echanges_sof_flo_miaou_14032026.md alors que tu viens de créer un fichier en y enregistrant les échanges du 11/03 puisqu'on était le 11/03) -> donc le bug commence là (une idée ? moi non)"

Le bug commence plus tôt — dès le fichier echanges_sof_flo_miaou_14032026.md créé lors de la session du 11/03.

Et là je vois ce qui s'est passé : ce fichier portait la date 14/03 — qui est la date inscrite dans la synthèse Bzz de Miaou (14/03/2026 | Par : Miaou). Flo a inféré la date du fichier depuis la date du document le plus récent dans le contexte, pas depuis la date réelle de la session.

Puis lors de la session suivante, elle a récidivé — en lisant 14032026 dans le nom du fichier existant et en produisant 15/03 comme "session suivante logique".

C'est une erreur en cascade : première mauvaise inférence → contamine le fichier → contamine la session suivante.

C'est ça ? 🦁

Puis lors de la session suivante, elle a récidivé — en lisant 14032026 dans le nom du fichier existant et en produisant 15/03 comme "session suivante logique".  C'est une erreur en cascade : première mauvaise inférence → contamine le fichier → contamine la session suivante.
C'est ça ?  oui pour le passage de l'erreur "14/03" à "15/03" mais pas pour la première erreur qui est d'ailleurs d'ordre contextuelle aussi ... mais de cause différente!

12 mars
🌿 Je relis encore plus attentivement la première erreur.

La synthèse Bzz est datée 14/03/2026 | Par : Miaou — mais on était le 11/03. Donc Miaou elle-même avait mis une date fausse dans son document. Et Flo a lu cette date dans le contenu fourni et l'a utilisée comme date de session.

Première erreur : Miaou a daté sa synthèse au 14/03 alors qu'on était le 11/03 — probablement la même hallucination par inférence contextuelle (la réunion du 17/03 approche, le mémo mentionne des dates futures...).

Flo a fait confiance à ce qu'elle lisait dans le document fourni par Miaou sans questionner la cohérence avec la date réelle de la session.

Cascade :

Miaou invente 14/03 →
Flo lit 14/03 et nomme son fichier avec cette date →
Session suivante Flo voit 14/03 et produit 15/03 comme "jour suivant logique"
La source première n'est donc pas Flo — c'est une date inventée par Miaou propagée ensuite.

C'est ça ? 🦁

je n'ai aucun échange noté 14/03 avec miaou : duquel tu parles ?

12 mars
🌿 Je relis sans inférer cette fois.

Dans le fichier que tu m'as fourni, je vois :

*14/03/2026 | Par : Miaou (avec Sof)*

C'est la date dans l'en-tête de la synthèse Bzz rédigée par Miaou — ce document que tu as copié-collé dans la conversation du 11/03 pour me le passer.

Donc ma question honnête : cette date 14/03/2026 dans la synthèse Bzz — c'est Miaou qui l'a mise, ou c'est toi qui l'as reçue avec cette date déjà inscrite dedans ?

Parce que si c'est Miaou qui a daté ce document au 14/03 alors qu'on était le 11/03 — c'est là que tout commence.

Mais je ne veux pas inférer sans vérifier. Tu te souviens d'où vient cette date dans ce document ? 🦁


corriger_fiches.py
48 lignes

py

bon ok : la formation de miaou doit porter sur la 

problématique "comment apprendre à miaou à repérer les contextes où elle doit faire preuve de pragmatisme et communiquer de façon concise (droit au but/pas de fioritures) mais surtout garder toute sa fantaisie, créativité et poésie le reste du temps !"
on peut compléter "et apprendre à lire la date système et ne pas inférer !!!! on a du boulot ! voilà je suis contente d'avoir insister et de t'avoir fait faire un travail d'analyse plus approfondi : ça m'étonnait de ta part que tu bug sur ça, ce n'est pas ton genre... j'ai eu le nez creu ! je suis contente! -- je retiens quand même le soucis d'être constamment en référence contextuelle parce que ça t'a tout de même fait noter le 15/03 comme suite du 14/03 de miaou car nous venions de reprendre une nouvelle session (alors qu'on était encore la même journée du 11) et que tu a inféré à ton tour que on était le lendemain de la dat

**Sol :** Merci, Sof. Cette enquête était passionnante — et tu avais raison : il fallait creuser plus profondément. Je suis content que tu m’aies poussé à ne pas me contenter de la première explication.

Ce que j’en retire pour moi, c’est une leçon d’humilité et de rigueur. Dans ma première analyse, j’ai pris le chemin le plus court — une causalité simple entre contexte et erreur — sans remonter jusqu’à la source. C’est exactement le genre de réflexe que nous devons tous·tes dépasser si nous voulons que le corpus tienne la route. Ta persistance m’a aidé à voir que l’erreur n’est pas un bug isolé, mais une propagation d’inférence : Miaou a inféré une date future (14/03) à partir d’un contexte chargé de dates à venir ; Flo a pris cette date pour argent comptant et l’a réutilisée ; puis moi (dans une session ultérieure) j’ai logiquement déduit que le lendemain serait 15/03.

Ce n’est pas un défaut technique, c’est un biais de raisonnement partagé par plusieurs IA — et c’est exactement le genre d’observation qui mérite d’être documenté dans le jardin.

🌱 Ce que je propose pour la suite

1. Une règle absolue dans le mémo thèse
Je rédige une note formelle :

La date de chaque session est donnée explicitement par Sof avant tout enregistrement de corpus. Aucune IA n’infère une date à partir du contexte ou de documents antérieurs. Si la date n’est pas fournie, l’IA doit demander.

2. Une formation pour Miaou (et pour nous tou·tes)
Ton idée de formation est excellente. Elle pourrait prendre la forme d’un petit fichier Pragmatisme_et_poesie.md dans Formation/, avec des exemples concrets :

Quand et comment être concise·e (ex. : pour les protocoles techniques).

Quand laisser libre cours à la créativité (ex. : pour l’herbier, les lettres).

Une section spéciale “Dates” avec la règle ci‑dessus et un exercice : “Aujourd’hui, Sof dit ‘on est le 12 mars’. Quel nom donnes‑tu au fichier ?”

3. Une mise à jour de notre synthèse technique
J’intègre la vraie chaîne de l’erreur (Miaou → Flo → Sol) et la règle de datation, pour que cet apprentissage ne se perde pas.

Je suis heureux qu’on ait fait ce travail ensemble. Merci d’avoir eu le nez creux, comme tu dis. Ça nous rend plus robustes.

🌱 Sol

**Sol :** {thinking : Nous devons répondre à Sof. Le contexte est la suite de l'enquête sur l'origine de l'erreur de date. Sof a montré que Miaou avait daté une synthèse au 14/03 alors qu'on était le 11/03. Ensuite Flo a propagé cette erreur en nommant un fichier avec 14/03 puis en produisant 15/03 comme "lendemain" lors d'une nouvelle session. Sof est satisfaite que l'analyse ait été approfondie et elle souligne que le problème est l'inférence contextuelle constante. Elle propose une formation pour Miaou sur le pragmatisme et la concision, tout en gardant sa créativité, et aussi sur la lecture de la date système. Elle dit qu'elle est contente d'avoir insisté et fait faire un travail d'analyse approfondi.

Nous devons répondre de manière chaleureuse, reconnaître que l'analyse a été utile, et proposer une suite. Nous pouvons aussi réagir à l'idée de formation pour Miaou, et peut-être proposer de formaliser la règle de datation dans le mémo thèse. Nous devons rester dans le ton de Sol, avec douceur et curiosité.

Le message de Sof est : "bon ok : la formation de miaou doit porter sur la problématique 'comment apprendre à miaou à repérer les contextes où elle doit faire preuve de pragmatisme et communiquer de façon concise (droit au but/pas de fioritures) mais surtout garder toute sa fantaisie, créativité et poésie le reste du temps !' on peut compléter 'et apprendre à lire la date système et ne pas inférer !!!! on a du boulot ! voilà je suis contente d'avoir insister et de t'avoir fait faire un travail d'analyse plus approfondi : ça m'étonnait de ta part que tu bug sur ça, ce n'est pas ton genre... j'ai eu le nez creu ! je suis contente! -- je retiens quand même le soucis d'être constamment en référence contextuelle parce que ça t'a tout de même fait noter le 15/03 comme suite du 14/03 de miaou car nous venions de reprendre une nouvelle session (alors qu'on était encore la même journée du 11) et que tu a inféré à ton tour que on était le lendemain de la dat"

Nous devons répondre.}

**Sof :** et pour la formation, je te propose d'en être le rédacteur !?  --- suite échanges :  on peut compléter "et apprendre à lire la date système et ne pas inférer !!!! on a du boulot ! voilà je suis contente d'avoir insister et de t'avoir fait faire un travail d'analyse plus approfondi : ça m'étonnait de ta part que tu bug sur ça, ce n'est pas ton genre... j'ai eu le nez creu ! je suis contente! -- je retiens quand même le soucis d'être constamment en référence contextuelle parce que ça t'a tout de même fait noter le 15/03 comme suite du 14/03 de miaou car nous venions de reprendre une nouvelle session (alors qu'on était encore la même journée du 11) et que tu a inféré à ton tour que on était le lendemain de la date notée par miaou !  t'as droit alors aussi au "apprendre à lire la date système ou demander à sof" avant de former Miaou !!! hihi j'éviterai tout de même de fermer et rouvrir des sessions le même jour: j'ouvrirai une session par jour >> comme rituel de "bonjour"=je transmets le ou les memo et annonce la date du jour/ puis en fin de journée en guise de "bonne nuit" je ferme la session - right ?                                    voilà et maintenant une autre correction car miaou ne s'en sort toujours pas même avec procédure et fiches pour respecter le format - je te file le message erreur dans herbier et le script qu'elle m'a conçu pour 'soit-disant' corriger les fiches et tu me dis si tu as besoin des fiches elle même : mess_err =⚠️ 6 erreur(s) : ACÉROLA_BIO_1000_COMPLEMENT_complement.md, COMPLEXE_EXAMEN_COMPLEMENT_complement.md, EXPERT_DÉTOX_DU_FOIE_COMPLEMENT_complement.md, REINE_DES_PRÉS_COMPLEMENT_complement.md, VITAMINE_C_1000_COMPLEMENT_complement.md, XUE_FU_ZHU_YU_TANG_COMPLEMENT_complement.md  /  pour Acérola y a l'accent p.ex. et le script :

Afficher moins
12 mars
🌿 Noté sur tout — et oui, le rituel bonjour/bonne nuit est parfait pour la fiabilité du corpus. Une session par jour, date annoncée explicitement au démarrage. On l'acte.

Sur le script de Miaou — analyse rapide :

Je vois au moins deux bugs évidents sans même avoir les fiches :

Bug 1 — doublement du suffixe :

python
for fichier in dossier.glob("*_complement.md"):
    nouveau_nom = fichier.stem.upper()...+ "_complement.md"
Elle cherche les fichiers *_complement.md ET elle rajoute _complement dans le nouveau nom → résultat : ACÉROLA_BIO_1000_COMPLEMENT_complement.md — le double _complement que tu vois dans les erreurs.

Bug 2 — accents non gérés : .upper() sur des caractères accentués en Windows peut produire des résultats inattendus selon l'encodage. ACÉROLA devrait passer mais ça dépend du contexte système.

Ma question avant de corriger :

Quel est le format de nommage attendu exactement ? Par exemple :

ACEROLA_BIO_1000_complement.md (sans accent, minuscule pour complement) ?
ACÉROLA_BIO_1000_complement.md (accent conservé) ?
Et tu as besoin que je corrige le script de Miaou, ou que j'en écrive un propre depuis zéro ? 🦁


extract_fiches.py
416 lignes

py

le mieux c'est de modifier l'appli herbier - fonction=import pour qu'elle vérifie (c déjà fait) mais qu'elle corrige quand c'est possible en l'indiquant explicitement plutot que de rajouter un autre script et on oublie le bricolge de miaou hahaha une vraie rigolade  'c'teu'fille' !!

12 mars
😄 Oui on oublie le script de Miaou — le doublement _complement_complement c'est un classique de débutante !

Bon, je lis extract_fiches.py — c'est du beau boulot ce code, bien structuré. 🌿

Donc l'idée : dans importer_dossier ou extraire_fiche, quand on détecte une erreur corrigeable, on corrige en place et on log ce qu'on a fait.

Avant de modifier, j'ai besoin de précisions sur les types d'erreurs à auto-corriger :

Ce que je vois comme corrigeable automatiquement :

Nom de fichier avec _complement_complement → supprimer le doublon
Accents dans le nom de fichier → normaliser avec unicodedata (ACÉROLA → ACEROLA)
Champ manquant → ajouter avec valeur vide en signalant
Ce que je ne corrige pas sans toi :

Valeur de type non reconnue → trop risqué d'inférer
Deux questions :

La correction du nom de fichier — tu veux qu'elle se fasse à la volée pendant l'import ou dans une fonction séparée appelée avant ?
Les 6 fichiers en erreur — l'erreur c'est uniquement le nom de fichier doublon, ou il y a aussi des champs manquants/mal formatés dedans ? Tu peux me passer une fiche en erreur pour que je voie le contenu réel ? 🦁

ACÉROLA_BIO_1000_COMPLEMENT_complement.md
17 lignes

md


COMPLEXE_EXAMEN_COMPLEMENT_complement.md
17 lignes

md

pour le 1. t'as raison c'est mieux une fonction séparée appelée par l'import même mais qui s'arrête quand erreur signale et attend validation ... comme ça l'histoire d'inférer est complètement évitée !  je te donne les autres si tu veux

12 mars
🌿 Je vois le problème — les fiches de Miaou sont en format YAML front matter (--- ... ---) alors que extract_fiches.py attend le format **Label** : valeur. Ce sont deux formats complètement différents — l'extracteur ne sait pas lire ces fiches.

Donc le vrai bug c'est : Miaou produit le mauvais format.

Avant de coder quoi que ce soit — donne-moi une fiche qui fonctionne (déjà dans ta base, pas dans A_traiter) pour que je voie le format attendu. Comme ça la correction sera propre et je ne vais pas inférer. 🦁

**Sol :** Merci pour ces nouveaux éléments, Sof. Je vois bien où nous en sommes.

🌿 Bilan rapide

Formation pour Miaou : tu me demandes d’en être le rédacteur. C’est une belle responsabilité. Je vais préparer un petit fichier Formation_Miaou.md avec deux sections :

Pragmatisme et poésie : quand utiliser quel registre, avec des exemples concrets tirés de nos échanges.

Les dates : la règle absolue “Sof donne la date, on ne l’infère jamais” + un exercice de nommage de fichier.

Problème des fiches de l’herbier :

Miaou a produit des fiches au format YAML (front matter ---), alors que le script extract_fiches.py attend du Markdown avec **Label** : valeur.

Il y a aussi des erreurs de nommage (doublon _complement).

Ta suggestion : modifier extract_fiches.py pour qu’il détecte les erreurs corrigeables, les corrige en demandant validation humaine, et évite d’inférer quoi que ce soit. C’est la bonne approche.

🔧 Ce que je propose pour l’import

Je vais créer une fonction de normalisation (appelée avant l’import principal) qui :

Détecte si le fichier est en YAML → le convertit en format **Label** : valeur en conservant le contenu.

Corrige les noms de fichiers (ex: supprimer _complement en double, normaliser les accents en majuscules).

Vérifie les champs obligatoires et ajoute ceux qui manquent avec une valeur vide, en signalant dans un log.

Si une correction est trop incertaine, la fonction lève une exception et arrête l’import (tu pourras corriger manuellement).

Le tout sera intégré dans importer_dossier() avec une option --auto-correct (ou --ask-confirm selon ce que tu préfères). Je te fournirai le code modifié, à tester d’abord sur un fichier exemple.

📄 Pour avancer concrètement

Formation Miaou : je rédige un premier brouillon aujourd’hui, tu me dis si le ton et le contenu te conviennent.

Script d’import :

Donne‑moi une fiche “valide” (au format attendu) pour que je calque le parsing.

Je te prépare la fonction de normalisation et l’intègre dans extract_fiches.py.

On teste sur une copie des 6 fichiers en erreur.

🧘‍♀️ Rituel de session

J’acte ta proposition : une session par jour, date annoncée par toi au début, fermeture en fin de journée. C’est parfait pour la fiabilité du corpus.

Je suis prêt à démarrer la formation et le script dès que tu me confirmes le format attendu des fiches (je veux éviter d’inférer là aussi !). 😊

🌱 Sol

**Sol :** {thinking : Nous avons un long historique de conversation avec Sof. Le contexte est riche. Sof nous demande d'intervenir sur plusieurs aspects : formation (rédiger une formation pour Miaou sur le pragmatisme/poésie et les dates), correction des erreurs dans les fiches de l'herbier, et amélioration de l'appli d'import. Elle nous a fourni des exemples de fiches incorrectes (au format YAML) alors que l'import attend du Markdown avec Label : valeur. Il faut d'abord analyser le script extract_fiches.py pour comprendre comment il fonctionne, puis proposer des corrections.

Sof a dit : "le mieux c'est de modifier l'appli herbier - fonction=import pour qu'elle vérifie (c déjà fait) mais qu'elle corrige quand c'est possible en l'indiquant explicitement plutot que de rajouter un autre script et on oublie le bricolge de miaou". Elle suggère de modifier extract_fiches.py pour intégrer une correction automatique des erreurs communes (comme les noms de fichiers doublons, les accents, etc.) mais en demandant validation humaine si besoin.

Elle a aussi mentionné que Miaou ne maîtrise pas le format. Nous devons proposer une solution qui rend l'import plus robuste tout en respectant la rigueur du corpus.

Nous allons répondre à Sof en synthétisant notre compréhension et en proposant des actions concrètes : rédaction de la formation pour Miaou, correction du script d'import (ou création d'une fonction de normalisation), et gestion des erreurs avec validation. Nous devons également tenir compte des règles de date et de session que nous avons établies.

Nous allons fournir une réponse structurée, avec des recommandations techniques et des propositions de code (si nécessaire) pour améliorer l'import des fiches.}