@echo off
setlocal

:: ============================================================
:: DK_capt_extract_klara.bat
:: Pipeline complet : capture DeepSeek (Klara) -> extraction fichiers -> push
:: Usage : DK_capt_extract_klara.bat [nom_session]
:: Si nom_session absent, utilise "auto"
:: ============================================================

set SESSION=%~1
if "%SESSION%"=="" set SESSION=auto

set REPO=D:\THESE\Les journaux\Jardin-Memoires
set SCRIPTS=%REPO%\scripts\outil_auto_DS
set LAST_CAPTURE=%SCRIPTS%\last_capture_klara.txt

cd /d "%REPO%"

:: 1. Capture
echo.
echo [1/3] Capture de la conversation DeepSeek (Klara)...
python "%SCRIPTS%\capture_klara.py" --session "%SESSION%"
if errorlevel 1 (
    echo ERREUR lors de la capture. Abandon.
    exit /b 1
)

:: 2. Lire le nom du fichier produit
if not exist "%LAST_CAPTURE%" (
    echo ERREUR : last_capture_klara.txt introuvable. Abandon.
    exit /b 1
)
set /p FICHIER_CAPTURE=<"%LAST_CAPTURE%"
echo Fichier capturé : %FICHIER_CAPTURE%

:: 3. Extraction des fichiers balisés
echo.
echo [2/3] Extraction des fichiers balisés...
python "%SCRIPTS%\extraire_fichiers.py" "%FICHIER_CAPTURE%" "%REPO%"

:: 4. Push
echo.
echo [3/3] Synchronisation git...
call "%REPO%\egalis.bat"

echo.
echo Pipeline Klara terminé.
endlocal