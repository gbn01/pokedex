from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..dtos.auth_dtos import RegisterDTO, TokenDTO
from ..dtos.trainers_dtos import TrainerResponseDTO
from ..auth.auth_service import AuthService, oauth2_bearer
from typing import Annotated
from ..config.database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

service_dependency = Annotated[AuthService, Depends(AuthService)]
db_dependency = Annotated[AsyncIOMotorDatabase, Depends(get_database)]


@router.post("/register", response_model=TrainerResponseDTO)
async def register(register: RegisterDTO, service: service_dependency, db: db_dependency):
    return await service.register(register, db)

@router.post("/login", response_model=TokenDTO)
async def login(login: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_bearer)], service: service_dependency, db: db_dependency):
    return await service.login(login, db)

@router.get("/me", response_model=TrainerResponseDTO)
async def me(service: service_dependency, db: db_dependency):
    return await service.get_current_user(db)