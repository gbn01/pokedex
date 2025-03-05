import uuid
from ..config.database import get_database
from ..models.models import Type
from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from ..dtos.types_dtos import *
from ..services.types_service import TypesService
from typing import Annotated
router = APIRouter()

service_dependency = Annotated[TypesService, Depends(TypesService)]
db_dependency = Annotated[AsyncIOMotorDatabase, Depends(get_database)]

@router.get("", response_model=list[TypeResponseDTO])
async def get_types(service: service_dependency, db: db_dependency):
    return await service.get_types(db)

@router.post("", status_code=200, response_model=TypeResponseDTO)
async def create_type(type: TypeRegisterDTO, service: service_dependency, db: db_dependency):
    return await service.create_type(type, db)

@router.get("/{type_id}", response_model=TypeResponseDTO)
async def get_type(type_id: str, service: service_dependency, db: db_dependency):
    return await service.get_type_by_id(type_id, db)

@router.put("/{type_id}", response_model=TypeResponseDTO)
async def update_type(type_id: str, type: TypeRegisterDTO, service: service_dependency, db: db_dependency):
    return await service.update_type(type_id, type, db)

@router.delete("/{type_id}", status_code=204)
async def delete_type(type_id: str, service: service_dependency, db: db_dependency):
    return await service.delete_type(type_id, db)
