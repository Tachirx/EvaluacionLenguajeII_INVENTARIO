from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from app.api.rutas import productos, inventario
from app.db.base import Base
from app.db.sesion import engine

#  rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # c:/.../backend
ROOT_DIR = os.path.dirname(BASE_DIR) # c:/.../EvaluacionLenguajeII
RUTA_FRONTEND = os.path.join(ROOT_DIR, "frontend")

app = FastAPI(
    title="Gestor de Inventario API",
    description="API REST para la gestión de inventario y alertas de stock bajo.",
    version="1.0.0"
)

# CONFIGURACION DEL CORS
origenes_permitidos = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173", # suponiendo que sea igual mío
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origenes_permitidos,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# archivos estáticos (CSS, JS)
app.mount("/static", StaticFiles(directory=RUTA_FRONTEND), name="static")

# os enrutadores
app.include_router(productos.enrutador, prefix="/api/productos", tags=["Productos"])
app.include_router(inventario.enrutador, prefix="/api/inventario", tags=["Inventario"])

@app.get("/")
def leer_interfaz():
    return FileResponse(os.path.join(RUTA_FRONTEND, "index.html"))
