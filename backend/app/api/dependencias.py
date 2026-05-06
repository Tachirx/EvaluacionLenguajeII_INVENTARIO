from typing import Generator
from app.db.sesion import SesionLocal

def obtener_bd() -> Generator:
    """
    Generador de dependencia que provee una sesión de base de datos
    para cada petición y asegura su cierre al finalizar.
    """
    try:
        bd = SesionLocal()
        yield bd
    finally:
        bd.close()
