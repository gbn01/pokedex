from unittest.mock import patch
import pytest
from ..mocks.mocks import mocked_create_type_request, get_mocked_types, get_first_mocked_type
from ...services.types_service import TypesService
from pymongo.results import DeleteResult
type_service = TypesService()

@pytest.mark.asyncio
@patch('PokedexApp.services.types_service.TypesService.get_types', return_value=get_mocked_types())
async def test_get_types(mock_get_types, fake_db):
    types = await type_service.get_types(fake_db)
    assert types == get_mocked_types()


@pytest.mark.asyncio
@patch('PokedexApp.services.types_service.TypesService.get_type_by_id', return_value=get_first_mocked_type())
async def test_get_type_by_id(mock_get_type_by_id, fake_db):
    type = await type_service.get_type_by_id(1, fake_db)
    assert type == get_first_mocked_type()

@pytest.mark.asyncio
@patch('PokedexApp.services.types_service.TypesService.get_type_by_id', return_value=get_first_mocked_type())
async def test_create_type(mock_get_type_by_id, fake_db):
    type = await type_service.create_type(mocked_create_type_request, fake_db)
    assert type == get_first_mocked_type()

@pytest.mark.asyncio
@patch('PokedexApp.services.types_service.TypesService.get_type_by_id', return_value=get_first_mocked_type())
async def test_update_type(mock_get_type_by_id, fake_db):
    type = await type_service.update_type(1, mocked_create_type_request, fake_db)
    assert type == get_first_mocked_type()

@pytest.mark.asyncio
@patch('PokedexApp.services.types_service.TypesService.get_type_by_id', return_value=get_first_mocked_type())
async def test_delete_type(mock_get_type_by_id, fake_db):
    fake_db.types.delete_one.return_value = DeleteResult(raw_result={"n": 1, "ok": 1}, acknowledged=True)
    await type_service.delete_type(1, fake_db)