@echo off
:: 🌿 init_corpus.bat — Jardin Coopératif
:: Initialise la base SQLite corpus_these.db
:: A lancer une seule fois (ou sans danger si déjà existante)

echo.
echo 🌿 Initialisation base corpus these...
echo.

cd /d D:\THESE
py -3.11 init_corpus.py

echo.
pause
