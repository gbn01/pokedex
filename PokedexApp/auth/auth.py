import datetime
from http.client import HTTPException
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from ..dtos.auth_dtos import RegisterDTO, TokenDTO
from ..dtos.trainers_dtos import TrainerResponseDTO
from typing import Annotated
from ..config.database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase
from jose import jwt, JWTError
import os
import uuid
import hashlib
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

db_dependency = Annotated[AsyncIOMotorDatabase, Depends(get_database)]
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login")


@router.post("/register", response_model=TrainerResponseDTO)
async def register(register: RegisterDTO, db: db_dependency):
    return await register(register, db)

@router.post("/login", response_model=TokenDTO)
async def login(login: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    return await login_trainer(login, db)

@router.get("/me", response_model=TrainerResponseDTO)
async def me(token: Annotated[str, Depends(oauth2_bearer)], db: db_dependency):
    return await get_current_user(token, db)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt

async def register(register: RegisterDTO, db: AsyncIOMotorDatabase) -> TrainerResponseDTO:
    trainer = await db.trainers.find_one({"name": register.name})
    if trainer:
        raise HTTPException(status_code=400, detail="Trainer already exists")
        
    trainer = register.model_dump()
    trainer["_id"] = str(uuid.uuid4())
    trainer["pokemons"] = []
    trainer["password"] = hashlib.sha256(trainer["password"].encode()).hexdigest()
    await db.trainers.insert_one(trainer)
    return trainer

async def login_trainer(login: OAuth2PasswordRequestForm, db: AsyncIOMotorDatabase) -> TrainerResponseDTO:
    trainer = await authenticate_user(login.username, login.password, db)
    if not trainer:
        raise HTTPException(status_code=401, detail="Invalid credentials")
        
    print(trainer)
        
    access_token = create_access_token({"id": trainer["_id"], "username": trainer["name"]})

    return {"access_token": access_token, "token_type": "bearer"}
    
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]) -> TrainerResponseDTO:
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        id: str = payload.get("id")
        name: str = payload.get("username")
        if id is None or name is None:
            raise credentials_exception
        return {"id": id, "name": name}
    except JWTError:
        raise credentials_exception
            
                
    
async def verify_password(password: str, hashed_password: str) -> bool:
    return hashlib.sha256(password.encode()).hexdigest() == hashed_password

async def authenticate_user(name: str, password: str, db: AsyncIOMotorDatabase) -> TrainerResponseDTO:
    trainer = await db.trainers.find_one({"name": name})
    if not trainer:
        return False
    if not verify_password(password, trainer["password"]):
        return False
    return trainer
    