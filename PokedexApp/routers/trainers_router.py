from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.database import Database
from motor.motor_asyncio import AsyncIOMotorDatabase
from ..config.database import get_database
from ..services.trainers_service import TrainersService
from ..dtos.trainers_dtos import TrainerUpdateDTO, TrainerResponseDTO

router = APIRouter()

db_dependency = Annotated[AsyncIOMotorDatabase, Depends(get_database)]

service_dependency = Annotated[TrainersService, Depends(TrainersService)]


@router.get("", response_model=list[TrainerResponseDTO])
async def get_trainers(db: db_dependency, service: service_dependency):
    return await service.get_trainers(db)


@router.get("/{trainer_id}", response_model=TrainerResponseDTO)
async def get_trainer(trainer_id: str, db: db_dependency, service: service_dependency):
    return await service.get_trainer(trainer_id, db)

@router.put("/{trainer_id}", response_model=TrainerResponseDTO)
async def update_trainer(trainer_id: str, trainer: TrainerUpdateDTO, db: db_dependency, service: service_dependency):
    return await service.update_trainer(trainer_id, trainer, db)

@router.delete("/{trainer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_trainer(trainer_id: str, db: db_dependency, service: service_dependency):
    return await service.delete_trainer(trainer_id, db)