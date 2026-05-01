@echo off
echo === Reset corpus_these.db ===
echo.
cd /d "%~dp0"
python reset_corpus.py
echo.
pause
