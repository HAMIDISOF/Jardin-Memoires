@echo off
:: 🌿 import_md.bat — Jardin Coopératif
:: Importe un fichier .md brut dans corpus_these.db
:: Usage : glisser-déposer le .md sur ce .bat
::         OU double-clic → saisir le chemin manuellement

echo.
echo 🌿 Import fichier .md dans le corpus...
echo.

if "%~1"=="" (
    set /p FICHIER="Chemin du fichier .md a importer : "
) else (
    set FICHIER=%~1
)

cd /d D:\THESE
py -3.11 init_corpus.py --import "%FICHIER%"

echo.
pause
