# app/routes/post.py

from fastapi import APIRouter, HTTPException
from app.models import PostModel
from app.database import mongo_db
from typing import List

router = APIRouter()

# Crear una publicación
@router.post("/", response_model=PostModel)
async def create_post(post: PostModel):
    await mongo_db.posts.insert_one(post.dict())
    return post

# Obtener una publicación por ID
@router.get("/{post_id}", response_model=PostModel)
async def get_post(post_id: str):
    post = await mongo_db.posts.find_one({"_id": post_id})
    if not post:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    return post

# Listar todas las publicaciones
@router.get("/", response_model=List[PostModel])
async def list_posts():
    posts = await mongo_db.posts.find().to_list(100)
    return posts
