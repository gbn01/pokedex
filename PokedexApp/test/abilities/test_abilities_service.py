from unittest.mock import patch
import pytest
from ..mocks.mocks import mocked_create_ability_request, get_mocked_abilities, get_first_mocked_ability
from ...services.abilities_service import AbilitiesService
from pymongo.results import DeleteResult
ability_service = AbilitiesService()

@pytest.mark.asyncio
@patch('PokedexApp.services.abilities_service.AbilitiesService.get_abilities', return_value=get_mocked_abilities())
async def test_get_abilities(mock_get_abilities, fake_db):
    abilities = await ability_service.get_abilities(fake_db)
    assert abilities == get_mocked_abilities()


@pytest.mark.asyncio
@patch('PokedexApp.services.abilities_service.AbilitiesService.get_ability_by_id', return_value=get_first_mocked_ability())
async def test_get_ability_by_id(mock_get_ability_by_id, fake_db):
    ability = await ability_service.get_ability_by_id(1, fake_db)
    assert ability == get_first_mocked_ability()

@pytest.mark.asyncio
@patch('PokedexApp.services.abilities_service.AbilitiesService.get_ability_by_id', return_value=get_first_mocked_ability())
async def test_create_ability(mock_get_ability_by_id, fake_db):
    ability = await ability_service.create_ability(mocked_create_ability_request, fake_db)
    assert ability == get_first_mocked_ability()

@pytest.mark.asyncio
@patch('PokedexApp.services.abilities_service.AbilitiesService.get_ability_by_id', return_value=get_first_mocked_ability())
async def test_update_ability(mock_get_ability_by_id, fake_db):
    ability = await ability_service.update_ability(1, mocked_create_ability_request, fake_db)
    assert ability == get_first_mocked_ability()

@pytest.mark.asyncio
@patch('PokedexApp.services.abilities_service.AbilitiesService.get_ability_by_id', return_value=get_first_mocked_ability())
async def test_delete_ability(mock_get_ability_by_id, fake_db):
    fake_db.abilities.delete_one.return_value = DeleteResult(raw_result={"n": 1, "ok": 1}, acknowledged=True)
    await ability_service.delete_ability(1, fake_db)