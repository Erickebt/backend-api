from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)

db = client["negocio"]
clientes = db["clientes"]

@app.get("/")
def home():
    return {"mensaje": "API funcionando"}

@app.get("/clientes")
def obtener_clientes():
    data = []

    for cliente in clientes.find():
        cliente["_id"] = str(cliente["_id"])
        data.append(cliente)

    return data

@app.post("/clientes")
def crear_cliente():
    nuevo = {
        "nombre": "Juan",
        "telefono": "099999999"
    }

    clientes.insert_one(nuevo)

    return {"mensaje": "Cliente creado"}