import uuid
from ..config.database import get_database
from ..models.models import Type
from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from ..dtos.types_dtos import *
from ..services.types_service import TypesService
router = APIRouter()

types_service = TypesService()

@router.get("", response_model=list[TypeResponseDTO])
async def get_types(db: AsyncIOMotorDatabase = Depends(get_database)):
    return await types_service.get_types(db)

@router.post("", status_code=200, response_model=TypeResponseDTO)
async def create_type(type: TypeRegisterDTO, db: AsyncIOMotorDatabase = Depends(get_database)):
    return await types_service.create_type(type, db)

@router.get("/{type_id}", response_model=TypeResponseDTO)
async def get_type(type_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    return await types_service.get_type_by_id(type_id, db)

@router.put("/{type_id}", response_model=TypeResponseDTO)
async def update_type(type_id: str, type: TypeRegisterDTO, db: AsyncIOMotorDatabase = Depends(get_database)):
    return await types_service.update_type(type_id, type, db)

@router.delete("/{type_id}", status_code=204)
async def delete_type(type_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    return await types_service.delete_type(type_id, db)
