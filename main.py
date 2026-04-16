from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return{"mensaje": "API funcionando"}

@app.get("/saludo")
def saludo():
    return{"mensaje": "Saludos estudiantes Python Senior"}

@app.get("/saludo/{nombre}")
def salud_nombre(nombre: str):
    return {"mensaje": f"Hola {nombre}"}

@app.get("/suma/{a}/{b}")
def suma(a: int, b:int):
    return{"resultado": a + b}

@app.get("/edad/{edad}")
def verificar_edad(edad: int):
    if edad >= 18:
        return{"mensaje": "Mayor de edad"}
    return{"mensaje": "Menor de edad"}

#LISTA DE TAREAS

tareas = []

@app.get("/tareas")
def obtener_tareas():
    return tareas

@app.post("/tareas")
def crear_tarea(nombre: str):
    tareas.append({"nombre": nombre, "completada" : False})
    return{"mensaje": "Tarea creada"}

@app.put("/tareas/{indice}")
def actualizar_tarea(indice: int, nuevo_nombre: str):
    if indice >= len(tareas):
        return {"error": "Indice no válido"}
    tareas[indice]["nombre"] =nuevo_nombre
    return{"mensaje": "Tarea actualizada"}

@app.delete("/tareas/{indice}")
def eliminar_tarea(indice: int):
    if indice >= len(tareas):
        return{"error": "Indice no válido"}
    tareas.pop(indice)
    return{"mensaje": "Tarea Eliminada"}

@app.put("/tareas/completar/{indice}")
def completar_tareas(indice: int):
    if indice >= len(tareas):
        return {"error": "Indice no válido"}
    tareas[indice]["completada"] = True
    return{"mensaje": "Tarea completada"}

@app.get("/tareas/pendientes")
def tareas_pendientes():
    return[t for t in tareas if not t["completada"]]

@app.get("/tareas/cantidad")
def cantidad_tareas():
    return{"total": len(tareas)}

@app.get("/buscar")
def buscar_tarea(nombre: str):
    return[t for t in tareas if nombre.lower() in t["nombre"].lower()]
