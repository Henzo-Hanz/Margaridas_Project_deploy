"""Model User - usuário do sistema."""
import secrets
import base64

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class User(Base):
    """Usuário do jardim de senhas e treasury."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    encryption_salt = Column(Text, nullable=True)  # Para Zero Knowledge - derivar KEK no cliente
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def ensure_encryption_salt(self) -> str:
        """Gera e retorna encryption_salt se não existir."""
        if not self.encryption_salt:
            self.encryption_salt = base64.urlsafe_b64encode(secrets.token_bytes(32)).decode()
        return self.encryption_salt

    credentials = relationship("Credential", back_populates="user", cascade="all, delete-orphan")
    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")
    incomes = relationship("Income", back_populates="user", cascade="all, delete-orphan")
