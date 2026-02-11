"""Model Income - renda/receita rastreada."""
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Income(Base):
    """Receita/Renda registrada no Treasury."""

    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)  # ex: Salário, Freelance
    value = Column(Float, nullable=False)  # valor da renda
    date = Column(DateTime(timezone=True), nullable=False, server_default=func.now())  # data da renda
    notes = Column(String(500), nullable=True)  # anotações adicionais
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="incomes")
