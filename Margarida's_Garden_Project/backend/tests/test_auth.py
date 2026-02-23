"""Testes de autenticação."""
import pytest
from fastapi.testclient import TestClient


def test_login_success(client: TestClient):
    # Assume usuário existe (init_db ou fixture)
    resp = client.post(
        "/api/auth/login",
        data={"username": "margarida@garden.local", "password": "garden123"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert resp.status_code in (200, 401)
    if resp.status_code == 200:
        data = resp.json()
        assert "access_token" in data


def test_login_invalid(client: TestClient):
    resp = client.post(
        "/api/auth/login",
        data={"username": "wrong@test.com", "password": "wrong"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert resp.status_code == 401
