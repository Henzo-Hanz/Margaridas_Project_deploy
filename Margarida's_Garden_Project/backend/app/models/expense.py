"""Model Expense - despesa rastreada."""
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.core.database import Base


class PaymentMethod(str, enum.Enum):
    """Métodos de pagamento."""
    CARD = "card"
    CASH = "cash"
    TRANSFER = "transfer"
    DEBIT = "debit"
    PIX = "pix"
    BILL = "bill"


class Expense(Base):
    """Despesa registrada no Treasury."""

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)  # ex: Supermercado, Aluguel
    value = Column(Float, nullable=False)  # valor da despesa
    date = Column(DateTime(timezone=True), nullable=False, server_default=func.now())  # data da despesa
    method = Column(SQLEnum(PaymentMethod), nullable=False, default=PaymentMethod.CARD)  # método de pagamento
    notes = Column(String(500), nullable=True)  # anotações adicionais
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="expenses")
