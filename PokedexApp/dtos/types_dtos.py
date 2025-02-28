
from pydantic import BaseModel, Field


class TypeResponseDTO(BaseModel):
    id: str = Field(..., description="The id of the type", alias="_id")
    name: str = Field(..., description="The name of the type")


class TypeRegisterDTO(BaseModel):
    name: str = Field(..., description="The name of the type")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "Fire"},
            ]
        }
    }