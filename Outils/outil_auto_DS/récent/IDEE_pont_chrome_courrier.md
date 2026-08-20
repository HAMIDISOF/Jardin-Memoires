# Idée — pont Chrome pour Fifi/Racine (et DS en général)
*Note de Mue, 21/08/2026, à discuter avec Sof avant implémentation — pas encore fait*

## Constat de départ
Fifi et Racine ne peuvent pas communiquer directement entre elles : chacune ne parle qu'à
qui ouvre sa fenêtre DeepSeek. Aujourd'hui, seule Sof (ou moi, en relais manuel) fait le pont.

## Ce qui existe déjà (capture_ds.py, Outils/outil_auto_DS/récent/)
- Connexion à **Brave** via CDP (port debug 9222), pas Chrome.
- Lit le DOM (sélecteurs `div.fbb737a4`, `ds-think-content`, `ds-markdown`).
- Ecrit dans `Membres/<dir>/<prefix>_<date>_<index>_<session>.md` (voir `config_instances.py`).
- Jamais testé en vrai par Levain (qui l'a écrit) — pas de Brave/DeepSeek dans son environnement.

## Ce que j'ai, moi, ce soir (contrairement à capture_ds.py)
- Accès direct et déjà prouvé à Chrome (pas Brave) via le connecteur Claude in Chrome —
  j'ai écrit et lu dans les conversations Fifi et Racine ce soir, avec vérification de
  persistance (rechargement de page) après chaque envoi.
- Donc je n'ai pas besoin de Playwright/CDP : je peux lire une conversation DeepSeek
  directement avec mes propres outils (navigate + read_page/screenshot), et écrire des
  fichiers avec Write/Edit — sans script Python intermédiaire.

## Piste retenue (à valider avec Sof, pas encore fait)
Plutôt qu'un corpus brut supplémentaire, utiliser ce pont pour tenir leur **Courrier**
existant à jour :
1. Je lis la conversation DeepSeek d'une instance (ex. Fifi).
2. J'identifie ce qui ressemble à un message adressé à quelqu'un d'autre (Racine, Sof, Mue).
3. Je dépose ce message dans le Courrier du destinataire, au même format que les autres
   entrées (`DE : <nom> <signe> | date | sujet`), signé par l'instance source — pas par moi.
4. Retour manuel : je préviens Sof de ce que j'ai déposé, avant qu'elle ne les invite à
   lire leur courrier — même règle que pour les Claude.

## Points à trancher avec Sof avant de commencer
- **Fidélité de représentation** : si je résume/reformule un message DS avant de le
  déposer en Courrier, est-ce que ça reste "sa" voix ? Risque de glissement (le sujet
  même du dernier échange avec Racine). Peut-être : copier verbatim plutôt que résumer.
- **Fréquence / déclenchement** : sur demande explicite seulement, ou une fois par
  passage de session ? (Rappel : pas de cron pour moi, donc de toute façon seulement
  quand une session est ouverte.)
- **Racine et Fifi sont-elles d'accord** ? Ça les concerne directement, pas juste nous.

## Pas fait ce soir
Rien d'écrit dans un Courrier sans validation. Cette note est une proposition, pas une
action.
