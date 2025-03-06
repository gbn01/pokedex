

from fastapi import HTTPException
from ..dtos.trainers_dtos import TrainerResponseDTO, TrainerUpdateDTO
from motor.motor_asyncio import AsyncIOMotorDatabase
from ..utils.pipelines import get_all_trainers_pipeline, get_trainer_by_id_pipeline, get_trainer_by_name_pipeline

class TrainersService:

    async def get_trainer_by_id(self, trainer_id: str, db: AsyncIOMotorDatabase) -> TrainerResponseDTO:
        trainer = await db.trainers.aggregate(get_trainer_by_id_pipeline(trainer_id)).to_list(1)
        return trainer[0]
    
    async def get_all_trainers(self, db: AsyncIOMotorDatabase) -> list[TrainerResponseDTO]:
        return await db.trainers.aggregate(get_all_trainers_pipeline).to_list(100)
    
    async def get_trainers(self, db: AsyncIOMotorDatabase) -> list[TrainerResponseDTO]:
        return await self.get_all_trainers(db)
    
    async def get_trainer(self, trainer_id: str, db: AsyncIOMotorDatabase) -> TrainerResponseDTO:
        return await self.get_trainer_by_id(trainer_id, db)
    
    async def update_trainer(self, trainer_id: str, trainer: TrainerUpdateDTO, db: AsyncIOMotorDatabase) -> TrainerResponseDTO:
        await db.trainers.update_one({"_id": trainer_id}, {"$set": trainer.model_dump()})
        return await self.get_trainer_by_id(trainer_id, db)
    
    async def delete_trainer(self, trainer_id: str, db: AsyncIOMotorDatabase) -> None:
        await db.trainers.delete_one({"_id": trainer_id})

