from pydantic import BaseModel
from typing import Optional

class ProveedorBase(BaseModel):
    nombre: str
    contacto: Optional[str] = None

class ProveedorCrear(ProveedorBase):
    pass

class Proveedor(ProveedorBase):
    id: int

    class Config:
        from_attributes = True
