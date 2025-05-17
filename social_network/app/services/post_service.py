# services/post_service.py

from app.database import mongo_db

class PostService:

    @staticmethod
    async def create_post(post_data: dict):
        """ Crea una nueva publicación en la base de datos """
        await mongo_db.posts.insert_one(post_data)

    @staticmethod
    async def get_post(post_id: str):
        """ Obtiene una publicación por su ID """
        post = await mongo_db.posts.find_one({"_id": post_id})
        return post

    @staticmethod
    async def list_posts(limit: int = 100):
        """ Lista todas las publicaciones con un límite """
        posts = await mongo_db.posts.find().to_list(limit)
        return posts
