

from pydantic import BaseModel, Field

from ..models.models import Ability, Type


class AbilityRegisterDto(BaseModel):
    name: str
    description: str
    power: int
    accuracy: int
    type: str
    category: str
    pp: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Fire Punch",
                    "description": "A fire punch that deals damage and has a chance to burn the opponent.",
                    "power": 75,
                    "accuracy": 100,
                    "type": "Fire",
                    "category": "Physical",
                    "pp": 15
                }
            ]
        },
    }


class AbilityResponseDTO(Ability):
    id: str = Field(..., description="The id of the ability", alias="_id")
    name: str = Field(..., description="The name of the ability")
    description: str = Field(..., description="The description of the ability")
    power: int = Field(..., description="The power of the ability")
    accuracy: int = Field(..., description="The accuracy of the ability")
    category: str = Field(..., description="The category of the ability")
    type: Type = Field(..., description="The type of the ability")
    pp: int = Field(..., description="The pp of the ability")
    

