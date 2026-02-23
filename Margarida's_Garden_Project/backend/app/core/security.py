"""Utilitários de segurança: hash de senhas, JWT, criptografia."""
import base64
import hashlib
import os
import secrets
from datetime import datetime, timedelta
from typing import Optional

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

# Contexto para hash de senhas de usuário
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha em texto corresponde ao hash."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Gera hash bcrypt da senha."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Cria token JWT."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=60))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_token(token: str) -> Optional[dict]:
    """Decodifica e valida token JWT."""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None


def _get_encryption_key() -> bytes:
    """Deriva chave de criptografia a partir da SECRET_KEY."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"margarida_garden_salt",
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(settings.SECRET_KEY.encode()))
    return key


def encrypt_password(plain_password: str) -> str:
    """Criptografa senha armazenada (credencial) para guardar no banco."""
    fernet = Fernet(_get_encryption_key())
    return fernet.encrypt(plain_password.encode()).decode()


def decrypt_password(encrypted_password: str) -> str:
    """Descriptografa senha armazenada para exibir ao usuário."""
    fernet = Fernet(_get_encryption_key())
    return fernet.decrypt(encrypted_password.encode()).decode()


def generate_salt_preview() -> str:
    """Gera string aleatória com aparência de encriptação/salt para animação."""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789$@&!#%"
    return "".join(secrets.choice(chars) for _ in range(20))


# ============ Dependência FastAPI para autenticação ============

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user import User

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
) -> User:
    """Valida token JWT e retorna usuário autenticado."""
    try:
        token = credentials.credentials
        payload = decode_token(token)
        
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido ou expirado",
            )
        
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário não encontrado no token",
            )
        
        user = db.query(User).filter(User.id == int(user_id)).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuário não existe",
            )
        
        return user
    except HTTPException:
        raise
    except Exception as e:
        import traceback
        error_msg = f"Erro ao validar token: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)  # Log para stdout
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro de autenticação: {str(e)}"
        )
