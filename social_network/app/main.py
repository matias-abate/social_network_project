# app/main.py
from fastapi import FastAPI
from app.routes import user, post, relationship

app = FastAPI()

# Importar las rutas
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(post.router, prefix="/posts", tags=["Posts"])
app.include_router(relationship.router, prefix="/relationships", tags=["Relationships"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(post.router, prefix="/posts", tags=["Posts"])
app.include_router(relationship.router, prefix="/relationships", tags=["Relationships"])
app.include_router(cache.router, prefix="/cache", tags=["Cache"])

@app.get("/")
def read_root():
    return {"message": "¡Red Social Activa!"}
