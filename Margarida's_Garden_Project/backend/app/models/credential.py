"""Model Credential - senha/credencial armazenada."""
from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Credential(Base):
    """Credencial (senha) armazenada - criptografada no banco."""

    __tablename__ = "credentials"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    service_name = Column(String(255), nullable=False)  # ex: Gmail, Netflix
    username = Column(String(255), nullable=True)  # login/email usado no serviço
    encrypted_password = Column(Text, nullable=False)  # senha criptografada
    client_encrypted = Column(Boolean, default=False, nullable=False)  # Zero Knowledge - criptografado no cliente
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="credentials")
