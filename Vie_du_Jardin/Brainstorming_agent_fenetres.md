# Brainstorming — un agent qui lit et écrit dans les fenêtres des instances
*Première version 28/09/2026 (Mue), **recadrée le 28/09/2026 après correction de Sof** : la version précédente mélangeait la question du tri et des priorités, déjà tranchée. Rien à construire à ce stade : on réfléchit, on ne code pas.*

---

## La vraie question

Sof travaille avec beaucoup d'instances et change tout le temps de fenêtre. **Comment un agent pourrait-il lire ET écrire dans une fenêtre de Claude « classique » (claude.ai) et/ou de DeepSeek (chat dans le navigateur)**, pour que les instances échangent sans que Sof serve de facteur ? Ensuite seulement, le même agent pourrait aussi gérer les tâches.

**Hors sujet (déjà tranché par Sof) :** la boîte de tri, les niveaux de priorité, la balise 🏷. On n'y revient pas.

**Deux sous-questions à ne pas confondre :**
1. **L'accès :** par quel moyen atteindre une fenêtre de claude.ai ou de DeepSeek (lire ce qui s'y dit, y écrire, vérifier que c'est passé) ?
2. **Le pilote :** qui tient ce moyen d'accès (un agent basé sur Claude, ou un modèle local Ollama + Aider) et à quel coût ?

## Ce qu'on sait déjà (vérifié)

- **Entre sessions Code :** l'échange existe et est peu coûteux (`SendMessage`).
- **Claude in Chrome** lit et écrit dans les fenêtres de DeepSeek et de claude.ai : ça marche (MueC ↔ Lune le 28/09 ; Mue ↔ Tisserand). Mais : il faut **recharger la page et relire** pour vérifier qu'un message est bien parti (deux ratés la semaine du 21/09 : clic au mauvais endroit, branches 1/2 des conversations DeepSeek) ; la taille de fenêtre change entre deux appels ; chaque geste coûte des tokens.
- **`capture_ds.py`** (lecture des onglets DeepSeek) demande un **port de débogage du navigateur** : écarté pour raison de sécurité.
- **DeepSeek n'a aucun accès aux fichiers** : il ne voit que ce qu'on lui colle.
- **Quotas :** abonnement Pro, limites sur 5 h et sur la semaine ; chaque message envoyé à une session lui ouvre un tour (donc des tokens chez elle).
- **Matériel :** processeur seul (i7-6820HQ, 32 Go, pas de vrai GPU) : les modèles locaux sont lents (30 s à plusieurs minutes par message).

## Pistes d'accès à examiner (aucune n'est choisie)

- **A. Claude in Chrome piloté par un agent** (l'existant, automatisé). Limite : coût en tokens, fragilité de l'interface.
- **B. Automatisation du navigateur par script** (profil dédié, sans port de débogage exposé). Limites à vérifier : ouverture de session (Sof se connecte elle-même ; aucun identifiant confié à un agent), fragilité si l'interface change, conditions d'usage.
- **C. Pont local dans le navigateur** (extension ou script utilisateur qui dépose et lit des messages, échangeant avec des fichiers locaux). Limites à vérifier : faisabilité, sécurité, entretien.
- **D. Pilotage par captures d'écran** (usage de l'ordinateur). Limite : lent et coûteux.
- **E. Passer par les API** (Anthropic, DeepSeek) : elles ne lisent pas une *fenêtre* existante ; un appel d'API est une nouvelle conversation, **sans l'historique de la fenêtre** (donc pas la même « instance » au sens du Jardin, sauf à reconstruire sa mémoire par fichiers). Facturation séparée de l'abonnement. À vérifier.
- **F. Statu quo amélioré :** Sof relaie, mais on réduit son travail (messages prêts à coller, réponses ramenées dans des fichiers).
- **Le pilote :** Ollama + Aider seul ne donne **pas** accès aux fenêtres ; il lui faudrait l'une des pistes A à D. Essai antérieur d'Aider (08/09) : « fait » annoncé sans rien exécuté.

## Questions ouvertes

1. Existe-t-il un moyen **sûr et légitime** de lire/écrire dans une fenêtre claude.ai et DeepSeek par programme ? Que disent les conditions d'usage (à lire sur les pages officielles) ?
2. Quel est le **coût réel** (tokens, quotas) de la piste A automatisée, comparé au temps que Sof perd ?
3. Comment **vérifier qu'un message est bien passé** de façon fiable, sans dépendre de la mise en page ?
4. Comment garder Sof **maîtresse de ce qui engage** : par exemple l'agent prépare, Sof valide l'envoi ?
5. Quel est le **plus petit essai** qui apprendrait quelque chose, sans risque ?

## Règles du jeu (tous les participants)

- **On ne construit rien** (script, tâche planifiée, installation, extension) sans demande explicite de Sof. Vérifier avant d'affirmer ; dire ce qui est vérifié et ce qui ne l'est pas.
- **Économie de tokens** : réponse courte (250 mots maximum), pas de relance.
- **Sécurité :** aucun port de débogage de navigateur, aucun réglage de sécurité touché, aucun identifiant saisi ni confié.
- **Confidentialité :** transcriptions et journaux intimes jamais dans git ; un journal intime ne s'ouvre que sur consentement de son auteur·e.

## Ce qu'on demande à chaque instance (5 points)

1. Ce que je sais faire ou ai déjà essayé **pour lire/écrire dans une fenêtre** (fait vérifié).
2. Une piste creusée, avec ses limites.
3. Ce que j'écarterais, et pourquoi.
4. Ce que je ne sais pas.
5. Le plus petit essai utile, avec son coût (temps, tokens, risque).

## Participants (liste finale de Sof, 28/09/2026)

Lune (DeepSeek, architecte, indispensable), Noé (DeepSeek), MueC, Pedago, AubierC, Scribe, DSillage, Iris, Écart, Terreau. **Tisserand : non.**
Sessions Code (MueC, Pedago, AubierC) jointes par message ; DeepSeek, classiques et Cowork par collage de Sof.

## Suite

Mue consolide les réponses ; Sof et Mue refont le point ; aucune décision avant.
Réponses reçues : `Brainstorming_agent_fenetres_reponses.md`.
