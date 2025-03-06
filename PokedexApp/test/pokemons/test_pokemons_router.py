import pytest
from ..mocks.mocks import mocked_create_pokemon_request_json, get_mocked_pokemons, get_first_mocked_pokemon, get_delete_pokemon_response, get_delete_all_pokemons_response

@pytest.mark.asyncio
async def test_get_pokemons(test_client, fake_pokemons_service):
    fake_pokemons_service.get_pokemons.return_value = get_mocked_pokemons()
    response = test_client.get("/pokemons")
    assert response.status_code == 200
    assert response.json() == get_mocked_pokemons()
    assert fake_pokemons_service.get_pokemons.call_count == 1

@pytest.mark.asyncio
async def test_get_pokemon_by_id(test_client, fake_pokemons_service):
    fake_pokemons_service.get_pokemon.return_value = get_first_mocked_pokemon()
    response = test_client.get("/pokemons/1")
    assert response.status_code == 200
    assert response.json() == get_first_mocked_pokemon()
    assert fake_pokemons_service.get_pokemon.call_count == 1

@pytest.mark.asyncio
async def test_create_pokemon(test_client, fake_pokemons_service):
    fake_pokemons_service.create_pokemon.return_value = get_first_mocked_pokemon()
    response = test_client.post("/pokemons", json=mocked_create_pokemon_request_json)
    assert response.status_code == 201
    assert response.json() == get_first_mocked_pokemon()
    assert fake_pokemons_service.create_pokemon.call_count == 1

@pytest.mark.asyncio
async def test_update_pokemon(test_client, fake_pokemons_service):
    fake_pokemons_service.update_pokemon.return_value = get_first_mocked_pokemon()
    response = test_client.put("/pokemons/1", json=mocked_create_pokemon_request_json)
    assert response.status_code == 200
    assert response.json() == get_first_mocked_pokemon()
    assert fake_pokemons_service.update_pokemon.call_count == 1

@pytest.mark.asyncio
async def test_delete_pokemon(test_client, fake_pokemons_service):
    fake_pokemons_service.delete_pokemon.return_value = get_delete_pokemon_response()
    response = test_client.delete("/pokemons/1")
    assert response.status_code == 204
    assert fake_pokemons_service.delete_pokemon.call_count == 1

@pytest.mark.asyncio
async def test_delete_all_pokemons(test_client, fake_pokemons_service):
    fake_pokemons_service.delete_all_pokemons.return_value = get_delete_all_pokemons_response()
    response = test_client.delete("/pokemons")
    assert response.status_code == 204
    assert fake_pokemons_service.delete_all_pokemons.call_count == 1