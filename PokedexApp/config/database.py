from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client.pokedex

async def get_database():
    try:
        yield db
    finally:
        client.close()