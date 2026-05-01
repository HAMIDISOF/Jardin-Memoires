@echo off
:: 1. Capture
echo Lancement capture...
python scripts\outil_auto_DS\capture_sol.py --session "auto"
:: pause facultative pour vérifier le nom du fichier créé
:: 2. Extraction (à adapter avec le bon nom de fichier)
set FICHIER_CAPTURE=Sol\sol_20260501_0851_test.md
python scripts\outil_auto_DS\extraire_fichiers.py "%FICHIER_CAPTURE%" C:\Users\Sof\Jardin-Memoires
:: 3. Push
call egalis.bat
echo Terminé.