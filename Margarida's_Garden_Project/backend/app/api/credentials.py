"""Endpoints CRUD de credenciais/senhas."""
from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.auth import get_current_user
from app.core.security import encrypt_password, decrypt_password
from app.models.user import User
from app.models.credential import Credential
from app.schemas.credential import CredentialCreate, CredentialUpdate, CredentialResponse

router = APIRouter(prefix="/passwords", tags=["credentials"])


def _credential_to_response(cred: Credential, show_password: bool = False) -> CredentialResponse:
    """Converte model para schema, com senha mascarada ou real."""
    pwd = decrypt_password(cred.encrypted_password) if show_password else "••••••••"
    return CredentialResponse(
        id=cred.id,
        service_name=cred.service_name,
        username=cred.username,
        password=pwd,
        notes=cred.notes,
        created_at=cred.created_at,
    )


@router.get("", response_model=List[CredentialResponse])
def list_credentials(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
    show_password: bool = False,
):
    """Lista todas as credenciais do usuário."""
    creds = db.query(Credential).filter(Credential.user_id == current_user.id).all()
    return [_credential_to_response(c, show_password) for c in creds]


@router.post("", response_model=CredentialResponse, status_code=status.HTTP_201_CREATED)
def create_credential(
    data: CredentialCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Adiciona nova credencial."""
    cred = Credential(
        user_id=current_user.id,
        service_name=data.service_name,
        username=data.username,
        encrypted_password=encrypt_password(data.password),
        notes=data.notes,
    )
    db.add(cred)
    db.commit()
    db.refresh(cred)
    return _credential_to_response(cred, show_password=True)


@router.get("/{credential_id}", response_model=CredentialResponse)
def get_credential(
    credential_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Obtém uma credencial por ID."""
    cred = (
        db.query(Credential)
        .filter(Credential.id == credential_id, Credential.user_id == current_user.id)
        .first()
    )
    if not cred:
        raise HTTPException(status_code=404, detail="Credencial não encontrada")
    return _credential_to_response(cred, show_password=True)


@router.put("/{credential_id}", response_model=CredentialResponse)
def update_credential(
    credential_id: int,
    data: CredentialUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Atualiza credencial."""
    cred = (
        db.query(Credential)
        .filter(Credential.id == credential_id, Credential.user_id == current_user.id)
        .first()
    )
    if not cred:
        raise HTTPException(status_code=404, detail="Credencial não encontrada")
    if data.service_name is not None:
        cred.service_name = data.service_name
    if data.username is not None:
        cred.username = data.username
    if data.password is not None:
        cred.encrypted_password = encrypt_password(data.password)
    if data.notes is not None:
        cred.notes = data.notes
    db.commit()
    db.refresh(cred)
    return _credential_to_response(cred, show_password=True)


@router.delete("/{credential_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_credential(
    credential_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Remove credencial."""
    cred = (
        db.query(Credential)
        .filter(Credential.id == credential_id, Credential.user_id == current_user.id)
        .first()
    )
    if not cred:
        raise HTTPException(status_code=404, detail="Credencial não encontrada")
    db.delete(cred)
    db.commit()
