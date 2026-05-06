# Importar todos los modelos para que Base.metadata.create_all() los registre correctamente.
from app.db.base_class import Base
from app.modelos.proveedor import Proveedor
from app.modelos.categoria import Categoria
from app.modelos.producto import Producto
