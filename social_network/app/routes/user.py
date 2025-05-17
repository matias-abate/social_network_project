# app/routes/user.py

from fastapi import APIRouter, HTTPException
from app.models import UserModel
from app.database import mongo_db
from typing import List

router = APIRouter()

# Crear un usuario
@router.post("/", response_model=UserModel)
async def create_user(user: UserModel):
    existing_user = await mongo_db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    await mongo_db.users.insert_one(user.dict())
    return user

# Obtener un usuario por username
@router.get("/{username}", response_model=UserModel)
async def get_user(username: str):
    user = await mongo_db.users.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# Listar todos los usuarios
@router.get("/", response_model=List[UserModel])
async def list_users():
    users = await mongo_db.users.find().to_list(100)
    return users
