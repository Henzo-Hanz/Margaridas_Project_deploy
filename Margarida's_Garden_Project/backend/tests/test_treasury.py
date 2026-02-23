"""Testes de Treasury (despesas/receitas)."""
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


def test_treasury_analytics_unauthorized(client: TestClient):
    resp = client.get("/api/treasury/analytics/summary")
    assert resp.status_code == 403


def test_treasury_analytics_authorized(client: TestClient):
    token = _get_token(client)
    if not token:
        pytest.skip("Usuário não existe - rode init_db")
    resp = client.get(
        "/api/treasury/analytics/summary?period=6m",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "expenses_total" in data
    assert "incomes_total" in data
    assert "balance" in data
