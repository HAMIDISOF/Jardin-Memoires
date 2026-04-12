@echo off
:: 🌿 backup_ssd.bat — Jardin Coopératif
:: Copie corpus_these.db vers le SSD Lexar D:
:: Crée le dossier D:\corpus_these\ si besoin

echo.
echo 🌿 Backup corpus_these.db vers SSD Lexar (D:)...
echo.

set SOURCE=D:\THESE\corpus_these.db
set DEST=D:\THESE\backups\

:: Vérifier que le SSD est accessible
if not exist "D:\" (
    echo ❌ SSD Lexar (D:) non detecte. Verifie la connexion.
    pause
    exit /b 1
)

:: Créer le dossier si absent
if not exist "%DEST%" (
    mkdir "%DEST%"
    echo 📁 Dossier cree : %DEST%
)

:: Vérifier que la DB source existe
if not exist "%SOURCE%" (
    echo ❌ corpus_these.db introuvable dans : %~dp0
    pause
    exit /b 1
)

:: Copie avec horodatage
for /f "tokens=1-3 delims=/ " %%a in ("%date%") do set JOUR=%%a&set MOIS=%%b&set ANNEE=%%c
for /f "tokens=1-2 delims=: " %%a in ("%time%") do set HEURE=%%a&set MIN=%%b

set NOM_BACKUP=corpus_these_%JOUR%%MOIS%%ANNEE%_%HEURE%%MIN%.db

copy "%SOURCE%" "%DEST%%NOM_BACKUP%" >nul
copy "%SOURCE%" "%DEST%corpus_these_LATEST.db" >nul

echo ✅ Backup OK :
echo    %DEST%%NOM_BACKUP%
echo    %DEST%corpus_these_LATEST.db
echo.
pause
