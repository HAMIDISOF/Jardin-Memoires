# outil_auto_DS — version consolidée (14/08/2026)

*Levain 🍞 — refonte du script que Flo avait fait, pour passer à quelque chose de paramétré plutôt que dupliqué par instance*

## Ce qui a changé

**Avant** : un fichier `capture_<instance>.py` distinct par instance (Sol, Kai, Klara, Luz), plus plusieurs versions abandonnées en cours de route (`capture_luz_v2.py`, `capture_sol_anc_v2/v3/v4.py`...). Chaque nouvelle instance = copier-coller-adapter un script entier. Ajouter Racine ou NOE aurait voulu dire un cinquième fichier quasi identique.

**Maintenant** :
- `config_instances.py` — un seul endroit où déclarer une instance (dossier, préfixe de nommage, indice pour repérer son onglet). Ajouter Racine ou NOE = une ligne, pas un fichier.
- `capture_ds.py` — un seul script de capture, paramétré par `--instance`. La logique DOM (sélecteurs CSS, découpage thinking/réponse) est reprise à l'identique de `capture_sol.py` — c'est la partie qui marchait, elle n'a pas été retouchée.
- `DS_capt_extract.bat` — un seul batch pour une instance : `DS_capt_extract.bat sol simondon`.
- `DS_capt_extract_batch_all.bat` — nouveau : capture + extrait **toutes** les instances configurées à la suite (utile si plusieurs conversations DeepSeek tournent en parallèle), mais **ne pousse jamais automatiquement**. Il capture tout en local, affiche un `git status` récapitulatif, et demande une confirmation explicite (o/n) avant un push unique pour tout le monde. C'est la version "pas casse-gueule" — le point qui inquiétait le plus dans la version précédente.

`extraire_fichiers.py` et le format de balisage (`RAPPEL_BALISAGE.md`) n'ont pas changé — ils étaient déjà génériques, pas besoin d'y toucher.

## Le point qui reste à surveiller

Plusieurs onglets DeepSeek partagent la même URL (`chat.deepseek.com`) — le script ne peut donc pas deviner tout seul lequel est Sol et lequel est Racine si les deux sont ouverts en même temps. Il essaie de matcher via le titre de l'onglet (`tab_hint` dans `config_instances.py`, ex. "Sol", "Racine"). Si ça ne suffit pas :
```
python capture_ds.py --list-tabs
```
liste les onglets ouverts avec leur index, et `--tab-index N` force le bon.

## Migration

1. Ce dossier (`récent/`) est autonome, à côté de l'ancien `outil_auto_DS/` — rien n'a été supprimé automatiquement.
2. Tester `capture_ds.py --instance sol` une fois pour vérifier que le comportement est identique à l'ancien `capture_sol.py`.
3. Une fois validé, tu peux archiver ou supprimer les anciens `capture_*.py` et `DS_capt_extract_*.bat` à la racine de `outil_auto_DS/` (les `capture_*_anc_v2/v3/v4.py` peuvent partir sans regret, c'étaient déjà des versions dépassées), et rapatrier le contenu de `récent/` à la racine.
4. Ajouter Racine et NOE a été fait directement dans `config_instances.py` — mais leur `tab_hint` ("Racine", "Noé") est une supposition sur le titre d'onglet DeepSeek, à vérifier/corriger la première fois.

## Non testé

Je n'ai pas pu tester la partie navigateur (connexion à Brave, extraction DOM réelle) — je n'ai pas de Brave/DeepSeek ouvert dans mon propre environnement. La logique d'extraction est copiée telle quelle de `capture_sol.py` qui, lui, était validé. Seule la partie autour (choix d'instance, choix d'onglet, nommage) est nouvelle et mériterait un premier essai prudent avant de faire confiance au batch multi-instances.
