from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import crud_producto
from app.esquemas.producto import Producto, ProductoCrear
from app.api.dependencias import obtener_bd

enrutador = APIRouter()

@enrutador.post("/", response_model=Producto, status_code=201)
def crear_producto(
    producto: ProductoCrear,
    db: Session = Depends(obtener_bd)
):
    """
    Crea un nuevo producto en el sistema.
    """
    try:
        return crud_producto.crear_producto(db=db, producto=producto)
    except Exception as e:
        # manejo de error estandar
        raise HTTPException(
            status_code=400, 
            detail="Error al crear el producto. Verifique los datos o si la categoría/proveedor existen."
        )

@enrutador.get("/", response_model=List[Producto])
def leer_productos(
    saltar: int = 0,
    limite: int = 100,
    db: Session = Depends(obtener_bd)
):
    """
    Obtiene el listado total del inventario.
    """
    productos = crud_producto.obtener_productos(db, saltar=saltar, limite=limite)
    return productos
