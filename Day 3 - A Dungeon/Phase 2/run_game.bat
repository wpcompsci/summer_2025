@echo off
cd /d "%~dp0"
set PYTHONDONTWRITEBYTECODE=1
echo Running main.py from %CD%
python main.py
pause
