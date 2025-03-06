from pydantic import BaseModel, Field
from .pokemons_dtos import PokemonResponseDTO

class TrainerUpdateDTO(BaseModel):
    name: str = Field(description="The name of the trainer")
    pokemons: list[str] = Field(description="The pokemons of the trainer")

class TrainerResponseDTO(BaseModel):
    id: str = Field(alias="_id")
    name: str = Field(description="The name of the trainer")
    pokemons: list[PokemonResponseDTO] = Field(description="The pokemons of the trainer")