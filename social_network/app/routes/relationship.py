# app/routes/relationship.py

from fastapi import APIRouter, HTTPException
from app.models import RelationshipModel
from app.services.relationship_service import RelationshipService
from typing import List

router = APIRouter()

# Crear una relación
@router.post("/", response_model=RelationshipModel)
async def create_relationship(relationship: RelationshipModel):
    RelationshipService.create_relationship(
        user_from=relationship.user_from,
        user_to=relationship.user_to,
        relationship_type=relationship.relationship_type
    )
    return relationship

# Obtener todas las relaciones de un usuario
@router.get("/{username}", response_model=List[RelationshipModel])
async def get_relationships(username: str):
    relationships = RelationshipService.get_relationships(username)
    if not relationships:
        raise HTTPException(status_code=404, detail="No se encontraron relaciones para este usuario")
    return relationships

# Eliminar una relación
@router.delete("/{user_from}/{user_to}")
async def delete_relationship(user_from: str, user_to: str):
    RelationshipService.delete_relationship(user_from, user_to)
    return {"message": f"Relación entre {user_from} y {user_to} eliminada correctamente"}
