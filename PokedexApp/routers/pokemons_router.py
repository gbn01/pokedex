from typing import Annotated
from fastapi import APIRouter
from ..services.pokemons_service import PokemonsService
from fastapi import Depends
from ..config.database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase
from ..dtos.pokemons_dtos import *

router = APIRouter()


service_dependency = Annotated[PokemonsService, Depends(PokemonsService)]
db_dependency = Annotated[AsyncIOMotorDatabase, Depends(get_database)]

@router.get("", response_model=list[PokemonResponseDTO])
async def get_pokemons(service: service_dependency, db: db_dependency):
    pokemons = await service.get_pokemons(db)
    return pokemons

@router.get("/{pokemon_id}", response_model=PokemonResponseDTO)
async def get_pokemon(pokemon_id: str, service: service_dependency, db: db_dependency):
    pokemon = await service.get_pokemon(pokemon_id, db)
    return pokemon

@router.post("", status_code=201, response_model=PokemonResponseDTO)
async def create_pokemon(pokemon: PokemonRegisterDto, service: service_dependency, db: db_dependency):
    pokemon = await service.create_pokemon(pokemon, db)
    return pokemon

@router.put("/{pokemon_id}", response_model=PokemonResponseDTO)
async def update_pokemon(pokemon_id: str, pokemon: PokemonRegisterDto, service: service_dependency, db: db_dependency):
    pokemon = await service.update_pokemon(pokemon_id, pokemon, db)
    return pokemon

@router.delete("/{pokemon_id}", status_code=204)
async def delete_pokemon(pokemon_id: str, service: service_dependency, db: db_dependency):
    await service.delete_pokemon(pokemon_id, db)

@router.delete("", status_code=204)
async def delete_all_pokemons(service: service_dependency, db: db_dependency):
    await service.delete_all_pokemons(db)









