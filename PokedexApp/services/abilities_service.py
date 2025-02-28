from typing import List
import uuid
from fastapi import HTTPException
from ..dtos.abilities_dtos import *
from motor.motor_asyncio import AsyncIOMotorDatabase


class AbilitiesService:


    async def get_ability_by_id(self, ability_id: str, db: AsyncIOMotorDatabase) -> AbilityResponseDTO:
        ability = await db.abilities.aggregate([{
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
        }]).to_list(length=1)
        return ability[0]
    
    async def get_all_abilities(self, db: AsyncIOMotorDatabase) -> List[AbilityResponseDTO]:
        abilities = await db.abilities.aggregate([{
            "$lookup": {
                "from": "types",
                "localField": "type",
                "foreignField": "_id",
                "as": "type"
            }
        },
        {
            "$unwind": "$type"
        }]).to_list(length=100)
        return abilities
    

    async def get_abilities(self, db: AsyncIOMotorDatabase) -> List[AbilityResponseDTO]:
        return await self.get_all_abilities(db)

    

    async def get_ability(self, ability_id: str, db: AsyncIOMotorDatabase) -> AbilityResponseDTO:
        return await self.get_ability_by_id(ability_id, db)



    async def create_ability(self, ability: AbilityRegisterDto, db: AsyncIOMotorDatabase) -> AbilityResponseDTO:
        abilityDoc = ability.model_dump()
        abilityDoc["_id"] = str(uuid.uuid4())
        result = await db.abilities.insert_one(abilityDoc)
        return await self.get_ability_by_id(result.inserted_id, db)


    async def update_ability(self, ability_id: str, ability: AbilityRegisterDto, db: AsyncIOMotorDatabase) -> AbilityResponseDTO:
        result = await db.abilities.update_one({"_id": ability_id}, {"$set": ability.model_dump()})

        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Ability not found")
        
        return await self.get_ability_by_id(ability_id, db)
    
    async def delete_ability(self, ability_id: str, db: AsyncIOMotorDatabase) -> None:
        result = await db.abilities.delete_one({"_id": ability_id})

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Ability not found")

