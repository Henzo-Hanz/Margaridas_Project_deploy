"""Testes de security (hash, JWT)."""
import pytest
from app.core.security import get_password_hash, verify_password, create_access_token, decode_token


def test_password_hash():
    pwd = "test123"
    hashed = get_password_hash(pwd)
    assert hashed != pwd
    assert verify_password(pwd, hashed)
    assert not verify_password("wrong", hashed)


def test_jwt_create_decode():
    payload = {"sub": "1", "email": "test@test.com"}
    token = create_access_token(data=payload)
    decoded = decode_token(token)
    assert decoded is not None
    assert decoded["sub"] == "1"
    assert decoded["email"] == "test@test.com"
    assert "exp" in decoded
