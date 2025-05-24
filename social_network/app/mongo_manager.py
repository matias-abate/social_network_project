from pymongo import MongoClient
import os

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(mongo_uri)
db = client["linkup_db"]

def get_users_collection():
    return db["users"]

def get_posts_collection():
    return db["posts"]