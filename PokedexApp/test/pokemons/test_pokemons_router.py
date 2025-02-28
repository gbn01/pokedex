from fastapi.testclient import TestClient
import pytest
from ..mocks.mocks import mocked_pokemons, mocked_create_pokemon_request
from ...main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_get_pokemons(client, fake_pokemons_service):
    fake_pokemons_service.get_pokemons.return_value = mocked_pokemons
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert response.json() == mocked_pokemons
    assert fake_pokemons_service.get_pokemons.call_count == 1

def test_get_pokemon_by_id(client, fake_pokemons_service):
    fake_pokemons_service.get_pokemon.return_value = mocked_pokemons[0]
    response = client.get("/pokemons/1")
    assert response.status_code == 200
    assert response.json() == mocked_pokemons[0]
    assert fake_pokemons_service.get_pokemon_by_id.call_count == 1

def test_create_pokemon(client, fake_pokemons_service):
    fake_pokemons_service.create_pokemon.return_value = mocked_pokemons[0]
    response = client.post("/pokemons", json=mocked_create_pokemon_request)
    assert response.status_code == 201
    assert response.json() == mocked_pokemons[0]
    assert fake_pokemons_service.create_pokemon.call_count == 1

def test_update_pokemon(client, fake_pokemons_service):
    fake_pokemons_service.update_pokemon.return_value = mocked_pokemons[0]
    response = client.put("/pokemons/1", json=mocked_create_pokemon_request)
    assert response.status_code == 200
    assert response.json() == mocked_pokemons[0]
    assert fake_pokemons_service.update_pokemon.call_count == 1

def test_delete_pokemon(client, fake_pokemons_service):
    fake_pokemons_service.delete_pokemon.return_value = None
    response = client.delete("/pokemons/1")
    assert response.status_code == 204
    assert fake_pokemons_service.delete_pokemon.call_count == 1

