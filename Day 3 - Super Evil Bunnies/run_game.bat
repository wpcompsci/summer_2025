@echo off
cd /d "%~dp0"
set PYTHONDONTWRITEBYTECODE=1
echo Running seb.py from %CD%
python seb.py
pause
