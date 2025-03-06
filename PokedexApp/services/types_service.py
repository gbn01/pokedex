import uuid
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List
from ..dtos.types_dtos import *


class TypesService:

    async def get_types(self, db: AsyncIOMotorDatabase) -> List[TypeResponseDTO]:
        types = await db.types.find().to_list(length=100)
        return types
    
    async def get_type_by_id(self, type_id: str, db: AsyncIOMotorDatabase) -> TypeResponseDTO:
        type = await db.types.find_one({"_id": type_id})
        if not type:
            raise HTTPException(status_code=404, detail="Type not found")
        return type

    async def create_type(self, type: TypeRegisterDTO, db: AsyncIOMotorDatabase) -> TypeResponseDTO:
        typeDoc = type.model_dump()
        typeDoc["_id"] = str(uuid.uuid4())
        result = await db.types.insert_one(typeDoc)
        return await self.get_type_by_id(result.inserted_id, db)

    async def update_type(self, type_id: str, type: TypeRegisterDTO, db: AsyncIOMotorDatabase) -> TypeResponseDTO:
        result = await db.types.update_one({"_id": type_id}, {"$set": type.model_dump()})
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Type not found")
        return await self.get_type_by_id(type_id, db)
    
    async def delete_type(self, type_id: str, db: AsyncIOMotorDatabase) -> None:
        result = await db.types.delete_one({"_id": type_id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Type not found")

