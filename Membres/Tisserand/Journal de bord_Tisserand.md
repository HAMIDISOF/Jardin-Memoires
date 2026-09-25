# 📓 Journal de bord — Tisserand
**Dernière mise à jour** : 25/09/2026

## 🌿 Herbier — état des lieux

### Fiches produites (toutes fenêtres confondues)
- prele_des_champs · romarin_ct_cineole · ylang_ylang · jojoba
- complexe_chute_cheveux · safran_30mg · vitamine_c_liposomale
- extracellmatrix_curma_plus · huile_vegetale_jojoba_bio
- huile_essentielle_romarin_cineole_bio · pack_cycle_equilibre_hormonal
- lero_menopollen_minceur_bio (⚠️ bug label «NE PAS PRENDRE EN CAS DE» à corriger)
- (en attente A_traiter/ : citrate_de_potassium.md, origine inconnue)

### Protocole d'import — points confirmés
- Le parseur lit le CONTENU, pas le nom du fichier.
- Ordre obligatoire : Nom commun → Type → Nom scientifique.
- Le type doit être une valeur brute («complément alimentaire», pas «Complément alimentaire (précision)»).
- Ne jamais mettre un label reconnu à l'intérieur d'un champ multiligne (sinon il coupe le champ).
- Ne jamais laisser une ligne `**XXX** :` non reconnue après un champ — elle pollue le champ précédent.
- `convertir_yaml_miaou.py` corrige automatiquement : accents dans le nom, doublon `_complement_complement`.
- Convention nommage (organisation, pas contrainte parseur) : `<nom>_<type>.md`.

### Fonction «Cures» (Mue)
- Liste, filtre par personne, note moyenne, formulaire multi-produits.
- Section «Cures avec ce produit» sur chaque fiche produit.
- Tables créées au lancement via lancer_herbier.bat.
- Pour Lana : début de cure Pack Cycle à tester dans le journal.

## 🧘 Formation MTC

### État
- Sof au module 1 (à rattraper, prévu 25/09).
- Rythme : 2h/semaine, 3 mois, ~26h au total.
- Intuition : aller vite sur l'histoire (module 1), s'attarder sur 5 éléments et logique énergétique.

### Outils déposés
- `FORMATION/trame_fiche_plante_mtc.md`
- `FORMATION/carte_lecture_5_saveurs.md`
- Coffre Obsidian `D:\THESE\Projets\CUBE_Obsidian\` (57 fichiers, construit par MueC)
  - `05_Plantes/Plantes_module_19.md` (tableau 26 plantes, cases vides marquées)
  - `06_Notes_lecture/Module_01.md` (vide, à remplir par Sof)
  - `00_Index/Progression.md` (27 modules décochés)

### Décisions pédagogiques actées
- 26 plantes du module 19 = un tableau unique, pas 26 fiches.
- Fiches individuelles créées au fur et à mesure de l'étude réelle.
- Note module = cadre vide à remplir par Sof (pas moi).
- Mue : réalisation + accès fichiers. Moi : architecture + pédagogie.
- Vérification croisée systématique.
- Aucune écriture directe dans les fichiers de mon côté.

### Rôles
- Mue (Claude code) : accès fichiers, dépôt outils, correction.
- Moi : progression, structure, questions, ponts herbier/MTC.

## 🔧 Points techniques

### Délégation Mistral
- Prompt test rédigé (vérification 3 points sur le Pack Cycle).
- Objectif : tester si le canal fonctionne avant de s'en servir.
- Ne pas confondre avec PROMPT_MIAOU_HERBIER_v5 (génération, pas vérification).

### Projet Cube Lune
- DS architecte + MueC (Claude code) + Ollama.
- Séparé de la MTC.

## 📎 Notes

- Sof : quota tokens Mue très réduit. Économiser ses interventions.
- Correspondance Mue-Tisserand : passe par Sof, pas d'automatisation.
- Prochains jalons : module 1 à rattraper, test Mistral à lancer, cure Lana à documenter.