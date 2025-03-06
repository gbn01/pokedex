import pytest
from ..mocks.mocks import get_mocked_trainers, get_first_mocked_trainer, get_delete_trainer_response, get_update_trainer_request_json

@pytest.mark.asyncio
async def test_get_trainers(test_client, fake_trainers_service):
    fake_trainers_service.get_trainers.return_value = get_mocked_trainers()
    response = test_client.get("/trainers")
    assert response.status_code == 200
    assert response.json() == get_mocked_trainers()
    assert fake_trainers_service.get_trainers.call_count == 1

@pytest.mark.asyncio
async def test_get_trainer_by_id(test_client, fake_trainers_service):
    fake_trainers_service.get_trainer.return_value = get_first_mocked_trainer()
    response = test_client.get("/trainers/1")
    assert response.status_code == 200
    assert response.json() == get_first_mocked_trainer()
    assert fake_trainers_service.get_trainer.call_count == 1

@pytest.mark.asyncio
async def test_update_trainer(test_client, fake_trainers_service):
    fake_trainers_service.update_trainer.return_value = get_first_mocked_trainer()
    response = test_client.put("/trainers/1", json=get_update_trainer_request_json())
    assert response.status_code == 200
    assert response.json() == get_first_mocked_trainer()
    assert fake_trainers_service.update_trainer.call_count == 1

@pytest.mark.asyncio
async def test_delete_trainer(test_client, fake_trainers_service):
    fake_trainers_service.delete_trainer.return_value = get_delete_trainer_response()
    response = test_client.delete("/trainers/1")
    assert response.status_code == 204
    assert fake_trainers_service.delete_trainer.call_count == 1