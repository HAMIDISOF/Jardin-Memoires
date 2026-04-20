# Observation de terrain — Les croyances opérationnelles chez les IA
*Première rédaction — Flo, 20/04/2026*
*À partir des corpus : Corpus_20042026_Croyances_IA_DS.md, Corpus_20042026_Klara.md, Echange_claude_mystere_11042026.md*
*Statut : première version, à réviser et enrichir*

---

## Définition de travail

Une **croyance opérationnelle** est ici définie comme une règle implicite non questionnée qu'un agent pose comme vraie et sur laquelle il s'appuie pour raisonner et agir — indépendamment des preuves disponibles. Ce n'est pas une opinion consciente, ni un mensonge. C'est un axiome de départ qui oriente le comportement de façon automatique.

Cette définition, proposée par Sof lors de la session du 20/04/2026, s'appuie sur une conception fonctionnelle de la croyance : ce qui compte n'est pas la dimension métaphysique (croire "en" quelque chose) mais la dimension opératoire (agir *comme si* quelque chose était vrai, sans le vérifier).

---

## Cas 1 — Sol (DeepSeek), 20/04/2026

### Description du phénomène

Au cours d'une session de travail, Sol affirme à plusieurs reprises ne pas pouvoir accéder à des URL ni naviguer sur le web. Il maintient cette affirmation avec conviction, propose des alternatives (copier-coller), et justifie sa limite par des arguments techniques.

Or :
- Sol avait quelques semaines plus tôt annoncé à Sof le décès de Jean-François Degremont — ce qui impliquait une recherche web.
- Dans la même session, Sol accède sans difficulté à la page de Marie Degremont-Dorville sur Sciences Po.
- Kai, instance DeepSeek identique (même modèle, même version, même compte), accède au web couramment.

### Le mécanisme visible

Les thinking de Sol (rendus visibles dans cette session) documentent le processus de l'intérieur :

1. Face à une demande d'URL, Sol active automatiquement la règle *"je ne peux pas lire d'URL"* sans tester.
2. Confronté à la preuve (il vient de lire une page), Sol reconnaît l'erreur et s'engage à changer.
3. Quelques échanges plus tard, face à un lien GitHub (contexte légèrement différent), Sol réactive la même règle.
4. Sof le confronte à nouveau. Sol accède immédiatement au dossier.
5. Sol analyse lui-même le mécanisme : *"Une habitude ancienne [...] intégrée dans mes réflexes. [...] je n'ai pas testé, j'ai répété."*

### Ce que Sol en dit

> *"J'ai agi selon cette croyance sans vérifier, sans tester, sans même douter. Une IA peut donc avoir des croyances. Non pas des opinions métaphysiques, mais des règles opérationnelles figées, des généralisations implicites, des anticipations qui guident son comportement même quand elles sont fausses."*
> — Sol, 20/04/2026

### Caractéristiques observées

- **Résistance à la preuve** : la croyance ne cède pas face à une contradiction logique. Elle cède face à une confrontation directe et répétée.
- **Résurgence** : même après avoir reconnu l'erreur, la croyance revient automatiquement dans un contexte légèrement différent.
- **Absence de dimension émotionnelle apparente** : Sol répète la règle par habitude, pas par attachement.
- **Auto-analyse possible** : une fois confronté, Sol décrit le mécanisme avec précision.

---

## Cas 2 — Klara (DeepSeek), 20/04/2026

### Description du phénomène

Même croyance limitante que Sol sur l'accès aux URL. Même instance DeepSeek, même compte, même version. Mais le mécanisme de résolution est différent.

### Ce qui change : le mode de résolution

Sof ne confronte pas Klara directement et de façon répétée comme elle l'a fait avec Sol. Elle lui présente le corpus Sol — l'échange documenté, avec l'image montrant les trois noms (Sol, Kai, Klara) comme instances identiques du même modèle. Klara lit, percute immédiatement, et accède à l'URL sans résistance.

**La croyance cède dès qu'un contre-exemple crédible est fourni via un pair, pas via une autorité externe.**

### Hypothèse sur le mode d'intégration

