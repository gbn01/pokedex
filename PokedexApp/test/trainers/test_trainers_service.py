from ..mocks.mocks import get_first_mocked_trainer, get_mocked_trainers, get_update_trainer_request, get_delete_trainer_response
from ...services.trainers_service import TrainersService
import pytest
from unittest.mock import patch
from pymongo.results import DeleteResult
trainer_service = TrainersService()

@pytest.mark.asyncio
@patch('PokedexApp.services.trainers_service.TrainersService.get_trainer_by_id', return_value=get_first_mocked_trainer())
async def test_get_trainer_by_id(mock_get_trainer_by_id, fake_db):
    trainer = await trainer_service.get_trainer_by_id("1", fake_db)
    assert trainer == get_first_mocked_trainer()

@pytest.mark.asyncio
@patch('PokedexApp.services.trainers_service.TrainersService.get_all_trainers', return_value=get_mocked_trainers())
async def test_get_all_trainers(mock_get_all_trainers, fake_db):
    trainers = await trainer_service.get_all_trainers(fake_db)
    assert trainers == get_mocked_trainers()

@pytest.mark.asyncio
@patch('PokedexApp.services.trainers_service.TrainersService.get_trainers', return_value=get_mocked_trainers())
async def test_get_trainers(mock_get_trainers, fake_db):
    trainers = await trainer_service.get_trainers(fake_db)
    assert trainers == get_mocked_trainers()

@pytest.mark.asyncio
@patch('PokedexApp.services.trainers_service.TrainersService.get_trainer', return_value=get_first_mocked_trainer())
async def test_get_trainer(mock_get_trainer, fake_db):
    trainer = await trainer_service.get_trainer("1", fake_db)
    assert trainer == get_first_mocked_trainer()

@pytest.mark.asyncio
@patch('PokedexApp.services.trainers_service.TrainersService.get_trainer_by_id', return_value=get_first_mocked_trainer())
async def test_update_trainer(mock_get_trainer_by_id, fake_db):
    trainer = await trainer_service.update_trainer("1", get_update_trainer_request(), fake_db)
    assert trainer == get_first_mocked_trainer()
    
@pytest.mark.asyncio
async def test_delete_trainer(fake_db):
    fake_db.pokemons.delete_one.return_value = DeleteResult(raw_result={"n": 1, "ok": 1}, acknowledged=True)
    await trainer_service.delete_trainer("1", fake_db)
