from ..services.abilities_service import AbilitiesService
from ..dtos.abilities_dtos import *
from ..config.database import get_database
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import Annotated
from ..auth.auth import get_current_user
router = APIRouter()

service_dependency = Annotated[AbilitiesService, Depends(AbilitiesService)] 
db_dependency = Annotated[AsyncIOMotorDatabase, Depends(get_database)]
auth_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("", response_model=list[AbilityResponseDTO])
async def get_abilities(service: service_dependency, db: db_dependency, user: auth_dependency):
    abilities = await service.get_abilities(db)
    return abilities

@router.post("", status_code=200, response_model=AbilityResponseDTO)
async def create_ability(ability: AbilityRegisterDto, service: service_dependency, db: db_dependency, user: auth_dependency):
    ability = await service.create_ability(ability, db)
    return ability

# @router.get("/fill", status_code=200)
# async def fill_abilities(service: service_dependency, db: db_dependency, user: auth_dependency):
#     abilities = await service.fill_abilities(db)
#     return {"message": "Abilities filled"}

@router.get("/{ability_id}", response_model=AbilityResponseDTO)
async def get_ability(ability_id: str, service: service_dependency, db: db_dependency, user: auth_dependency):
    ability = await service.get_ability(ability_id, db)
    return ability

@router.get("/type/{type_name}", response_model=list[AbilityResponseDTO])
async def get_abilities_by_type(type_name: str, service: service_dependency, db: db_dependency, user: auth_dependency):
    abilities = await service.get_abilities_by_type(type_name, db)
    return abilities



@router.put("/{ability_id}", response_model=AbilityResponseDTO)
async def update_ability(ability_id: str, ability: AbilityRegisterDto, service: service_dependency, db: db_dependency, user: auth_dependency):
    ability = await service.update_ability(ability_id, ability, db)
    return ability

@router.delete("/{ability_id}", status_code=204)
async def delete_ability(ability_id: str, service: service_dependency, db: db_dependency, user: auth_dependency):
    await service.delete_ability(ability_id, db)
