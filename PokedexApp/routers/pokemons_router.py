from ..config.database import get_database
from ..models.models import Pokemon, Ability, Type
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from pydantic.fields import Field
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()