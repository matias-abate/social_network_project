# app/main.py

from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_pass = os.getenv("NEO4J_PASSWORD")
redis_host = os.getenv("REDIS_HOST")
redis_port = int(os.getenv("REDIS_PORT"))

# Inicializar la app de FastAPI
app = FastAPI()

# Importar las rutas
from app.routes import user, post, relationship, cache

# Registrar rutas
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(post.router, prefix="/posts", tags=["Posts"])
app.include_router(relationship.router, prefix="/relationships", tags=["Relationships"])
app.include_router(cache.router, prefix="/cache", tags=["Cache"])

@app.get("/")
def read_root():
    return {"message": "¡Red Social Activa!"}
