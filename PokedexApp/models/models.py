from typing import Optional
from pydantic import BaseModel
from pydantic.fields import Field
from bson import ObjectId

class Pokemon(BaseModel):
    id: str = Field(alias="_id")
    name: str
    type: str
    abilities: list[str]
    weaknesses: list[str]

class Type(BaseModel):
    id: str = Field(alias="_id")
    name: str = Field(nullable=False, description="The name of the type")

class Ability(BaseModel):
    id: str = Field(alias="_id")
    name: str
    description: str
    power: int
    accuracy: int
    type: str
    category: str
    pp: int

class Trainer(BaseModel):
    id: str = Field(alias="_id")
    name: str
    password: str
    pokemons: list[str]
