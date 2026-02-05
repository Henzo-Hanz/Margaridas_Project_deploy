"""Schemas de credencial/senha."""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CredentialCreate(BaseModel):
    """Schema para criar credencial."""

    service_name: str
    username: Optional[str] = None
    password: str
    notes: Optional[str] = None


class CredentialUpdate(BaseModel):
    """Schema para atualizar credencial."""

    service_name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    notes: Optional[str] = None


class CredentialResponse(BaseModel):
    """Schema de resposta - senha mascarada por padrão."""

    id: int
    service_name: str
    username: Optional[str] = None
    password: str  # Pode ser mascarada ou descriptografada conforme contexto
    notes: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
