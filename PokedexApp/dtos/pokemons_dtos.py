from pydantic import BaseModel, Field

from .abilities_dtos import AbilityResponseDTO
from .types_dtos import TypeResponseDTO

from ..models.models import Ability, Pokemon, Type


class PokemonRegisterDto(BaseModel):
    name: str = Field(..., description="The name of the pokemon", max_length=20, min_length=3)
    type: str = Field(..., description="The type of the pokemon")
    abilities: list[str] = Field(..., description="The abilities of the pokemon")
    weaknesses: list[str] = Field(..., description="The weaknesses of the pokemon")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"name": "Pikachu", "type": "7c04fcae-1534-4b0f-b118-80b84cf43db5", "abilities": ["9b91be12-6f6d-4817-ac5a-82c5408ee9bd"], "weaknesses": ["9d66e360-bde1-4d65-aea8-96cb8ade9d22"]}
            ]
        }
    }

class PokemonResponseDTO(Pokemon):
    id: str = Field(..., description="The id of the pokemon", alias="_id", name="id")
    name: str = Field(..., description="The name of the pokemon")
    type: TypeResponseDTO = Field(..., description="The type of the pokemon")
    abilities: list[AbilityResponseDTO] = Field(..., description="The abilities of the pokemon")
    weaknesses: list[TypeResponseDTO] = Field(..., description="The weaknesses of the pokemon")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"id": "1", "name": "Pikachu", "type": "Electric", "abilities": [{"id": "2", "name": "Static"}], "weaknesses": [{"id": "3", "name": "Ground"}]}
            ]
        },
        "populate_by_name": True,
    }


class AddToTrainerDto(BaseModel):
    name: str = Field(..., description="The name of the pokemon")
    type: str = Field(..., description="The type of the pokemon")
    abilities: list[str] = Field(..., description="The abilities of the pokemon")
    weaknesses: list[str] = Field(..., description="The weaknesses of the pokemon")