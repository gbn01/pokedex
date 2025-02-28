from typing import List
import uuid
from fastapi import Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase

from ..dtos.pokemons_dtos import PokemonRegisterDto, PokemonResponseDTO

from ..models.models import Pokemon
from ..config.database import get_database


class PokemonsService:

    async def get_pokemon_by_id(self, pokemon_id: str, db: AsyncIOMotorDatabase) -> PokemonResponseDTO:
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
    
    async def get_all_pokemons(self, db: AsyncIOMotorDatabase) -> List[PokemonResponseDTO]:
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
        return pokemons

    async def get_pokemons(self, db: AsyncIOMotorDatabase) -> List[PokemonResponseDTO]:
        return await self.get_all_pokemons(db)


    async def get_pokemon(self, pokemon_id: str, db: AsyncIOMotorDatabase) -> PokemonResponseDTO:
        return await self.get_pokemon_by_id(pokemon_id, db)


    async def create_pokemon(self, pokemon: PokemonRegisterDto, db: AsyncIOMotorDatabase) -> PokemonResponseDTO:
        pokemonDoc = pokemon.model_dump()
        pokemonDoc["_id"] = str(uuid.uuid4())
        result = await db.pokemons.insert_one(pokemonDoc)
        
        return await self.get_pokemon_by_id(result.inserted_id, db)


    async def update_pokemon(self, pokemon_id: str, pokemon: PokemonRegisterDto, db: AsyncIOMotorDatabase) -> PokemonResponseDTO:
        result = await db.pokemons.update_one({"_id": pokemon_id}, {"$set": pokemon})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        
        return await self.get_pokemon_by_id(pokemon_id, db)


    async def delete_pokemon(self, pokemon_id: str, db: AsyncIOMotorDatabase) -> None:
        result = await db.pokemons.delete_one({"_id": pokemon_id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Pokemon not found")








