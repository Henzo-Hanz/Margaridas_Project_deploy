"""Schemas para Expense."""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from enum import Enum


class PaymentMethodSchema(str, Enum):
    """Métodos de pagamento."""
    CARD = "card"
    CASH = "cash"
    TRANSFER = "transfer"
    DEBIT = "debit"
    PIX = "pix"
    BILL = "bill"


class ExpenseCreate(BaseModel):
    """Schema para criar despesa."""
    name: str = Field(..., min_length=1, max_length=255)
    value: float = Field(..., gt=0)
    date: Optional[datetime] = None
    method: PaymentMethodSchema = PaymentMethodSchema.CARD
    notes: Optional[str] = None


class ExpenseUpdate(BaseModel):
    """Schema para atualizar despesa."""
    name: Optional[str] = None
    value: Optional[float] = None
    date: Optional[datetime] = None
    method: Optional[PaymentMethodSchema] = None
    notes: Optional[str] = None


class ExpenseResponse(BaseModel):
    """Schema para resposta de despesa."""
    id: int
    name: str
    value: float
    date: datetime
    method: PaymentMethodSchema
    notes: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
