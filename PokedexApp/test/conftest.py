from fastapi.testclient import TestClient
from ..main import app
from ..config.database import get_database
from unittest.mock import Mock
import pytest

mock_db = Mock()
mock_pokemons_service = Mock()
mock_types_service = Mock()
mock_abilities_service = Mock()

def get_mock_database():
    yield mock_db

app.dependency_overrides[get_database] = get_mock_database

@pytest.fixture
def get_fake_database():
    yield mock_db

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
def client():
    return TestClient(app)