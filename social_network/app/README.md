""# Proyecto de Red Social - Persistencia Políglota

Este proyecto es un backend para una red social, utilizando persistencia poliglota con:
- **MongoDB** para el almacenamiento de usuarios y publicaciones.
- **Neo4j** para modelar relaciones entre usuarios.
- **Redis** para manejar caché en tiempo real y métricas.

---

## 🚀 **Instalación**
### 🔹 **1️⃣ Clonar el repositorio**
```bash
git clone <URL-DEL-REPO>
cd social_network_project
```

---

### 🔹 **2️⃣ Crear un entorno virtual**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
.env\Scripts\activate   # Windows
```

---

### 🔹 **3️⃣ Instalar las dependencias**
```bash
pip install -r requirements.txt
```

---

### 🔹 **4️⃣ Configurar las bases de datos**
- **MongoDB:** Debe estar corriendo en `mongodb://localhost:27017`.
- **Neo4j:** Debe estar corriendo en `bolt://localhost:7687`.  
  Usuario: `neo4j`, Contraseña: `password`.
- **Redis:** Debe estar corriendo en `localhost:6379`.

---

### 🔹 **5️⃣ Levantar el servidor**
```bash
uvicorn app.main:app --reload
```

---

### 🔹 **6️⃣ Documentación interactiva**
Podés acceder a la documentación generada automáticamente en:
- [Swagger UI](http://127.0.0.1:8000/docs)
- [Redoc UI](http://127.0.0.1:8000/redoc)

---

## 📌 **Rutas Principales**
| Ruta                             | Método   | Descripción                           |
|----------------------------------|----------|--------------------------------------|
| `/users/`                        | `POST`   | Crear un usuario                     |
| `/users/`                        | `GET`    | Listar todos los usuarios            |
| `/users/{username}`              | `GET`    | Obtener un usuario por su username   |
| `/posts/`                        | `POST`   | Crear una publicación                |
| `/posts/`                        | `GET`    | Listar todas las publicaciones       |
| `/posts/{post_id}`               | `GET`    | Obtener una publicación por ID       |
| `/relationships/`                | `POST`   | Crear una relación entre usuarios    |
| `/relationships/{username}`      | `GET`    | Obtener todas las relaciones de un usuario |
| `/relationships/{user_from}/{user_to}` | `DELETE` | Eliminar una relación entre usuarios |
| `/cache/views/{username}`        | `POST`   | Incrementar vistas de perfil         |
| `/cache/views/{username}`        | `GET`    | Obtener vistas de perfil             |
| `/cache/likes/{post_id}`         | `POST`   | Dar like a una publicación           |
| `/cache/likes/{post_id}`         | `GET`    | Obtener cantidad de likes de un post |
| `/cache/active-users`            | `GET`    | Listar usuarios activos              |

---

## ✅ **Contribución**
1. Hacer un fork del repositorio.
2. Crear un branch para tu nueva funcionalidad:
    ```bash
    git checkout -b feature/nueva-funcionalidad
    ```
3. Hacer commit de los cambios:
    ```bash
    git commit -m "Agregada nueva funcionalidad"
    ```
4. Push al branch:
    ```bash
    git push origin feature/nueva-funcionalidad
    ```
5. Crear un Pull Request.

---

## ⚠️ **Notas Adicionales**
- Asegurate de que MongoDB, Neo4j y Redis estén corriendo antes de iniciar el servidor.
- Las credenciales de acceso para Neo4j deben ser actualizadas en `database.py` si cambian.
- Cualquier problema, revisar los logs de `uvicorn` para identificar errores.

---

¡Listo para correr y explorar esta red social distribuida! 🚀""
