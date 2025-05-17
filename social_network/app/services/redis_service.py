# app/services/redis_service.py

from app.database import redis_client

class RedisService:

    @staticmethod
    def increment_view_count(username: str):
        """Incrementa el contador de vistas para un usuario"""
        redis_client.incr(f"profile_views:{username}")

    @staticmethod
    def get_view_count(username: str) -> int:
        """Obtiene el contador de vistas para un usuario"""
        return int(redis_client.get(f"profile_views:{username}") or 0)

    @staticmethod
    def like_post(post_id: str):
        """Incrementa el contador de likes para una publicación"""
        redis_client.incr(f"post_likes:{post_id}")

    @staticmethod
    def get_likes(post_id: str) -> int:
        """Obtiene el contador de likes para una publicación"""
        return int(redis_client.get(f"post_likes:{post_id}") or 0)

    @staticmethod
    def add_active_user(username: str):
        """Agrega un usuario a la lista de conectados"""
        redis_client.sadd("active_users", username)

    @staticmethod
    def remove_active_user(username: str):
        """Elimina un usuario de la lista de conectados"""
        redis_client.srem("active_users", username)

    @staticmethod
    def get_active_users() -> list:
        """Obtiene la lista de usuarios conectados"""
        return list(redis_client.smembers("active_users"))
