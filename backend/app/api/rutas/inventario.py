from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import crud_producto
from app.esquemas.producto import Producto
from app.api.dependencias import obtener_bd

enrutador = APIRouter()

@enrutador.get("/alertas", response_model=List[Producto])
def obtener_alertas_stock(db: Session = Depends(obtener_bd)):
    """
    Retorna únicamente los productos cuyo stock_actual sea menor o igual al stock_minimo.
    """
    productos_en_alerta = crud_producto.obtener_productos_con_alerta(db)
    return productos_en_alerta
