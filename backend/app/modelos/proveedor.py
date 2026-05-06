from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Proveedor(Base):
    __tablename__ = "proveedor"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True, nullable=False)
    contacto = Column(String(100), nullable=True)
    
    productos = relationship("Producto", back_populates="proveedor", cascade="all, delete-orphan")
