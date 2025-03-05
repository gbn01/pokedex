import pytest
from ..mocks.mocks import mocked_create_ability_request, get_mocked_abilities, get_first_mocked_ability
from ...main import app
from ...services.abilities_service import AbilitiesService

ability_service = AbilitiesService()

@pytest.mark.asyncio
async def test_get_abilities(test_client, fake_db):
    fake_db.abilities.find.return_value = get_mocked_abilities()
    abilities = await ability_service.get_abilities(fake_db)
    assert abilities == get_mocked_abilities()
    assert ability_service.get_abilities.call_count == 1

@pytest.mark.asyncio
async def test_get_ability_by_id(test_client, fake_db):
    fake_db.abilities.find_one.return_value = get_first_mocked_ability()
    ability = await ability_service.get_ability_by_id(1, fake_db)
    assert ability == get_first_mocked_ability()
    assert ability_service.get_ability_by_id.call_count == 1

@pytest.mark.asyncio
async def test_create_ability(test_client, fake_db):
    fake_db.abilities.insert_one.return_value = get_first_mocked_ability()
    ability = await ability_service.create_ability(mocked_create_ability_request, fake_db)
    assert ability == get_first_mocked_ability()
    assert ability_service.create_ability.call_count == 1

@pytest.mark.asyncio
async def test_update_ability(test_client, fake_db):
    fake_db.abilities.update_one.return_value = get_first_mocked_ability()
    ability = await ability_service.update_ability(1, mocked_create_ability_request, fake_db)
    assert ability == get_first_mocked_ability()
    assert ability_service.update_ability.call_count == 1

@pytest.mark.asyncio
async def test_delete_ability(test_client, fake_db):
    fake_db.abilities.delete_one.return_value = get_first_mocked_ability()
    await ability_service.delete_ability(1, fake_db)
    assert ability_service.delete_ability.call_count == 1