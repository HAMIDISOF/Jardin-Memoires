@echo off
:: 🌿 zip_semaine.bat — Jardin Coopératif
:: Zippe tous les .md du dossier courant
:: Nomme le zip : corpus_semaine_JJMMAAAA.zip
:: Copie aussi le zip sur SSD D:

echo.
echo 🌿 Archivage .md de la semaine...
echo.

:: Vérifier que zip est disponible (PowerShell natif Windows 10+)
where powershell >nul 2>&1
if errorlevel 1 (
    echo ❌ PowerShell requis (Windows 10+)
    pause
    exit /b 1
)

:: Horodatage
for /f "tokens=1-3 delims=/ " %%a in ("%date%") do set JOUR=%%a&set MOIS=%%b&set ANNEE=%%c
set NOM_ZIP=corpus_semaine_%JOUR%%MOIS%%ANNEE%.zip
set DEST_LOCAL=D:\THESE\archives\%NOM_ZIP%

:: Créer dossier archives
if not exist "D:\THESE\archives\" mkdir "D:\THESE\archives\"

:: Zipper tous les .md de D:\THESE\
powershell -Command "Compress-Archive -Path 'D:\THESE\*.md' -DestinationPath '%DEST_LOCAL%' -Force"

if errorlevel 1 (
    echo ❌ Erreur lors du zip. Aucun .md trouve ?
    pause
    exit /b 1
)

echo ✅ Zip cree : %DEST_LOCAL%
echo    (directement sur SSD D:\THESE\archives\)

echo.
pause
