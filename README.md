API de Tareas con FastAPI

Este proyecto es una API básica desarrollada con FastAPI, que permite gestionar tareas y usuarios utilizando los métodos HTTP (GET, POST, PUT, DELETE).

Características
Crear, listar, actualizar y eliminar tareas
Marcar tareas como completadas
Filtrar tareas (completadas y pendientes)
Gestión básica de usuarios
Documentación automática con Swagger

Requisitos

Antes de comenzar, asegúrate de tener instalado:

Python 3.8 o superior
pip (gestor de paquetes de Python)

Instalación
Instalar dependencias:

pip install fastapi uvicorn
▶️ Ejecución

Ejecuta el servidor con:

uvicorn main:app --reload
🌐 Acceso a la API

Una vez ejecutado, abre en tu navegador:

API:
http://127.0.0.1:8000
Documentación interactiva (Swagger):
http://127.0.0.1:8000/docs

Uso

Desde /docs podrás:

Probar todos los endpoints
Enviar datos (POST, PUT)
Eliminar registros (DELETE)

Ejemplo de endpoints
GET /tareas
POST /tareas
PUT /tareas/{indice}
DELETE /tareas/{indice}
GET /tareas/pendientes

Tecnologías
Python
FastAPI
Uvicorn

Autor
Proyecto desarrollado como práctica de aprendizaje en backend con FastAPI 
