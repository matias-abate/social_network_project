# services/user_service.py

from app.database import mongo_db

class UserService:

    @staticmethod
    async def create_user(user_data: dict):
        """ Crea un nuevo usuario en la base de datos """
        existing_user = await mongo_db.users.find_one({"email": user_data["email"]})
        if existing_user:
            return None
        await mongo_db.users.insert_one(user_data)
        return user_data

    @staticmethod
    async def get_user(username: str):
        """ Obtiene un usuario por su username """
        user = await mongo_db.users.find_one({"username": username})
        return user

    @staticmethod
    async def list_users(limit: int = 100):
        """ Lista todos los usuarios con un límite """
        users = await mongo_db.users.find().to_list(limit)
        return users
