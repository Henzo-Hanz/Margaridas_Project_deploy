"""Testes de credenciais (CRUD)."""
import pytest
from fastapi.testclient import TestClient


def _get_token(client: TestClient) -> str | None:
    resp = client.post(
        "/api/auth/login",
        data={"username": "margarida@garden.local", "password": "garden123"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    if resp.status_code != 200:
        return None
    return resp.json()["access_token"]


def test_list_credentials_unauthorized(client: TestClient):
    resp = client.get("/api/passwords")
    assert resp.status_code == 403


def test_list_credentials_authorized(client: TestClient):
    token = _get_token(client)
    if not token:
        pytest.skip("Usuário não existe - rode init_db")
    resp = client.get("/api/passwords", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
