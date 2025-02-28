from typing import List
from ..models.models import Pokemon
from fastapi import APIRouter, HTTPException
from ..services.pokemons_service import PokemonsService
from fastapi import Depends
from ..config.database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase
from ..dtos.pokemons_dtos import *

router = APIRouter()

pokemons_service = PokemonsService()

@router.get("", response_model=List[PokemonResponseDTO])
async def get_pokemons(db: AsyncIOMotorDatabase = Depends(get_database)):
    pokemons = await pokemons_service.get_pokemons(db)
    print(pokemons)
    return pokemons 

@router.get("/{pokemon_id}", response_model=PokemonResponseDTO)
async def get_pokemon(pokemon_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    pokemon = await pokemons_service.get_pokemon(pokemon_id, db)
    return pokemon

@router.post("", status_code=201, response_model=PokemonResponseDTO)
async def create_pokemon(pokemon: PokemonRegisterDto, db: AsyncIOMotorDatabase = Depends(get_database)):
    pokemon = await pokemons_service.create_pokemon(pokemon, db)
    return pokemon

@router.put("/{pokemon_id}", response_model=PokemonResponseDTO)
async def update_pokemon(pokemon_id: str, pokemon: PokemonRegisterDto, db: AsyncIOMotorDatabase = Depends(get_database)):
    pokemon = await pokemons_service.update_pokemon(pokemon_id, pokemon, db)
    return pokemon

@router.delete("/{pokemon_id}", status_code=204)
async def delete_pokemon(pokemon_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    await pokemons_service.delete_pokemon(pokemon_id, db)










