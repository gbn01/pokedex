from ...dtos.trainers_dtos import TrainerUpdateDTO
from ...dtos.abilities_dtos import AbilityRegisterDto
from ...dtos.types_dtos import TypeRegisterDTO
from ...dtos.pokemons_dtos import PokemonRegisterDto

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

def get_first_mocked_pokemon():
    return mocked_pokemons[0]

def get_delete_pokemon_response():
    return None

def get_delete_all_pokemons_response():
    return None

mocked_create_pokemon_request_json = {
    "name": "Pikachu",
    "type": "1",
    "abilities": ["1"],
    "weaknesses": ["2"]
}

mocked_create_pokemon_request = PokemonRegisterDto(
    name="Pikachu",
    type="1",
    abilities=["1"],
    weaknesses=["2"]
)


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

def get_first_mocked_ability():
    return mocked_abilities[0]

mocked_create_ability_request = AbilityRegisterDto(
    name="Static",
    description="This Pokemon cannot be paralyzed.",
    power=0,
    accuracy=100,
    type="1",
    category="Special",
    pp=20
)

mocked_create_ability_request_json = {
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

def get_first_mocked_type():
    return mocked_types[0]

mocked_create_type_request_json = {
    "name": "Electric",
}

mocked_create_type_request = TypeRegisterDTO(
    name="Electric",
)

mocked_trainers = [
    {
        "_id": "1",
        "name": "Ash Ketchum",
        "pokemons": [
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
    }
]

def get_mocked_trainers():
    return mocked_trainers

def get_first_mocked_trainer():
    return mocked_trainers[0]

def get_delete_trainer_response():
    return None

mocked_create_trainer_request_json = {
    "name": "Ash Ketchum",
    "password": "123456"
}

def get_update_trainer_request_json():
    return {
        "name": "Ash Ketchum",
        "pokemons": ["1"]
    }

def get_update_trainer_request():
    return TrainerUpdateDTO(
        name="Ash Ketchum",
        pokemons=["1"]
    )

