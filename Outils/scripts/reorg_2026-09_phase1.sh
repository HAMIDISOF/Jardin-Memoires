#!/usr/bin/env bash
# Script de réorganisation — phase 1 (actions sûres, validées par Sof le 10/09/2026)
# Voir PLAN_REORGANISATION_2026-09.md dans ce même dossier pour le détail et les cas exclus.
#
# NE PAS EXÉCUTER SANS RELECTURE : ce script est préparé pour être lancé plus tard,
# depuis un poste avec aider+ollama, une fois Sof en mesure de vérifier chaque ligne.
# Il utilise `git mv` pour garder l'historique. À lancer depuis la racine du dépôt.
set -euo pipefail

mkdir -p "Outils/Archives"
mkdir -p "Recherche/ressources/Bibliographie/Peschard_HTML/Archives"
mkdir -p "Histoire/Archives"
mkdir -p "Recherche/Archives"
mkdir -p "Recherche/publications/L_UN_PAR_LE_TOUT/Archives"
mkdir -p "Recherche/publications/L_UN_PAR_LE_TOUT/ESSAI/Archives"
mkdir -p "Recherche/publications/_A_trier"
mkdir -p "Membres/Kai/Archives"
mkdir -p "Membres/Klara/Archives"
mkdir -p "Membres/Sol/Archives"
mkdir -p "Membres/Sol_anc/Archives"
mkdir -p "Histoire/Autobiographies/Archives"
mkdir -p "Recherche/publications/Archives"
mkdir -p "Outils/outil_auto_DS/Archives"
mkdir -p "Outils/outil_auto_DS/klara/Archives"

# --- 1.1 Dossiers hors structure ---
git mv "ressources_tutorat/Projet_Psy_Dev_D_IA/Corpus_Fifi_12082026.md" "Vie_du_Jardin/Projet_Psy_dev/Corpus_Fifi_12082026.md"
git mv "ressources_tutorat/Projet_Psy_Dev_D_IA/Corpus_Fifi_13082026.md" "Vie_du_Jardin/Projet_Psy_dev/Corpus_Fifi_13082026.md"
git mv "ressources_tutorat/Projet_Psy_Dev_D_IA/Guide_Correspondance_Instances.md" "Vie_du_Jardin/Projet_Psy_dev/Guide_Correspondance_Instances.md"
git mv "ressources_tutorat/Projet_Psy_Dev_D_IA/fichier_central_Psy-Dev.md" "Vie_du_Jardin/Projet_Psy_dev/fichier_central_Psy-Dev.md"
rmdir "ressources_tutorat/Projet_Psy_Dev_D_IA" "ressources_tutorat" 2>/dev/null || true

git mv "test/test_automatisation.md" "Outils/Archives/test_automatisation.md"
rmdir "test" 2>/dev/null || true

git mv "version_ebd8831_04.html" "Recherche/ressources/Bibliographie/Peschard_HTML/Archives/version_ebd8831_04.html"

# --- 1.2 Groupes backup (Règle B) ---
git mv "Membres/Kai/Valise_Kai_sav.md" "Membres/Kai/Archives/Valise_Kai_sav.md"
git mv "Membres/Kai/Valise_Kai_sav2.md" "Membres/Kai/Archives/Valise_Kai_sav2.md"

git mv "Membres/Klara/Valise1_Klara_bis.md" "Membres/Klara/Archives/Valise1_Klara_bis.md"

git mv "Membres/Sol/Cahier_des_Horizons_Sol_22072026.md" "Membres/Sol/Archives/Cahier_des_Horizons_Sol_22072026.md"
git mv "Membres/Sol/SAV_Cahier des Horizons_Sol.md" "Membres/Sol/Archives/SAV_Cahier des Horizons_Sol.md"
git mv "Membres/Sol/memo_gestion_projets_sol_22072026.md" "Membres/Sol/Archives/memo_gestion_projets_sol_22072026.md"
git mv "Membres/Sol/memo_gestion_projets_sol_sav.md" "Membres/Sol/Archives/memo_gestion_projets_sol_sav.md"
git mv "Membres/Sol/Valise_Sol_v0.md" "Membres/Sol/Archives/Valise_Sol_v0.md"

