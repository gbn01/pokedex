from fastapi import FastAPI
from .routers.pokemons_router import router as pokemons_router
from fastapi.middleware.cors import CORSMiddleware
from .routers.types_router import router as types_router
app = FastAPI()


app.include_router(pokemons_router, prefix="/pokemons")
app.include_router(types_router, prefix="/types")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Bem-vindo à Pokedex!"}