"""Schemas para Income."""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class IncomeCreate(BaseModel):
    """Schema para criar receita."""
    name: str = Field(..., min_length=1, max_length=255)
    value: float = Field(..., gt=0)
    date: Optional[datetime] = None
    notes: Optional[str] = None


class IncomeUpdate(BaseModel):
    """Schema para atualizar receita."""
    name: Optional[str] = None
    value: Optional[float] = None
    date: Optional[datetime] = None
    notes: Optional[str] = None


class IncomeResponse(BaseModel):
    """Schema para resposta de receita."""
    id: int
    name: str
    value: float
    date: datetime
    notes: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
