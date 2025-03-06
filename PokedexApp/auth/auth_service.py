import datetime
import os
import uuid
import hashlib
from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..dtos.auth_dtos import RegisterDTO
from motor.motor_asyncio import AsyncIOMotorDatabase
from ..dtos.trainers_dtos import TrainerResponseDTO
from typing import Annotated
from jose import jwt, JWTError

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login")

class AuthService:

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=30)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
        return encoded_jwt

    async def register(self, register: RegisterDTO, db: AsyncIOMotorDatabase) -> TrainerResponseDTO:
        trainer = await db.trainers.find_one({"name": register.name})
        if trainer:
            raise HTTPException(status_code=400, detail="Trainer already exists")
        
        trainer = register.model_dump()
        trainer["_id"] = str(uuid.uuid4())
        trainer["pokemons"] = []
        trainer["password"] = hashlib.sha256(trainer["password"].encode()).hexdigest()
        await db.trainers.insert_one(trainer)
        return trainer

    async def login(self, login: OAuth2PasswordRequestForm, db: AsyncIOMotorDatabase) -> TrainerResponseDTO:
        trainer = await self.authenticate_user(login.username, login.password, db)
        if not trainer:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        print(trainer)
        
        access_token = self.create_access_token({"id": trainer["_id"], "username": trainer["name"]})

        return {"access_token": access_token, "token_type": "bearer"}
    
    async def get_current_user(self, token: Annotated[str, Depends(oauth2_bearer)]) -> TrainerResponseDTO:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
            id: str = payload.get("id")
            name: str = payload.get("username")
            if id is None or name is None:
                raise credentials_exception
            return {"id": id, "name": name}
        except JWTError:
            raise credentials_exception
            
                
    
    async def verify_password(self, password: str, hashed_password: str) -> bool:
        return hashlib.sha256(password.encode()).hexdigest() == hashed_password

    async def authenticate_user(self, name: str, password: str, db: AsyncIOMotorDatabase) -> TrainerResponseDTO:
        trainer = await db.trainers.find_one({"name": name})
        if not trainer:
            return False
        if not self.verify_password(password, trainer["password"]):
            return False
        return trainer
    
    