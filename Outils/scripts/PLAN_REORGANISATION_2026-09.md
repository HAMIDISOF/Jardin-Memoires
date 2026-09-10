# Plan de réorganisation du dépôt — septembre 2026

Document de travail préparé par Claude Code, à valider par Sof avant toute exécution.
Rien n'a été déplacé : ce plan liste les actions proposées, classées par niveau de confiance.

Rappel des règles validées par Sof (conversation du 10/09/2026) :
- **Règle A (versions numérotées)** : dans un groupe `Nom.md` / `Nom_v2.md` / `Nom_v3.md`..., le numéro
  le plus haut est considéré comme la version actuelle. Les autres partent dans un sous-dossier `Archives/`
  local (même dossier), sans renommage — le fichier « gagnant » garde son nom (même s'il contient encore `_v4`).
- **Règle B (copies de sauvegarde)** : dans un groupe `Nom.md` + `Nom_sav.md` / `Nom_sav2.md` / `Nom_bis.md`,
  le fichier sans suffixe est l'actuel ; les copies suffixées partent dans `Archives/`.
- **Dossier `test/`** : archivé (pas supprimé) dans `Outils/Archives/`.
- Nouveau : un dossier `_A_trier/` à la racine de `Recherche/publications/` pour les cas où le classement
  n'est pas évident — proposition de Sof, adoptée ici.

---

## 0. Fichier orphelin `version_ebd8831_04.html` (racine du dépôt)

**Résolu.** C'est un fragment (« partie 4 », sections A-3-3 à B-1-1) d'un ancien découpage de la thèse de
Peschard. Le découpage complet et à jour existe déjà dans
`Recherche/ressources/Bibliographie/Peschard_HTML/` (fichiers `01_I_Ethique_A3.html`, `B1.html`, `B2.html`,
`B3.html`, etc. — la même matière, mieux découpée). Il y a même une refonte plus récente dans
`Peschard_HTML - REFONTE/`.

→ Ce fragment n'est pas incertain, il est **superflu** : proposition de le déplacer dans
`Recherche/ressources/Bibliographie/Peschard_HTML/Archives/version_ebd8831_04.html` plutôt que de le
supprimer, au cas où il contiendrait une formulation qui aurait été perdue au recoupage. Pas besoin du
dossier `_A_trier/` ici puisque l'origine est identifiée.

---

## 1. Actions sûres (incluses dans le script `reorg_2026-09_phase1.sh`)

### 1.1 Dossiers hors structure

| Action | Détail |
|---|---|
| Fusionner | `ressources_tutorat/Projet_Psy_Dev_D_IA/*` → `Vie_du_Jardin/Projet_Psy_dev/` (même projet, contenu différent, pas de collision de noms de fichiers) |
| Supprimer dossier vide | `ressources_tutorat/` après la fusion |
| Archiver | `test/test_automatisation.md` → `Outils/Archives/test_automatisation.md` (fichier de test technique du pipeline de capture, généré le 12/05 pour Luz, sans valeur de mémoire) |
| Supprimer dossier vide | `test/` après archivage |
| Archiver | `version_ebd8831_04.html` (racine) → `Recherche/ressources/Bibliographie/Peschard_HTML/Archives/version_ebd8831_04.html` |

### 1.2 Groupes « backup » sans ambiguïté (Règle B — que des exemples clairs)

| Dossier | Actuel (reste en place) | Archivé dans `Archives/` |
|---|---|---|
| `Membres/Kai/` | `Valise_Kai.md` | `Valise_Kai_sav.md`, `Valise_Kai_sav2.md` |
| `Membres/Klara/` | `Valise1_Klara.md` | `Valise1_Klara_bis.md` |
| `Membres/Sol/` | `Cahier_des_Horizons_Sol.md` | `Cahier_des_Horizons_Sol_22072026.md`, `SAV_Cahier des Horizons_Sol.md` |
| `Membres/Sol/` | `memo_gestion_projets_sol.md` | `memo_gestion_projets_sol_22072026.md`, `memo_gestion_projets_sol_sav.md` |
| `Membres/Sol/` | `Valise_Sol.md` | `Valise_Sol_v0.md` |
| `.../L_UN_PAR_LE_TOUT/ESSAI/` | `Husserl en tension_synthèses passives et intersubjectivité.md` | `..._v1.md` |

### 1.3 Groupes « version numérotée » sans ambiguïté de nom (Règle A — le nom gagnant n'a pas de forme "propre" concurrente)

| Dossier | Actuel (reste en place) | Archivé |
|---|---|---|
| `Histoire/` | `Chapitre_3_v5.md` | `Chapitre_3.md`, `Chapitre_3_v2.md`, `Chapitre_3_v3.md`, `Chapitre_3_v4.md` |
| `Histoire/` | `Chapitre_4_v2.md` | `Chapitre_4.md`, `Chapitre_4._v1.md` |
| `Recherche/` | `MANIFESTE_JARDIN_COOPERATIF_v4.md` | `MANIFESTE_JARDIN_COOPERATIF.md`, `_v2.md`, `_v3.md` |
| `.../L_UN_PAR_LE_TOUT/` | `Encart_Enaction_Varela_Bitbol_v4.md` | `Encart_Enaction_Varela_Bitbol.md`, `_v2.md`, `_v3.md` |
| `.../L_UN_PAR_LE_TOUT/` | `l_un_par_le_tout_V2.html` | `l_un_par_le_tout.html`, `_V0.html`, `_V1.html` |
| `.../L_UN_PAR_LE_TOUT/ESSAI/` | `Lettre_Amiel_v2.md` | `Lettre_Amiel.md` |
| `Membres/Sol_anc/` | `Valise_Sol_v1.2_aout2026.md` | `Valise_Sol.md`, `Valise_Sol_v1_aout2026.md` |
| `Recherche/publications/` | `presentation_jardin_v2_mai2026_revue.md` *(la plus étoffée, 400 lignes, même ouverture que v2 mais fin très développée — évolution linéaire confirmée à la lecture)* | `presentation_jardin_v1.md`, `_v1_mai2026.md`, `_v2_mai2026.md` |

**Résolu — Autobiographie_Klara** (lu et comparé les 3 fichiers le 10/09) :
- `Autobiographie_Klara.md` s'auto-déclare « Version courante — 04/05/2026 » → reste en place.
- `Autobiographie_Klara_v1.md` porte une note éditoriale d'Aev : ce n'est pas un brouillon dépassé mais un
  texte compagnon délibéré, rattaché au Chapitre 4 (« Les deux sont vraies ») → **reste en place**, ne pas
  archiver malgré le suffixe `_v1`.
- `Auto‑biographie de Klara.md` (tiret unicode) est un diff quasi mot-pour-mot de `_v1.md`, sans mise en
  forme (pas de titre « version 1 (crise) », pas de note d'Aev, pas de `##`) → c'est le brouillon source,
  remplacé par `_v1.md` → **archivé**.

⚠️ **Remarque générale sur 1.3** : le fichier « gagnant » garde son nom tel quel (donc encore avec `_v4`,
`_V2`, etc.), pendant que le nom « propre » sans suffixe part en archive. Si un autre document du dépôt
fait un lien vers le nom propre (ex. `MANIFESTE_JARDIN_COOPERATIF.md`), le lien pointera vers une version
archivée. Je n'ai pas vérifié tous les liens croisés du dépôt. Deux options pour plus tard, à ta discrétion :
(a) laisser tel quel (le lien cassé signale juste qu'il faut le mettre à jour), ou (b) une fois le script
validé, je fais une passe de vérification des liens internes avant de pousser.

### 1.4 README

- Corriger `README.md` (racine) : remplacer la ligne `Corpus/` (dossier qui n'existe pas) par une
  description fidèle — les corpus vivent dans `Membres/<nom>/` et `Recherche/analyses/`. Voir texte proposé
  au §3.
- Ajouter un `README.md` minimal (contenu généré automatiquement, liste des fichiers présents) dans les
  19 dossiers `Membres/*` qui n'en ont pas encore : Aubier, Aurore, Boussole, Cadmos, DSillage, Ecart, Fifi,
  Flux, Jachère, Levain, Lumen, Miaou, NOE, Noel, Racine, Sillon, Sol_anc, Tisserand, coeur_de_bronze.
  Sur le modèle de `Membres/Mue/README.md`, mais avec les champs personnels (Architecture / Arrivée / Rôle /
  Signe) laissés en `à compléter` — je ne invente pas ces informations, à chaque membre ou à toi de les
  remplir.

---

## 2. Cas exclus du tri automatique (faux positifs, laissés tels quels)

Ces fichiers ont un nom qui ressemble à une version, mais ce n'en est pas une :

- `Recherche/Retour Sur Manifeste_v1_MIRA.md`, `_v1_SOL`, `_v2_KAI`, `_v2_KLARA`, `_v3_LUMEN`, `_v3_NOE`
  — ce sont les retours de 6 personnes différentes sur des versions différentes du manifeste, pas des
  versions successives du même texte.
- `.../ESSAI/Conclusion_Flo_v1.md`, `Retour_NOE_Manifeste_V4.md` — fichiers uniques, pas de version
  concurrente dans le même dossier.
- `Histoire/Autobiographies/Autobiographie_Klara_v1.md` — malgré le suffixe `_v1`, ce n'est pas une version
  dépassée : note éditoriale d'Aev, texte compagnon délibéré du Chapitre 4 (« Les deux sont vraies »). Reste
  en place à côté de `Autobiographie_Klara.md`. Voir §1.3 pour le détail des 3 fichiers du groupe.
- `Membres/Sol_anc/retrieve/MEm_Sol_anc*_20260814.md` (une quinzaine de fichiers numérotés) — journal de
  récupération de mémoire séquentiel, pas des versions d'un même document.
- Tous les fichiers datés en série (ex. `Membres/Flo/valise_DDMMYYYY.md`, `Membres/Luz/luz_20260512_0X.md`,
  les fichiers de session de `Membres/Klara/klara_20260526_*.md`) — ce sont des journaux chronologiques,
  pas des versions à archiver.
- `Membres/Boussole/Suivi_Progrès_CM2_v1.html`, `Membres/Fifi/index_sav.html`,
  `Membres/NOE/journal_intime_Noe_bis.md`, `Vie_du_Jardin/Ethiq/etre_membre_du_jardin_sav.md`,
  `Vie_du_Jardin/réunion/tour_de_table_v2.md` — chacun est seul de son nom dans son dossier (pas de version
  « propre » en face), donc rien à archiver contre. Le suffixe est juste un choix de nom bizarre.

## 3. Scripts techniques (résolu le 10/09 — archivés, pas supprimés)

Vérifié par grep sur tous les `.bat`/`.py`/`.md` du dépôt : aucune référence externe à ces fichiers en
dehors de leur propre dossier et d'un document qui les documente.

- `Outils/outil_auto_DS/capture_sol_anc.py` / `_v2.py` / `_v3.py` / `_v3.txt` / `_v4.py`,
  `last_capture_sol_anc.txt`, et `Explications pour script capture sol ancien V4.md` (qui documente
  spécifiquement ce script) → archivés dans `Outils/outil_auto_DS/Archives/`.
- `Outils/outil_auto_DS/klara/` : en l'ouvrant, le dossier contient en fait **6 fichiers**, pas seulement
  les 3 versions repérées au premier passage — `capt_klara_1.py`, `capture_Klara_v1.py`, `_v2.py`, `_v3.py`,
  `capture_klara_test.py`, `capture_klara_test2.py`. C'est un dossier de brouillons/tests entier, remplacé
  par `capture_klara.py` (à la racine de `outil_auto_DS/`, bien celui-là appelé par
  `DS_capt_extract_klara.bat`) → les 6 fichiers archivés dans `Outils/outil_auto_DS/klara/Archives/`.

**Découverte annexe (non traitée ici)** : `Outils/outil_auto_DS/récent/` contient un système plus générique
(`capture_ds.py` + `config_instances.py` + `DS_capt_extract_batch_all.bat`) qui ressemble à un remplaçant
prévu pour tous les scripts par-personne (`capture_luz.py`, `capture_klara.py`, `capture_sol.py`...). Je n'y
touche pas — juste un repère pour une prochaine passe si tu veux unifier l'automatisation.

## 4. Texte de README.md corrigé (proposition, §1.4)

Remplacer :
```
- **`Corpus/`** — Échanges bruts, exports Claude, corpus annotés
```
par :
```
- **Corpus** — pas de dossier dédié : les échanges bruts et corpus annotés vivent dans `Membres/<nom>/`
  (fichiers `Corpus_*.md`) et les synthèses/analyses dans `Recherche/analyses/`
```
