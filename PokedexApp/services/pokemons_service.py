from typing import List
import uuid
from fastapi import Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase

from ..dtos.pokemons_dtos import PokemonRegisterDto, PokemonResponseDTO

from ..models.models import Pokemon
from ..config.database import get_database


class PokemonsService:


    async def get_pokemons(db: AsyncIOMotorDatabase) -> List[PokemonResponseDTO]:
        pokemons = await db.pokemons.aggregate([{
            "$lookup": {
                "from": "abilities",
                "localField": "abilities",
                "foreignField": "_id",
                "as": "abilities"
            }
        }, {
            "$lookup": {
                "from": "types",
                "localField": "weaknesses",
                "foreignField": "_id",
                "as": "weaknesses"
            }
        }, {
            "$lookup": {
                "from": "types",
                "localField": "type",
                "foreignField": "_id",
                "as": "type"
            }
        }, {
            "$unwind": "$type"
        }]).to_list(100)
        print(pokemons)
        return pokemons


    async def get_pokemon(pokemon_id: str, db: AsyncIOMotorDatabase) -> PokemonResponseDTO:
        pokemon = await db.pokemons.aggregate([{
            "$match": {"_id": pokemon_id}
        }, {
            "$lookup": {
                "from": "abilities",
                "localField": "abilities",
                "foreignField": "_id",
                "as": "abilities"
            }
        }, {
            "$lookup": {
                "from": "types",
                "localField": "weaknesses",
                "foreignField": "_id",
                "as": "weaknesses"
            }
        }, {
            "$unwind": "$abilities"
        }, {
            "$unwind": "$weaknesses"
        }]).to_list(1)
        if len(pokemon) == 0:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return pokemon[0]


    async def create_pokemon(pokemon: PokemonRegisterDto, db: AsyncIOMotorDatabase) -> PokemonResponseDTO:
        pokemonDoc = pokemon.model_dump()
        pokemonDoc["_id"] = str(uuid.uuid4())
        result = await db.pokemons.insert_one(pokemonDoc)
        createdPokemon = await db.pokemons.aggregate([{
            "$match": {"_id": result.inserted_id}
        }, {
            "$lookup": {
                "from": "abilities",
                "localField": "abilities",
                "foreignField": "_id",
                "as": "abilities"
            }
        }, {
            "$lookup": {
                "from": "types",
                "localField": "weaknesses",
                "foreignField": "_id",
                "as": "weaknesses"
            }
        }, {
            "$unwind": "$abilities"
        }, {
            "$unwind": "$weaknesses"
        }]).to_list(1)
        if len(createdPokemon) == 0:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return createdPokemon[0]


    async def update_pokemon(pokemon_id: str, pokemon: PokemonRegisterDto, db: AsyncIOMotorDatabase) -> PokemonResponseDTO:
        result = await db.pokemons.update_one({"_id": pokemon_id}, {"$set": pokemon})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        updatedPokemon = await db.pokemons.aggregate([{
            "$match": {"_id": pokemon_id}
        }, {
            "$lookup": {
                "from": "abilities",
                "localField": "abilities",
                "foreignField": "_id",
                "as": "abilities"
            }
        }, {
            "$lookup": {
                "from": "types",
                "localField": "weaknesses",
                "foreignField": "_id",
                "as": "weaknesses"
            }
        }, {
            "$unwind": "$abilities"
        }, {
            "$unwind": "$weaknesses"
        }]).to_list(1)
        if len(updatedPokemon) == 0:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return updatedPokemon[0]


    async def delete_pokemon(pokemon_id: str, db: AsyncIOMotorDatabase) -> None:
        result = await db.pokemons.delete_one({"_id": pokemon_id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Pokemon not found")








