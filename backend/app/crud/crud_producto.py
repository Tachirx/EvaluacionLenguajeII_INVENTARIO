from sqlalchemy.orm import Session, joinedload
from app.modelos.producto import Producto
from app.esquemas.producto import ProductoCrear

def obtener_productos(db: Session, saltar: int = 0, limite: int = 100):
    return (
        db.query(Producto)
        .options(joinedload(Producto.categoria), joinedload(Producto.proveedor))
        .offset(saltar)
        .limit(limite)
        .all()
    )

def obtener_productos_con_alerta(db: Session):
    return (
        db.query(Producto)
        .options(joinedload(Producto.categoria), joinedload(Producto.proveedor))
        .filter(Producto.stock_actual <= Producto.stock_minimo)
        .all()
    )

def crear_producto(db: Session, producto: ProductoCrear):
    db_producto = Producto(
        nombre=producto.nombre,
        precio=producto.precio,
        stock_actual=producto.stock_actual,
        stock_minimo=producto.stock_minimo,
        categoria_id=producto.categoria_id,
        proveedor_id=producto.proveedor_id
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto
