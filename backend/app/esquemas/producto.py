from pydantic import BaseModel, Field
from typing import Optional
from app.esquemas.categoria import Categoria
from app.esquemas.proveedor import Proveedor

class ProductoBase(BaseModel):
    nombre: str
    precio: float = Field(gt=0, description="El precio debe ser mayor a 0")
    stock_actual: int = Field(ge=0, description="El stock no puede ser negativo")
    stock_minimo: int = Field(ge=0, default=10, description="El stock mínimo no puede ser negativo")
    categoria_id: int
    proveedor_id: int

class ProductoCrear(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int
    #  información de la categoría y proveedor para la vista de la tabla en el Frontend
    categoria: Optional[Categoria] = None
    proveedor: Optional[Proveedor] = None

    class Config:
        from_attributes = True
