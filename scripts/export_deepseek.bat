@echo off
echo === Export DeepSeek vers Markdown ===
echo.
echo Installation des dependances si necessaire...
pip install selenium webdriver-manager --break-system-packages --quiet
echo.
cd /d "%~dp0"
python export_deepseek.py
echo.
pause
