
from pydantic import BaseModel


class RegisterDTO(BaseModel):
    name: str
    password: str

class TokenDTO(BaseModel):
    access_token: str
    token_type: str


    