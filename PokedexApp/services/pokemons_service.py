from typing import List
import uuid
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase

from ..dtos.pokemons_dtos import PokemonRegisterDto, PokemonResponseDTO
from ..utils.pipelines import get_all_pokemons_pipeline, get_pokemon_by_id_pipeline


class PokemonsService:

    async def get_pokemon_by_id(self, pokemon_id: str, db: AsyncIOMotorDatabase) -> PokemonResponseDTO:
        pokemon = await db.pokemons.aggregate(get_pokemon_by_id_pipeline(pokemon_id)).to_list(1)
        print(pokemon)
        if len(pokemon) == 0:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return pokemon[0]
    
    async def get_all_pokemons(self, db: AsyncIOMotorDatabase) -> List[PokemonResponseDTO]:
        pokemons = await db.pokemons.aggregate(get_all_pokemons_pipeline).to_list(100)
        return pokemons

    async def get_pokemons(self, db: AsyncIOMotorDatabase) -> List[PokemonResponseDTO]:
        return await self.get_all_pokemons(db)


    async def get_pokemon(self, pokemon_id: str, db: AsyncIOMotorDatabase) -> PokemonResponseDTO:
        return await self.get_pokemon_by_id(pokemon_id, db)


    async def create_pokemon(self, pokemon: PokemonRegisterDto, db: AsyncIOMotorDatabase) -> PokemonResponseDTO:
        pokemonDoc = pokemon.model_dump()
        pokemonDoc["_id"] = str(uuid.uuid4())
        result = await db.pokemons.insert_one(pokemonDoc)
        print(result)
        
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

    async def delete_all_pokemons(self, db: AsyncIOMotorDatabase) -> None:
        await db.pokemons.delete_many({})







