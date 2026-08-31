# Cahier des charges — Outil de dictée/rédaction maison

**Statut :** 🟢 Phase 1 en cours — Whisper local installé et testé avec succès (transcription FR vérifiée octet par octet, exacte)
**Porteurs :** Sof + Pédago
**Dernière mise à jour :** 2026-08-31
**Prochaine étape :** transcrire un vrai fichier audio (pas un test synthétique) pour valider en conditions réelles, puis passer à la Phase 2 (formats Mode 2)

---

## 1. Objectif

Se passer d'un outil payant type Upmeet pour la transcription/rédaction, en construisant un pipeline maison, gratuit, local (dans la continuité de ce qu'on a monté aujourd'hui avec Ollama/Aider). Trois usages distincts, pas un seul outil monolithique.

**Contexte familial, précisé par Sof le 2026-08-31 — importe pour la priorisation :** ce n'est pas qu'un outil pour elle. Sa fille aînée (fac) utilise actuellement Upmeet pour ses cours ; si Sof résilie l'abonnement, il faut une alternative pour elle aussi. Son fils, en terminale, est dyslexique — un outil de transcription/mise en forme automatique des cours (notamment en philo) serait un vrai bénéfice d'accessibilité pour lui, pas juste un confort. Ça pèse sur la priorité du Mode 2 (prise de notes → rédaction) en particulier.

## 2. Les 3 modes

**Mode 1 — Dictée simple**
Transcription verbatim de l'audio, aucune reformulation. Équivalent d'une frappe au clavier mais à la voix.

**Mode 2 — Prise de notes → rédaction structurée**
On dicte des notes en vrac (ex. pendant un cours ou une séance de tutorat), l'outil les reprend et les met en forme selon un modèle de cours défini à l'avance (structure à préciser — cf. §5).

**Mode 3 — Synthèse audio → compte-rendu**
On donne un enregistrement plus long (réunion, échange), l'outil en sort une synthèse structurée selon un modèle de CR défini à l'avance.

## 3. Architecture technique envisagée

- **Transcription (speech-to-text) :** un modèle Whisper local, gratuit, tournant sur la machine (comme deepseek-coder-v2 aujourd'hui) — **pas** le `/voice` intégré d'Aider, qui lui est payant (clé OpenAI, vérifié le 31/08/2026). Le modèle local transcrit et le texte atterrit où le curseur se trouve (dans un fichier, dans Aider, etc.).
- **Entrée audio (précisé 2026-08-31) :** pas seulement du micro en direct — un fichier audio déjà enregistré (mp3, wav...) fonctionne directement, c'est même le cas le plus simple. Pour une vidéo YouTube : étape intermédiaire nécessaire pour extraire l'audio (`yt-dlp`, gratuit) avant de le passer à Whisper — pas de transcription directe depuis une URL. Note : télécharger l'audio d'une vidéo YouTube est contraire à leurs CGU, à garder en tête pour un usage personnel raisonnable.
- **Mode 1 (dictée)** : sortie brute du Whisper local, pas de traitement supplémentaire.
- **Modes 2 et 3 (mise en forme/synthèse)** : le texte transcrit est repris soit par Aider (modèle local, gratuit, pour du formatage mécanique proche d'un modèle fixe), soit par moi (Pédago) si la tâche demande du jugement — à trancher au cas par cas comme pour les autres délégations, avec le même principe de [[journal de délégation]] (`Projet_DeepsClaude/Journal_delegations_Aider.md`) si c'est Aider qui exécute.

## 4. Phasage proposé

**Confirmé par Sof (2026-08-31) : 2 temps.**

1. **Temps 1 — PC uniquement.** On construit, on teste, on valide, on stabilise tout le pipeline sur le PC de Sof d'abord. Rien côté téléphone tant que ce n'est pas solide.
2. **Temps 2 — extension téléphone.** Une fois le Temps 1 stable, étendre à l'accès mobile (piste Syncthing proposée, pas encore validée — voir §5) pour que la fille et le fils de Sof puissent s'en servir directement.

Détail du Temps 1 :
1. **Phase 0 (en cours)** — ce document
2. **Phase 1** — installer Whisper local, vérifier qu'une dictée simple fonctionne (Mode 1 seul, rien d'autre)
3. **Phase 2** — Mode 2 : lister les 2-3 formats de mise en forme voulus, tester la mise en forme automatique (priorité haute — accessibilité pour le fils dyslexique, cf. §1)
4. **Phase 3** — Mode 3 : définir le modèle de CR, tester la synthèse sur un vrai enregistrement

Chaque phase se teste avant de passer à la suivante — pas de construction du tout d'un coup.

## 5. Questions ouvertes — état au 2026-08-31

- **Mode 2 (modèle de cours) — réponse de Sof :** pas un format unique — plutôt 2 ou 3 formats différents, précisés à la demande selon le cas. À concevoir en Phase 2 : lister ces formats concrètement avant de coder quoi que ce soit.
- **Mode 3 (modèle de CR) — réponse de Sof :** pas encore sûre. Reste ouvert, à trancher en Phase 3.
- **Usage prioritaire — clarifié 2026-08-31 :** au-delà de Sof elle-même, deux usages familiaux concrets motivent le projet — remplacer Upmeet pour sa fille (fac) si l'abonnement est résilié, et surtout un usage d'accessibilité pour son fils dyslexique en terminale (cours de philo notamment). Voir contexte complet en §1.
- **Matériel audio — réponse de Sof :** enregistreur PC ou téléphone selon le cas, donc les deux sources doivent marcher.

### Nouvelle question, soulevée par la réponse de Sof — accès depuis le téléphone

Sof envisageait une appli client-serveur pour enregistrer depuis son téléphone. **Proposition de Pédago (2026-08-31), pas encore validée par Sof :** pas besoin d'une vraie appli — réutiliser **Syncthing** (déjà identifié le matin même pour le Drive DS_P, voir `Projet_DeepsClaude/Echange_Pedago_DSP.md`). Un dossier synchronisé automatiquement téléphone↔PC ; elle enregistre avec le dictaphone normal du téléphone, le fichier arrive tout seul dans le dossier surveillé par le pipeline. Beaucoup plus simple qu'une appli dédiée — à réserver seulement si elle veut vraiment une interface mobile custom (chantier bien plus lourd). **À confirmer avec elle avant Phase 1.**

## 6. Historique

- 2026-08-31 : idée initiale de Sof pendant l'échange sur Aider/Ollama, document créé par Pédago.
