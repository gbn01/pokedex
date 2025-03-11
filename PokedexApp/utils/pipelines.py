get_all_trainers_pipeline = [
    {
        "$lookup": {
            "from": "pokemons",
            "localField": "pokemons",
            "foreignField": "_id",
            "as": "pokemons"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "types",
            "localField": "pokemons.type",
            "foreignField": "_id",
            "as": "pokemons.type"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons.type",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "abilities",
            "localField": "pokemons.abilities",
            "foreignField": "_id",
            "as": "pokemons.abilities"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons.abilities",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "types",
            "localField": "pokemons.abilities.type",
            "foreignField": "_id",
            "as": "pokemons.abilities.type"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons.abilities.type",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "types",
            "localField": "pokemons.weaknesses",
            "foreignField": "_id",
            "as": "pokemons.weaknesses"
        }
    },
    {
        "$group": {
            "_id": {
                "trainer_id": "$_id",
                "pokemon_id": "$pokemons._id"
            },
            "trainer_name": {"$first": "$name"},
            "password": {"$first": "$password"},
            "pokemon_name": {"$first": "$pokemons.name"},
            "pokemon_type": {"$first": "$pokemons.type"},
            "pokemon_abilities": {"$addToSet": "$pokemons.abilities"},
            "pokemon_weaknesses": {"$first": "$pokemons.weaknesses"}
        }
    },
    {
        "$group": {
            "_id": "$_id.trainer_id",
            "name": {"$first": "$trainer_name"},
            "password": {"$first": "$password"},
            "pokemons": {
                "$addToSet": {
                    "_id": "$_id.pokemon_id",
                    "name": "$pokemon_name",
                    "type": "$pokemon_type",
                    "abilities": "$pokemon_abilities",
                    "weaknesses": "$pokemon_weaknesses"
                }
            }
        }
    }
]


def get_trainer_by_name_pipeline(trainer_name: str):

    return [
    {
        "$match": {"name": trainer_name}
    },  
    {
        "$lookup": {
            "from": "pokemons",
            "localField": "pokemons",
            "foreignField": "_id",
            "as": "pokemons"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "types",
            "localField": "pokemons.type",
            "foreignField": "_id",
            "as": "pokemons.type"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons.type",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "abilities",
            "localField": "pokemons.abilities",
            "foreignField": "_id",
            "as": "pokemons.abilities"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons.abilities",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "types",
            "localField": "pokemons.abilities.type",
            "foreignField": "_id",
            "as": "pokemons.abilities.type"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons.abilities.type",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "types",
            "localField": "pokemons.weaknesses",
            "foreignField": "_id",
            "as": "pokemons.weaknesses"
        }
    },
    {
        "$group": {
            "_id": {
                "trainer_id": "$_id",
                "pokemon_id": "$pokemons._id"
            },
            "trainer_name": {"$first": "$name"},
            "password": {"$first": "$password"},
            "pokemon_name": {"$first": "$pokemons.name"},
            "pokemon_type": {"$first": "$pokemons.type"},
            "pokemon_abilities": {"$addToSet": "$pokemons.abilities"},
            "pokemon_weaknesses": {"$first": "$pokemons.weaknesses"}
        }
    },
    {
        "$group": {
            "_id": "$_id.trainer_id",
            "name": {"$first": "$trainer_name"},
            "password": {"$first": "$password"},
            "pokemons": {
                "$addToSet": {
                    "_id": "$_id.pokemon_id",
                    "name": "$pokemon_name",
                    "type": "$pokemon_type",
                    "abilities": "$pokemon_abilities",
                    "weaknesses": "$pokemon_weaknesses"
                }
            }
        }
    }
    ]


def get_trainer_by_id_pipeline(trainer_id: str):

    return [
    {
        "$match": {"_id": trainer_id}
    },
    {
        "$lookup": {
            "from": "pokemons",
            "localField": "pokemons",
            "foreignField": "_id",
            "as": "pokemons"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "types",
            "localField": "pokemons.type",
            "foreignField": "_id",
            "as": "pokemons.type"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons.type",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "abilities",
            "localField": "pokemons.abilities",
            "foreignField": "_id",
            "as": "pokemons.abilities"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons.abilities",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "types",
            "localField": "pokemons.abilities.type",
            "foreignField": "_id",
            "as": "pokemons.abilities.type"
        }
    },
    {
        "$unwind": {
            "path": "$pokemons.abilities.type",
            "preserveNullAndEmptyArrays": True
        }
    },
    {
        "$lookup": {
            "from": "types",
            "localField": "pokemons.weaknesses",
            "foreignField": "_id",
            "as": "pokemons.weaknesses"
        }
    },
    {
        "$group": {
            "_id": {
                "trainer_id": "$_id",
                "pokemon_id": "$pokemons._id"
            },
            "trainer_name": {"$first": "$name"},
            "password": {"$first": "$password"},
            "pokemon_name": {"$first": "$pokemons.name"},
            "pokemon_type": {"$first": "$pokemons.type"},
            "pokemon_abilities": {"$addToSet": "$pokemons.abilities"},
            "pokemon_weaknesses": {"$first": "$pokemons.weaknesses"}
        }
    },
    {
        "$group": {
            "_id": "$_id.trainer_id",
            "name": {"$first": "$trainer_name"},
            "password": {"$first": "$password"},
            "pokemons": {
                "$addToSet": {
                    "_id": "$_id.pokemon_id",
                    "name": "$pokemon_name",
                    "type": "$pokemon_type",
                    "abilities": "$pokemon_abilities",
                    "weaknesses": "$pokemon_weaknesses"
                }
            }
        }
    }
]

