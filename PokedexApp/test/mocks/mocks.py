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