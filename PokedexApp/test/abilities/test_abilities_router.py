import pytest
from ..mocks.mocks import mocked_abilities, mocked_create_ability_request, get_mocked_abilities, get_first_mocked_ability
from ...main import app

@pytest.mark.asyncio
async def test_get_abilities(test_client, fake_abilities_service):
    fake_abilities_service.get_abilities.return_value = get_mocked_abilities()
    response = test_client.get("/abilities")
    assert response.status_code == 200
    assert response.json() == mocked_abilities
    assert fake_abilities_service.get_abilities.call_count == 1

@pytest.mark.asyncio
async def test_get_ability_by_id(test_client, fake_abilities_service):
    fake_abilities_service.get_ability_by_id.return_value = get_first_mocked_ability()
    response = test_client.get("/abilities/1")
    assert response.status_code == 200
    assert response.json() == get_first_mocked_ability()
    assert fake_abilities_service.get_ability_by_id.call_count == 1 

@pytest.mark.asyncio
async def test_create_ability(test_client, fake_abilities_service):
    fake_abilities_service.create_ability.return_value = get_first_mocked_ability()
    response = test_client.post("/abilities", json=mocked_create_ability_request)
    assert response.status_code == 200
    assert response.json() == get_first_mocked_ability()
    assert fake_abilities_service.create_ability.call_count == 1

@pytest.mark.asyncio
async def test_update_ability(test_client, fake_abilities_service):
    fake_abilities_service.update_ability.return_value = get_first_mocked_ability()
    response = test_client.put("/abilities/1", json=mocked_create_ability_request)
    assert response.status_code == 200
    assert response.json() == get_first_mocked_ability()
    assert fake_abilities_service.update_ability.call_count == 1

@pytest.mark.asyncio
async def test_delete_ability(test_client, fake_abilities_service):
    fake_abilities_service.delete_ability.return_value = None
    response = test_client.delete("/abilities/1")
    assert response.status_code == 204
    assert fake_abilities_service.delete_ability.call_count == 1