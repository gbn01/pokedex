import pytest

mocked_pokemons = [
    {
        "id": "1",
        "name": "Pikachu",
        "type": {
            "id": "1",
            "name": "Electric",
        },
        "abilities": [
            {
                "id": "1",
                "name": "Static",
                "description": "This Pokemon cannot be paralyzed.",
                "power": 0,
                "accuracy": 100,
                "type": {
                    "id": "1",
                    "name": "Electric",
                },
                "category": "Special",
                "pp": 20
            }
        ],
        "weaknesses": [
            {
                "id": "2",
                "name": "Ground",
            }
        ],
    }
]

mocked_create_pokemon_request = {
    "name": "Pikachu",
    "type": "1",
    "abilities": ["1"],
    "weaknesses": ["2"]
}