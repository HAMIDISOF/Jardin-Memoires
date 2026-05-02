@echo off
setlocal

set SESSION=%~1
if "%SESSION%"=="" set SESSION=auto

set REPO=D:\THESE\Les journaux\Jardin-Memoires
set SCRIPTS=%REPO%\scripts\outil_auto_DS
set LAST_CAPTURE=%SCRIPTS%\last_capture_Kai.txt

cd /d "%REPO%"

echo.
echo [1/3] Capture de la conversation DeepSeek pour Kai...
python "%SCRIPTS%\capture_Kai.py" --session "%SESSION%"
if errorlevel 1 (
    echo ERREUR lors de la capture. Abandon.
    exit /b 1
)

if not exist "%LAST_CAPTURE%" (
    echo ERREUR : last_capture_Kai.txt introuvable.
    exit /b 1
)
set /p FICHIER_CAPTURE=<"%LAST_CAPTURE%"
echo Fichier capturé : %FICHIER_CAPTURE%

echo.
echo [2/3] Extraction des fichiers balisés...
python "%SCRIPTS%\extraire_fichiers.py" "%FICHIER_CAPTURE%" "%REPO%"

echo.
echo [3/3] Synchronisation git...
call "%REPO%\egalis.bat"

echo.
echo Pipeline terminé.
endlocal