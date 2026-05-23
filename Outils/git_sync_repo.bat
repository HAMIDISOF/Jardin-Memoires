@echo off
setlocal enabledelayedexpansion

REM ---------- Configuration ----------
set BRANCH=main
set REMOTE=origin

REM ---------- Aller à la racine du dépôt (si le script est dans le dépôt) ----------
cd /d "%~dp0"
echo [INFO] Dépôt : %cd%

REM ---------- 1. Ajouter tous les changements ----------
git add -A
if %errorlevel% neq 0 ( echo [ERREUR] git add a échoué & exit /b 1 )

REM ---------- 2. Vérifier s'il y a des modifications à commiter ----------
git diff --cached --quiet
if %errorlevel% equ 0 (
    echo [INFO] Aucune modification à commiter.
) else (
    echo [INFO] Modifications détectées, commit en cours...
    git commit -m "Auto commit %date% %time%"
    if %errorlevel% neq 0 ( echo [ERREUR] git commit a échoué & exit /b 1 )
)

REM ---------- 3. Pull avec rebase ----------
echo [INFO] Pull --rebase depuis %REMOTE%/%BRANCH%...
git pull --rebase %REMOTE% %BRANCH%
if %errorlevel% neq 0 (
    echo [ATTENTION] Conflit detecte lors du rebase. Annulation...
    git rebase --abort
    echo [ERREUR] Pull --rebase echoue. Resolvez manuellement, puis relancez.
    exit /b 1
)

REM ---------- 4. Push ----------
echo [INFO] Push vers %REMOTE%/%BRANCH%...
git push %REMOTE% %BRANCH%
if %errorlevel% neq 0 (
    echo [ERREUR] Push echoue (verifiez vos droits ou le reseau).
    exit /b 1
)

echo [SUCCES] Synchronisation terminee.
exit /b 0