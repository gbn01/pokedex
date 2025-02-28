from ..services.abilities_service import AbilitiesService
from ..dtos.abilities_dtos import *
from ..config.database import get_database
from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

abilities_service = AbilitiesService()

@router.get("", response_model=list[AbilityResponseDTO])
async def get_abilities(db: AsyncIOMotorDatabase = Depends(get_database)):
    abilities = await abilities_service.get_abilities(db)
    return abilities

@router.post("", status_code=200, response_model=AbilityResponseDTO)
async def create_ability(ability: AbilityRegisterDto, db: AsyncIOMotorDatabase = Depends(get_database)):
    ability = await abilities_service.create_ability(ability, db)
    return ability

@router.get("/{ability_id}", response_model=AbilityResponseDTO)
async def get_ability(ability_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    ability = await abilities_service.get_ability(ability_id, db)
    return ability

@router.put("/{ability_id}", response_model=AbilityResponseDTO)
async def update_ability(ability_id: str, ability: AbilityRegisterDto, db: AsyncIOMotorDatabase = Depends(get_database)):
    ability = await abilities_service.update_ability(ability_id, ability, db)
    return ability

@router.delete("/{ability_id}", status_code=204)
async def delete_ability(ability_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    await abilities_service.delete_ability(ability_id, db)
