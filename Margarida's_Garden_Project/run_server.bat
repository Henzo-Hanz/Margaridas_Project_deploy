@echo off
REM Ativa o venv e roda o servidor
call .venv\Scripts\activate.bat
python backend/run.py
pause
