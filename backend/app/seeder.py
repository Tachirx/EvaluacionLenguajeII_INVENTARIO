import sys
import os

#  path del proyecto esta en sys.path para importaciones
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.sesion import SesionLocal
from app.modelos.proveedor import Proveedor
from app.modelos.categoria import Categoria
from app.modelos.producto import Producto
from app.db.base import Base
from app.db.sesion import engine

def poblar_datos():
    # las tablas (creacion)
    Base.metadata.create_all(bind=engine)
    
    bd = SesionLocal()
    try:
        # HAY QUE VERIFICAR si ya existen proveedores para no duplicar en varias ejecuciones
        if bd.query(Proveedor).first():
            print("La base de datos ya contiene información. Se omite el seeder.")
            return

        print("Iniciando la inserción de datos semilla (seeders)...")

        # Proveedores
        prov1 = Proveedor(nombre="Industrial Suministros C.A.", contacto="contacto@industrialsum.com")
        prov2 = Proveedor(nombre="Metalúrgica Andina", contacto="ventas@metalurgica.ve")
        
        bd.add_all([prov1, prov2])
        bd.commit()

        # Categorías
        cat1 = Categoria(nombre="Herramientas", descripcion="Herramientas manuales y eléctricas")
        cat2 = Categoria(nombre="Materiales", descripcion="Materia prima para producción")
        
        bd.add_all([cat1, cat2])
        bd.commit()

        # Productos
        # Producto con stock normal
        prod1 = Producto(
            nombre="Taladro Percutor 800W", 
            precio=120.50, 
            stock_actual=50, 
            stock_minimo=10, 
            categoria_id=cat1.id, 
            proveedor_id=prov1.id
        )
        
        # Producto con stock BAJO (Alerta)
        prod2 = Producto(
            nombre="Caja de Tornillos 2 pulgadas", 
            precio=15.00, 
            stock_actual=5, 
            stock_minimo=15, 
            categoria_id=cat2.id, 
            proveedor_id=prov2.id
        )
        
        # Producto con stock muy critico (Alerta)
        prod3 = Producto(
            nombre="Lámina de Acero 3mm", 
            precio=45.00, 
            stock_actual=2, 
            stock_minimo=10, 
            categoria_id=cat2.id, 
            proveedor_id=prov2.id
        )

        bd.add_all([prod1, prod2, prod3])
        bd.commit()

        print("Datos semilla insertados correctamente.")
        
    except Exception as e:
        bd.rollback()
        print(f"Error al poblar la base de datos: {e}")
    finally:
        bd.close()

if __name__ == "__main__":
    poblar_datos()
