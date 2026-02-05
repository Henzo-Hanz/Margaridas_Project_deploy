"""Schemas de usuário."""
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """Schema para criação de usuário."""

    name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """Schema de resposta de usuário (sem senha)."""

    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    """Schema de token JWT."""

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Dados extraídos do token."""

    user_id: Optional[int] = None
    email: Optional[str] = None
