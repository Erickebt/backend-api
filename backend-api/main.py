from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("MONGO_DATABASE")

client = MongoClient(MONGO_URL)
db = client[DATABASE_NAME]

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "API funcionando"
    }

@app.get("/clientes")
def clientes():
    return list(db.clientes.find({}, {"_id": 0}))