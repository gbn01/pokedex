import pytest
from ..mocks.mocks import mocked_types, mocked_create_type_request, get_mocked_types
from ...main import app

@pytest.mark.asyncio
async def test_get_types(test_client, fake_types_service):
    fake_types_service.get_types.return_value = get_mocked_types()
    response = test_client.get("/types")
    assert response.status_code == 200
    assert response.json() == mocked_types
    assert fake_types_service.get_types.call_count == 1

@pytest.mark.asyncio
async def test_get_type_by_id(test_client, fake_types_service):
    fake_types_service.get_type_by_id.return_value = mocked_types[0]
    response = test_client.get("/types/1")
    assert response.status_code == 200
    assert response.json() == mocked_types[0]
    assert fake_types_service.get_type_by_id.call_count == 1

@pytest.mark.asyncio
async def test_create_type(test_client, fake_types_service):
    fake_types_service.create_type.return_value = mocked_types[0]
    response = test_client.post("/types", json=mocked_create_type_request)
    assert response.status_code == 200
    assert response.json() == mocked_types[0]
    assert fake_types_service.create_type.call_count == 1

@pytest.mark.asyncio
async def test_update_type(test_client, fake_types_service):
    fake_types_service.update_type.return_value = mocked_types[0]
    response = test_client.put("/types/1", json=mocked_create_type_request)
    assert response.status_code == 200
    assert response.json() == mocked_types[0]
    assert fake_types_service.update_type.call_count == 1

@pytest.mark.asyncio
async def test_delete_type(test_client, fake_types_service):
    fake_types_service.delete_type.return_value = None
    response = test_client.delete("/types/1")
    assert response.status_code == 204
    assert fake_types_service.delete_type.call_count == 1