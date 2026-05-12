@echo off
cd /d "D:\THESE\Les journaux\Jardin-Memoires\scripts\outil_auto_DS"

REM Paramètre : nom de session (optionnel)
set SESSION=%1
if "%SESSION%"=="" set SESSION=auto

REM Capture
echo 📸 Capture de la session %SESSION%...
python capture_luz.py --session "%SESSION%"
if errorlevel 1 (
    echo ❌ Erreur lors de la capture
    pause
    exit /b 1
)

REM Lecture du fichier produit
set /p CAPTURE_FILE=<last_capture_luz.txt
if not exist "%CAPTURE_FILE%" (
    echo ❌ Fichier de capture introuvable : %CAPTURE_FILE%
    pause
    exit /b 1
)

REM Extraction
echo 📄 Extraction des fichiers balises...
python extraire_fichiers.py "%CAPTURE_FILE%" "D:\THESE\Les journaux\Jardin-Memoires"

echo ✅ Terminé. Vérifie les fichiers, puis push manuel.
pause