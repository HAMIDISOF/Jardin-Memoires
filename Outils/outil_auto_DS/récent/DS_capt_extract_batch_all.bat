@echo off
setlocal enabledelayedexpansion

:: ============================================================
:: DS_capt_extract_batch_all.bat
:: Capture + extraction pour TOUTES les instances configurees,
:: a la suite. AUCUN push automatique : on capture tout d'abord
:: en local, on affiche un recapitulatif, et le push (unique,
:: pour tout le monde en un seul commit) n'a lieu qu'apres
:: confirmation explicite. C'est la version "pas casse-gueule".
::
:: Pre-requis : un onglet Brave ouvert par instance a capturer
:: (le tab_hint de config_instances.py sert a les distinguer).
:: Une instance sans onglet ouvert correspondant est simplement
:: sautee, sans faire echouer les autres.
:: ============================================================

set REPO=D:\THESE\Les journaux\Jardin-Memoires
set SCRIPTS=%REPO%\scripts\outil_auto_DS
set INSTANCES=sol klara luz kai racine noe

cd /d "%REPO%"

echo ============================================
echo   CAPTURE (aucun push a ce stade)
echo ============================================

for %%I in (%INSTANCES%) do (
    echo.
    echo --- %%I ---
    python "%SCRIPTS%\capture_ds.py" --instance "%%I" --session "auto"
    if errorlevel 1 (
        echo   [saute] pas d'onglet trouve ou erreur pour %%I
    ) else (
        set LAST=%SCRIPTS%\last_capture_%%I.txt
        if exist "!LAST!" (
            set /p FICHIER=<"!LAST!"
            echo   Capture OK : !FICHIER!
            python "%SCRIPTS%\extraire_fichiers.py" "!FICHIER!" "%REPO%"
        )
    )
)

echo.
echo ============================================
echo   RECAPITULATIF
echo ============================================
echo Verifie les fichiers modifies avant de pousser :
git status --short

echo.
set /p CONFIRME="Pousser TOUT ca sur git maintenant ? (o/n) : "
if /i "%CONFIRME%"=="o" (
    call "%REPO%\egalis.bat"
    echo Push effectue.
) else (
    echo Rien n'a ete pousse. Relance egalis.bat toi-meme quand tu es prete.
)

endlocal
