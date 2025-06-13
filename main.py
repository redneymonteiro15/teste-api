from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do .env localmente

app = FastAPI()

MONGO_DETAILS = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client.meubanco

@app.get("/")
async def root():
    count = await db.test.count_documents({})
    return {"message": f"FastAPI com MongoDB funcionando! {count} docs na coleção test."}