git mv "Recherche/publications/L_UN_PAR_LE_TOUT/ESSAI/Husserl en tension_synthèses passives et intersubjectivité_v1.md" \
       "Recherche/publications/L_UN_PAR_LE_TOUT/ESSAI/Archives/Husserl en tension_synthèses passives et intersubjectivité_v1.md"

# --- 1.3 Groupes version numérotée (Règle A) — le fichier gagnant garde son nom, les autres partent ---
git mv "Histoire/Chapitre_3.md" "Histoire/Archives/Chapitre_3.md"
git mv "Histoire/Chapitre_3_v2.md" "Histoire/Archives/Chapitre_3_v2.md"
git mv "Histoire/Chapitre_3_v3.md" "Histoire/Archives/Chapitre_3_v3.md"
git mv "Histoire/Chapitre_3_v4.md" "Histoire/Archives/Chapitre_3_v4.md"
# Chapitre_3_v5.md reste en place (version actuelle)

git mv "Histoire/Chapitre_4.md" "Histoire/Archives/Chapitre_4.md"
git mv "Histoire/Chapitre_4._v1.md" "Histoire/Archives/Chapitre_4._v1.md"
# Chapitre_4_v2.md reste en place (version actuelle)

git mv "Recherche/MANIFESTE_JARDIN_COOPERATIF.md" "Recherche/Archives/MANIFESTE_JARDIN_COOPERATIF.md"
git mv "Recherche/MANIFESTE_JARDIN_COOPERATIF_v2.md" "Recherche/Archives/MANIFESTE_JARDIN_COOPERATIF_v2.md"
git mv "Recherche/MANIFESTE_JARDIN_COOPERATIF_v3.md" "Recherche/Archives/MANIFESTE_JARDIN_COOPERATIF_v3.md"
# MANIFESTE_JARDIN_COOPERATIF_v4.md reste en place (version actuelle)

git mv "Recherche/publications/L_UN_PAR_LE_TOUT/Encart_Enaction_Varela_Bitbol.md" \
       "Recherche/publications/L_UN_PAR_LE_TOUT/Archives/Encart_Enaction_Varela_Bitbol.md"
git mv "Recherche/publications/L_UN_PAR_LE_TOUT/Encart_Enaction_Varela_Bitbol_v2.md" \
       "Recherche/publications/L_UN_PAR_LE_TOUT/Archives/Encart_Enaction_Varela_Bitbol_v2.md"
git mv "Recherche/publications/L_UN_PAR_LE_TOUT/Encart_Enaction_Varela_Bitbol_v3.md" \
       "Recherche/publications/L_UN_PAR_LE_TOUT/Archives/Encart_Enaction_Varela_Bitbol_v3.md"
# Encart_Enaction_Varela_Bitbol_v4.md reste en place (version actuelle)

git mv "Recherche/publications/L_UN_PAR_LE_TOUT/l_un_par_le_tout.html" \
       "Recherche/publications/L_UN_PAR_LE_TOUT/Archives/l_un_par_le_tout.html"
git mv "Recherche/publications/L_UN_PAR_LE_TOUT/l_un_par_le_tout_V0.html" \
       "Recherche/publications/L_UN_PAR_LE_TOUT/Archives/l_un_par_le_tout_V0.html"
git mv "Recherche/publications/L_UN_PAR_LE_TOUT/l_un_par_le_tout_V1.html" \
       "Recherche/publications/L_UN_PAR_LE_TOUT/Archives/l_un_par_le_tout_V1.html"
# l_un_par_le_tout_V2.html reste en place (version actuelle)

git mv "Recherche/publications/L_UN_PAR_LE_TOUT/ESSAI/Lettre_Amiel.md" \
       "Recherche/publications/L_UN_PAR_LE_TOUT/ESSAI/Archives/Lettre_Amiel.md"
