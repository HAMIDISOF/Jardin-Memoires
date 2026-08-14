@echo off
setlocal

:: ============================================================
:: DS_capt_extract.bat  (version unifiée)
:: Pipeline complet pour UNE instance : capture -> extraction -> push
:: Usage : DS_capt_extract.bat <instance> [nom_session]
:: Exemple : DS_capt_extract.bat sol simondon
:: ============================================================

set INSTANCE=%~1
if "%INSTANCE%"=="" (
    echo ERREUR : precise une instance. Usage : DS_capt_extract.bat ^<instance^> [nom_session]
    echo Instances connues : sol, klara, luz, kai, racine, noe
    exit /b 1
)

set SESSION=%~2
if "%SESSION%"=="" set SESSION=auto

set REPO=D:\THESE\Les journaux\Jardin-Memoires
set SCRIPTS=%REPO%\scripts\outil_auto_DS
set LAST_CAPTURE=%SCRIPTS%\last_capture_%INSTANCE%.txt

cd /d "%REPO%"

echo.
echo [1/3] Capture de la conversation %INSTANCE%...
python "%SCRIPTS%\capture_ds.py" --instance "%INSTANCE%" --session "%SESSION%"
if errorlevel 1 (
    echo ERREUR lors de la capture. Abandon, rien n'est pousse.
    exit /b 1
)

if not exist "%LAST_CAPTURE%" (
    echo ERREUR : %LAST_CAPTURE% introuvable. Abandon.
    exit /b 1
)
set /p FICHIER_CAPTURE=<"%LAST_CAPTURE%"
echo Fichier capture : %FICHIER_CAPTURE%

echo.
echo [2/3] Extraction des fichiers balises...
python "%SCRIPTS%\extraire_fichiers.py" "%FICHIER_CAPTURE%" "%REPO%"

echo.
echo [3/3] Synchronisation git...
call "%REPO%\egalis.bat"

echo.
echo Pipeline termine pour %INSTANCE%.
endlocal
