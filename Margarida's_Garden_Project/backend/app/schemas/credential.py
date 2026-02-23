"""Schemas de credencial/senha."""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CredentialCreate(BaseModel):
    """Schema para criar credencial. Zero Knowledge: use password_encrypted. Legacy: use password."""

    service_name: str
    username: Optional[str] = None
    password: Optional[str] = None  # Legacy - servidor criptografa
    password_encrypted: Optional[str] = None  # Zero Knowledge - blob base64 já criptografado no cliente
    notes: Optional[str] = None


class CredentialUpdate(BaseModel):
    """Schema para atualizar credencial."""

    service_name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None  # Legacy
    password_encrypted: Optional[str] = None  # Zero Knowledge
    notes: Optional[str] = None


class CredentialResponse(BaseModel):
    """Schema de resposta. password: mascarada, real (legacy) ou blob base64 (client_encrypted)."""

    id: int
    service_name: str
    username: Optional[str] = None
    password: str
    client_encrypted: bool = False
    notes: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
