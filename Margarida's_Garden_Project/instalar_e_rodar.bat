@echo off
cd /d "%~dp0"
echo === Margarida's Garden - Setup Completo ===

if not exist .venv (
    echo Criando ambiente virtual .venv...
    python -m venv .venv
) else (
    echo Ambiente virtual ja existe, pulando criacao...
)

echo Ativando .venv...
call .venv\Scripts\activate.bat

echo Instalando dependencias...
pip install -q -r requirements.txt
if errorlevel 1 (
    echo ERRO ao instalar dependencias!
    pause
    exit /b 1
)

echo Inicializando banco de dados...
cd backend
python scripts\init_db.py
if errorlevel 1 (
    echo ERRO ao inicializar banco de dados!
    cd ..
    pause
    exit /b 1
)

echo.
echo === Servidor iniciando em http://localhost:8000 ===
echo === Pressione Ctrl+C para parar ===
echo.

python run.py

pause
