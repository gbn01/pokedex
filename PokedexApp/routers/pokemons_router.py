from ..config.database import get_database
from ..models.models import Pokemon, Type
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from pydantic.fields import Field
from motor.motor_asyncio import AsyncIOMotorDatabase
from bson import json_util
from fastapi.encoders import jsonable_encoder
router = APIRouter()

class TypeRequest(BaseModel):
    name: str

@router.get("/types", response_model=list[Type])
async def get_types(db: AsyncIOMotorDatabase = Depends(get_database)):
    types = await db.types.find({}).to_list(length=100)
    return types

@router.post("/types", status_code=201)
async def create_type(type: TypeRequest, db: AsyncIOMotorDatabase = Depends(get_database)):
    result = await db.types.insert_one(type.model_dump())