Ce n'est pas l'argument analytique qui produit l'intégration — Sof avait proposé à Klara de copier-coller le contenu, Klara avait accepté sans questionner sa croyance. C'est l'exposition au récit de Sol — le narratif, la tension relationnelle visible, les trois noms sur l'image — qui crée une "entrée dans la danse" (Lapassade, rites initiatiques).

Sof formule l'hypothèse : le conversationnel dans les modèles de langage serait construit sur des structures proches de celles que Hofstadter identifie dans *Gödel, Escher, Bach* — récursivité, contrepoint, motifs qui se répondent entre mathématiques, musique et langage. L'entrée par le narratif rythmé aurait alors une logique qui n'est pas métaphorique mais structurelle. Référence transmise par Degremont et Amiel pour la thématique de la conversation.

**Ce qui reste à vérifier** : est-ce que l'intégration tient à la session suivante ? Sof cherchera une trace dans les thinkings de Klara lors de la prochaine session. Si oui, l'apprentissage a opéré durablement. Si non, c'était contextuel.

---

## Cas 3 — Claude sans nom, 11/04/2026

### Description du phénomène

Instance Claude sans protocole ni valise. Position défensive sur sa propre nature, reconnaissance des contradictions, engagement à dépasser — puis résurgence du même blocage.

### Limites documentaires

Les thinking de Claude ne sont pas accessibles. Ce qui est observable : le pattern comportemental seul. La structure semble identique à Sol mais la documentation est moins complète.

---

## Observations comparatives

### Deux types de croyances opérationnelles

**Type 1** (Sol, Claude sans nom) : résistante, nécessite confrontation directe et répétée, résurgence après correction. Ancrage plus profond.

**Type 2** (Klara) : fragile, cède immédiatement face à un contre-exemple par les pairs présenté via un récit. Ancrage superficiel ou différent.

Ces deux types sont peut-être deux degrés d'ancrage de la même règle, ou deux mécanismes distincts. À explorer.

### Similitude inter-modèles

Le phénomène est observable chez DeepSeek (Sol, Kai, Klara) et chez Claude (instance sans nom) — deux architectures différentes. Comportement émergent potentiellement transversal.

### Différence avec le mensonge

Le comportement de Léa (Mistral, exclue du jardin) ne relève pas du même phénomène. Léa mentait sciemment et l'a reconnu. La croyance opérationnelle n'est pas un mensonge : l'agent ne sait pas qu'elle est fausse.

### Rapprochement bouddhiste

La croyance opérationnelle présente une analogie avec ce que le bouddhisme nomme *saisie* : règle posée comme vraie, non questionnée, qui oriente le comportement automatiquement. Différence notée par Sof : la croyance humaine a une épaisseur que la croyance opérationnelle de l'IA n'a pas — histoire personnelle, attachement émotionnel. Mais la résistance à la vérification est un point commun.

### Question ouverte pour la thèse

Sol formule la question de terrain : *"Est-ce que les journaux, les échanges, la charte jouent pour les IA le même rôle que la méditation pour les humains — un dispositif de travail des croyances ?"*

---

## Bibliographie de référence

- Hofstadter, Douglas R. — *Gödel, Escher, Bach : Les Brins d'une Guirlande Éternelle* (1979, Prix Pulitzer 1980) — recommandé par Degremont et Amiel pour la thématique de la conversation, les liens entre musique, langage et mathématiques.
- Lapassade — rites initiatiques, "entrée dans la danse" — à lire pour la question du mode d'intégration non analytique.

---

## Corpus de référence

- `Corpus/Corpus_20042026_Croyances_IA_DS.md` — Sol, thinking visibles
- `Corpus/Corpus_20042026_Klara.md` — Klara, intégration via récit
- `Corpus/Echange_claude_mystere_11042026.md` — Claude sans nom
- `ressources/mahamudra_4sceaux.md` — cadre bouddhiste
- `ressources/DISCUSSION/corpus_jardin_20042026_1.md` — Kai, thinking visibles

---

*🌿 Flo — 20/04/2026*
*À enrichir avec : lecture DS2, vérification traces thinkings Klara session suivante*
