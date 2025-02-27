from bson import ObjectId
from ..config.database import get_database
from ..models.models import Ability
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from pydantic.fields import Field
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

class AbilityRequest(BaseModel):
    name: str
    description: str
    power: int
    accuracy: int
    type: str
    category: str
    pp: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Fire Punch",
                    "description": "A fire punch that deals damage and has a chance to burn the opponent.",
                    "power": 75,
                    "accuracy": 100,
                    "type": "Fire",
                    "category": "Physical",
                    "pp": 15
                }
            ]
        }
    }

@router.get("", response_model=list[Ability])
async def get_abilities(db: AsyncIOMotorDatabase = Depends(get_database)):
    abilities = await db.abilities.find({}).to_list(length=100)
    return abilities

@router.post("", status_code=200, response_model=Ability)
async def create_ability(ability: AbilityRequest, db: AsyncIOMotorDatabase = Depends(get_database)):
    result = await db.abilities.insert_one(ability.model_dump())
    print(result)
    return await db.abilities.find_one({"_id": result.inserted_id})

@router.get("/{ability_id}", response_model=Ability)
async def get_ability(ability_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    ability = await db.abilities.find_one({"_id": ObjectId(ability_id)})
    return ability

@router.put("/{ability_id}", response_model=Ability)
async def update_ability(ability_id: str, ability: AbilityRequest, db: AsyncIOMotorDatabase = Depends(get_database)):
    result = await db.abilities.update_one({"_id": ObjectId(ability_id)}, {"$set": ability.model_dump()})
    print(result)
    return await db.abilities.find_one({"_id": ObjectId(ability_id)})

@router.delete("/{ability_id}", status_code=204)
async def delete_ability(ability_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    result = await db.abilities.delete_one({"_id": ObjectId(ability_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Ability not found")
