# app/models.py

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Modelo para Usuario
class UserModel(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    bio: Optional[str] = None
    followers: Optional[int] = 0
    following: Optional[int] = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Modelo para Publicación
class PostModel(BaseModel):
    user_id: str
    content: str
    media: Optional[List[str]] = []
    likes: Optional[int] = 0
    comments: Optional[List[dict]] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Modelo para Relaciones en Neo4j
class RelationshipModel(BaseModel):
    user_from: str
    user_to: str
    relationship_type: str   # Ej: "FRIEND", "FOLLOW", "BLOCK"
    created_at: datetime = Field(default_factory=datetime.utcnow)
