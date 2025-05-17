# app/routes/cache.py

from fastapi import APIRouter
from app.services.redis_service import RedisService

router = APIRouter()

# Incrementar vistas de perfil
@router.post("/views/{username}")
async def increment_view(username: str):
    RedisService.increment_view_count(username)
    return {"message": f"Vista incrementada para {username}"}

# Obtener vistas de perfil
@router.get("/views/{username}")
async def get_view_count(username: str):
    count = RedisService.get_view_count(username)
    return {"username": username, "views": count}

# Dar like a un post
@router.post("/likes/{post_id}")
async def like_post(post_id: str):
    RedisService.like_post(post_id)
    return {"message": f"Like agregado al post {post_id}"}

# Obtener likes de un post
@router.get("/likes/{post_id}")
async def get_likes(post_id: str):
    count = RedisService.get_likes(post_id)
    return {"post_id": post_id, "likes": count}

# Obtener usuarios conectados
@router.get("/active-users")
async def get_active_users():
    users = RedisService.get_active_users()
    return {"active_users": users}