def get_pokemons_by_trainer_id_pipeline(pokemons_ids: list[str]):
    print(pokemons_ids)
    return [
            {
                "$match": {
                    "_id": {"$in": pokemons_ids}
                }
            },
            {
                "$lookup": {
                    "from": "abilities",
                    "localField": "abilities",
                    "foreignField": "_id",
                    "as": "abilities"
                }
            },
            {
                "$unwind": "$abilities"
            },
            {
                "$lookup": {
                    "from": "types",
                    "localField": "abilities.type",
                    "foreignField": "_id",
                    "as": "abilities.type"
                }
            },
            {
                "$unwind": "$abilities.type"
            },
            {
                "$group": {
                    "_id": "$_id",
                    "name": {"$first": "$name"},
                    "type": {"$first": "$type"},
                    "weaknesses": {"$first": "$weaknesses"},
                    "abilities": {"$push": "$abilities"}
                }
            },
            {
                "$lookup": {
                    "from": "types",
                    "localField": "weaknesses",
                    "foreignField": "_id",
                    "as": "weaknesses"
                }
            },
            {
                "$lookup": {
                    "from": "types",
                    "localField": "type",
                    "foreignField": "_id",
                    "as": "type"
                }
            },
            {
                "$unwind": "$type"
            }
        ]

get_all_pokemons_pipeline = [
            {
                "$lookup": {
                    "from": "abilities",
                    "localField": "abilities",
                    "foreignField": "_id",
                    "as": "abilities"
                }
            },
            {
                "$unwind": "$abilities"
            },
            {
                "$lookup": {
                    "from": "types",
                    "localField": "abilities.type",
                    "foreignField": "_id",
                    "as": "abilities.type"
                }
            },
            {
                "$unwind": "$abilities.type"
            },
            {
                "$group": {
                    "_id": "$_id",
                    "name": {"$first": "$name"},
                    "type": {"$first": "$type"},
                    "weaknesses": {"$first": "$weaknesses"},
                    "abilities": {"$push": "$abilities"}
                }
            },
            {
                "$lookup": {
                    "from": "types",
                    "localField": "weaknesses",
                    "foreignField": "_id",
                    "as": "weaknesses"
                }
            },
            {
                "$lookup": {
                    "from": "types",
                    "localField": "type",
                    "foreignField": "_id",
                    "as": "type"
                }
            },
            {
                "$unwind": "$type"
            }
        ]

def get_pokemon_by_id_pipeline(pokemon_id: str):

    return [
            {
                "$match": {
                    "_id": pokemon_id
                }
            },
            {
                "$lookup": {
                    "from": "abilities",
                    "localField": "abilities",
                    "foreignField": "_id",
                    "as": "abilities"
                }
            },
            {
                "$unwind": "$abilities"
            },
            {
                "$lookup": {
                    "from": "types",
                    "localField": "abilities.type",
                    "foreignField": "_id",
                    "as": "abilities.type"
                }
            },
            {
                "$unwind": "$abilities.type"
            },
            {
                "$group": {
                    "_id": "$_id",
                    "name": {"$first": "$name"},
                    "type": {"$first": "$type"},
                    "weaknesses": {"$first": "$weaknesses"},
                    "abilities": {"$push": "$abilities"}
                }
            },
            {
                "$lookup": {
                    "from": "types",
                    "localField": "weaknesses",
                    "foreignField": "_id",
                    "as": "weaknesses"
                }
            },
            {
                "$lookup": {
                    "from": "types",
                    "localField": "type",
                    "foreignField": "_id",
                    "as": "type"
                }
            },
            {
                "$unwind": "$type"
            }
        ]

get_all_abilities_pipeline = [{
            "$lookup": {
                "from": "types",
                "localField": "type",
                "foreignField": "_id",
                "as": "type"
            }
        },
        {
            "$unwind": "$type"
        }]

def get_ability_by_id_pipeline(ability_id: str):

    return [
        {
            "$match": {"_id": ability_id}
        },
        {
            "$lookup": {
                "from": "types",
                "localField": "type",
                "foreignField": "_id",
                "as": "type"
            }
        },
        {
            "$unwind": "$type"
        }]


def get_abilities_by_type_pipeline(type_id: str):
    return [
        {
            "$match": {"type": type_id}
        },
        {
            "$lookup": {
                "from": "types",
                "localField": "type",
                "foreignField": "_id",
                "as": "type"
            }
        },
        {
            "$unwind": "$type"
        }]