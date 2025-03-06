from unittest.mock import patch
import pytest
from ..mocks.mocks import mocked_create_pokemon_request, get_mocked_pokemons, get_first_mocked_pokemon
from ...services.pokemons_service import PokemonsService
from pymongo.results import DeleteResult
pokemon_service = PokemonsService()

@pytest.mark.asyncio
@patch('PokedexApp.services.pokemons_service.PokemonsService.get_pokemons', return_value=get_mocked_pokemons())
async def test_get_pokemons(mock_get_pokemons, fake_db):
    pokemons = await pokemon_service.get_pokemons(fake_db)
    assert pokemons == get_mocked_pokemons()


@pytest.mark.asyncio
@patch('PokedexApp.services.pokemons_service.PokemonsService.get_pokemon_by_id', return_value=get_first_mocked_pokemon())
async def test_get_pokemon_by_id(mock_get_pokemon_by_id, fake_db):
    pokemon = await pokemon_service.get_pokemon_by_id(1, fake_db)
    assert pokemon == get_first_mocked_pokemon()

@pytest.mark.asyncio
@patch('PokedexApp.services.pokemons_service.PokemonsService.get_pokemon_by_id', return_value=get_first_mocked_pokemon())
async def test_create_pokemon(mock_get_pokemon_by_id, fake_db):
    pokemon = await pokemon_service.create_pokemon(mocked_create_pokemon_request, fake_db)
    assert pokemon == get_first_mocked_pokemon()

@pytest.mark.asyncio
@patch('PokedexApp.services.pokemons_service.PokemonsService.get_pokemon_by_id', return_value=get_first_mocked_pokemon())
async def test_update_pokemon(mock_get_pokemon_by_id, fake_db):
    pokemon = await pokemon_service.update_pokemon(1, mocked_create_pokemon_request, fake_db)
    assert pokemon == get_first_mocked_pokemon()

@pytest.mark.asyncio
@patch('PokedexApp.services.pokemons_service.PokemonsService.get_pokemon_by_id', return_value=get_first_mocked_pokemon())
async def test_delete_pokemon(mock_get_pokemon_by_id, fake_db):
    fake_db.pokemons.delete_one.return_value = DeleteResult(raw_result={"n": 1, "ok": 1}, acknowledged=True)
    await pokemon_service.delete_pokemon(1, fake_db)