from fastapi.testclient import TestClient
from ..main import app
import pytest

def test_read_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo à Pokedex API!"}
