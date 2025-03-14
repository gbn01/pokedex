from fastapi.testclient import TestClient

from ..auth.auth_service import AuthService
from ..services.trainers_service import TrainersService

from ..services.abilities_service import AbilitiesService
from ..services.pokemons_service import PokemonsService
from ..services.types_service import TypesService
from ..main import app
from ..config.database import get_database
from unittest.mock import AsyncMock
import pytest   

mock_db = AsyncMock()
mock_pokemons_service = AsyncMock()
mock_types_service = AsyncMock()
mock_abilities_service = AsyncMock()
mock_trainers_service = AsyncMock()
mock_auth_service = AsyncMock()
@pytest.fixture
def fake_pokemons_service():
    return mock_pokemons_service

@pytest.fixture
def fake_types_service():
    return mock_types_service

@pytest.fixture
def fake_abilities_service():
    return mock_abilities_service

@pytest.fixture
def fake_trainers_service():
    return mock_trainers_service

@pytest.fixture
def fake_auth_service():
    return mock_auth_service

@pytest.fixture
def fake_db():
    return mock_db

def get_mock_database():
    yield mock_db

def get_mock_pokemons_service():
    yield mock_pokemons_service

def get_mock_types_service():
    yield mock_types_service

def get_mock_abilities_service():
    yield mock_abilities_service

def get_mock_trainers_service():
    yield mock_trainers_service

def get_mock_auth_service():
    yield mock_auth_service

@pytest.fixture
def test_client():
    return TestClient(app)

app.dependency_overrides[get_database] = get_mock_database
app.dependency_overrides[PokemonsService] = get_mock_pokemons_service
app.dependency_overrides[TypesService] = get_mock_types_service
app.dependency_overrides[AbilitiesService] = get_mock_abilities_service
app.dependency_overrides[TrainersService] = get_mock_trainers_service
app.dependency_overrides[AuthService] = get_mock_auth_service