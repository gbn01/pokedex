import pytest

mocked_pokemons = [
    {
        "_id": "1",
        "name": "Pikachu",
        "type": {
            "_id": "1",
            "name": "Electric",
        },
        "abilities": [
            {
                "_id": "1",
                "name": "Static",
                "description": "This Pokemon cannot be paralyzed.",
                "power": 0,
                "accuracy": 100,
                "type": {
                    "_id": "1",
                    "name": "Electric",
                },
                "category": "Special",
                "pp": 20
            }
        ],
        "weaknesses": [
            {
                "_id": "2",
                "name": "Ground",
            }
        ],
    }
]

def get_mocked_pokemons():
    return mocked_pokemons

mocked_create_pokemon_request = {
    "name": "Pikachu",
    "type": "1",
    "abilities": ["1"],
    "weaknesses": ["2"]
}


mocked_abilities = [
    {
        "_id": "1",
        "name": "Static",
        "description": "This Pokemon cannot be paralyzed.",
        "power": 0,
        "accuracy": 100,
        "type": {
            "_id": "1",
            "name": "Electric",
        },
        "category": "Special",
        "pp": 20
    }
]

def get_mocked_abilities():
    return mocked_abilities

mocked_create_ability_request = {
    "name": "Static",
    "description": "This Pokemon cannot be paralyzed.",
    "power": 0,
    "accuracy": 100,
    "type": "1",
    "category": "Special",
    "pp": 20
}

mocked_types = [
    {
        "_id": "1",
        "name": "Electric",
    }
]

def get_mocked_types():
    return mocked_types

mocked_create_type_request = {
    "name": "Electric",
}

