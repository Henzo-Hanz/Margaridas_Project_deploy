"""Script para inicializar banco e criar usuário padrão."""
import sys
from pathlib import Path

# Adiciona backend ao path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.core.database import SessionLocal, engine, Base
from app.core.security import get_password_hash
from app.core.config import settings
from app.models.user import User


def init_db():
    """Cria tabelas e usuário padrão Margarida."""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(User).filter(User.email == settings.DEFAULT_USER_EMAIL).first():
            print("Usuário Margarida já existe.")
            return
        user = User(
            name=settings.DEFAULT_USER_NAME,
            email=settings.DEFAULT_USER_EMAIL,
            hashed_password=get_password_hash(settings.DEFAULT_USER_PASSWORD),
        )
        db.add(user)
        db.commit()
        print(f"Usuário '{settings.DEFAULT_USER_NAME}' criado com sucesso!")
        print(f"  Email: {settings.DEFAULT_USER_EMAIL}")
        print(f"  Senha: {settings.DEFAULT_USER_PASSWORD}")
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
