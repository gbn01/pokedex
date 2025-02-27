from typing import Optional
from pydantic import BaseModel
from pydantic.fields import Field
from bson import ObjectId

# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError("Invalid ObjectId")
#         return ObjectId(v)

#     @classmethod
#     def __modify_schema__(cls, field_schema):
#         field_schema.update(type="string")

class Pokemon(BaseModel):
    name: str
    type: str
    abilities: list[str]


class Type(BaseModel):
    id: Optional[str | ObjectId] = Field(alias="_id")
    name: str = Field(nullable=False, description="The name of the type")

    model_config = {
        "json_encoders": {ObjectId: str},
        "populate_by_name": True,
        "arbitrary_types_allowed": True
    }

class Ability(BaseModel):
    name: str
    description: str
    power: int
    accuracy: int
    category: str
    pp: int