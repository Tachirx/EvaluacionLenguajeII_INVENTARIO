from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Producto(Base):
    __tablename__ = "producto"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True, nullable=False)
    precio = Column(Float, nullable=False)
    stock_actual = Column(Integer, nullable=False, default=0)
    stock_minimo = Column(Integer, nullable=False, default=10)
    
    categoria_id = Column(Integer, ForeignKey("categoria.id"), nullable=False)
    proveedor_id = Column(Integer, ForeignKey("proveedor.id"), nullable=False)
    
    categoria = relationship("Categoria", back_populates="productos")
    proveedor = relationship("Proveedor", back_populates="productos")
