from bson import ObjectId
from ..config.database import get_database
from ..models.models import Pokemon, Type
from fastapi import APIRouter, Body, Depends, HTTPException, Path
from pydantic import BaseModel
from pydantic.fields import Field
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

class TypeRequest(BaseModel):
    name: str

@router.get("", response_model=list[Type])
async def get_types(db: AsyncIOMotorDatabase = Depends(get_database)):
    types = await db.types.find({}).to_list(length=100)
    return types

@router.post("", status_code=201)
async def create_type(type: TypeRequest, db: AsyncIOMotorDatabase = Depends(get_database)):
    result = await db.types.insert_one(type.model_dump())

@router.get("/{type_id}", response_model=Type)
async def get_type(type_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    type = await db.types.find_one({"_id": ObjectId(type_id)})
    if not type:
        raise HTTPException(status_code=404, detail="Type not found")
    return type

@router.put("/{type_id}", response_model=Type)
async def update_type(type_id: str, type: TypeRequest, db: AsyncIOMotorDatabase = Depends(get_database)):
    result = await db.types.update_one({"_id": ObjectId(type_id)}, {"$set": type.model_dump()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Type not found")
    return result.upserted_id

@router.delete("/{type_id}", status_code=204)
async def delete_type(type_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    result = await db.types.delete_one({"_id": ObjectId(type_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Type not found")
