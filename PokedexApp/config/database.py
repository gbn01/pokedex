from motor.motor_asyncio import AsyncIOMotorClient
import os

async def get_database():
    try:
        client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
        db = client.pokedex
        yield db
    finally:
        client.close()