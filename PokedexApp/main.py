from fastapi import FastAPI
from .routers.pokemons_router import router as pokemons_router
from fastapi.middleware.cors import CORSMiddleware
from .routers.types_router import router as types_router
from .routers.abilities_router import router as abilities_router
from .routers.trainers_router import router as trainers_router
from .auth.auth_router import router as auth_router

app = FastAPI()


app.include_router(pokemons_router, prefix="/pokemons", tags=["Pokemons"])
app.include_router(types_router, prefix="/types", tags=["Types"])
app.include_router(abilities_router, prefix="/abilities", tags=["Abilities"])
app.include_router(trainers_router, prefix="/trainers", tags=["Trainers"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à Pokedex API!"}