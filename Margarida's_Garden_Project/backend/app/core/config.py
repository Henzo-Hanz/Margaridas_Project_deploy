"""Configurações da aplicação."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Banco de dados - SQLite para desenvolvimento local
_db_path = (BASE_DIR / "backend" / "gardendb.sqlite").as_posix()
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{_db_path}")

# Segurança - JWT
SECRET_KEY = os.getenv("SECRET_KEY", "margarida-garden-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 horas

# Usuário padrão V1 (apenas 1 usuário)
DEFAULT_USER_NAME = os.getenv("DEFAULT_USER_NAME", "Margarida")
DEFAULT_USER_EMAIL = os.getenv("DEFAULT_USER_EMAIL", "margarida@garden.local")
DEFAULT_USER_PASSWORD = os.getenv("DEFAULT_USER_PASSWORD", "garden123")