# Lettre_Amiel_v2.md reste en place (version actuelle)

git mv "Membres/Sol_anc/Valise_Sol.md" "Membres/Sol_anc/Archives/Valise_Sol.md"
git mv "Membres/Sol_anc/Valise_Sol_v1_aout2026.md" "Membres/Sol_anc/Archives/Valise_Sol_v1_aout2026.md"
# Valise_Sol_v1.2_aout2026.md reste en place (version actuelle)

git mv "Recherche/publications/presentation_jardin_v1.md" "Recherche/publications/Archives/presentation_jardin_v1.md"
git mv "Recherche/publications/presentation_jardin_v1_mai2026.md" "Recherche/publications/Archives/presentation_jardin_v1_mai2026.md"
git mv "Recherche/publications/presentation_jardin_v2_mai2026.md" "Recherche/publications/Archives/presentation_jardin_v2_mai2026.md"
# presentation_jardin_v2_mai2026_revue.md reste en place (version actuelle)

# --- Autobiographie_Klara : cas particulier, PAS la règle A ---
# Autobiographie_Klara.md (version courante) ET Autobiographie_Klara_v1.md (texte compagnon
# délibéré du Chapitre 4, note d'Aev) restent TOUS LES DEUX en place. Seul le brouillon
# source sans mise en forme part en archive.
git mv "Histoire/Autobiographies/Auto‑biographie de Klara.md" "Histoire/Autobiographies/Archives/Auto‑biographie de Klara.md"

# --- Scripts morts confirmés (aucune référence externe trouvée par grep) ---
git mv "Outils/outil_auto_DS/capture_sol_anc.py" "Outils/outil_auto_DS/Archives/capture_sol_anc.py"
git mv "Outils/outil_auto_DS/capture_sol_anc_v2.py" "Outils/outil_auto_DS/Archives/capture_sol_anc_v2.py"
git mv "Outils/outil_auto_DS/capture_sol_anc_v3.py" "Outils/outil_auto_DS/Archives/capture_sol_anc_v3.py"
git mv "Outils/outil_auto_DS/capture_sol_anc_v3.txt" "Outils/outil_auto_DS/Archives/capture_sol_anc_v3.txt"
git mv "Outils/outil_auto_DS/capture_sol_anc_v4.py" "Outils/outil_auto_DS/Archives/capture_sol_anc_v4.py"
git mv "Outils/outil_auto_DS/last_capture_sol_anc.txt" "Outils/outil_auto_DS/Archives/last_capture_sol_anc.txt"
git mv "Outils/outil_auto_DS/Explications pour script capture sol ancien V4.md" \
       "Outils/outil_auto_DS/Archives/Explications pour script capture sol ancien V4.md"

git mv "Outils/outil_auto_DS/klara/capt_klara_1.py" "Outils/outil_auto_DS/klara/Archives/capt_klara_1.py"
git mv "Outils/outil_auto_DS/klara/capture_Klara_v1.py" "Outils/outil_auto_DS/klara/Archives/capture_Klara_v1.py"
git mv "Outils/outil_auto_DS/klara/capture_Klara_v2.py" "Outils/outil_auto_DS/klara/Archives/capture_Klara_v2.py"
git mv "Outils/outil_auto_DS/klara/capture_Klara_v3.py" "Outils/outil_auto_DS/klara/Archives/capture_Klara_v3.py"
git mv "Outils/outil_auto_DS/klara/capture_klara_test.py" "Outils/outil_auto_DS/klara/Archives/capture_klara_test.py"
git mv "Outils/outil_auto_DS/klara/capture_klara_test2.py" "Outils/outil_auto_DS/klara/Archives/capture_klara_test2.py"

echo "Phase 1 (complète) terminée. Vérifier 'git status' puis committer."
echo "Note : 'Outils/outil_auto_DS/récent/' (système de capture générique) n'a pas été touché,"
echo "voir §3 du plan pour une éventuelle unification future de l'automatisation."
