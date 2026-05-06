-- 
-- ESQUEMA/SCRIPT DE LA BD POR SI ACASO ALGO FALLA EN LA AUTOMATIZACIÓN
 CREATE DATABASE inventario_db;
-- \c inventario_db;


-- TABLA: proveedor

CREATE TABLE IF NOT EXISTS proveedor (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100)
);

-- Índices para optimizar búsquedas por nombre
CREATE INDEX IF NOT EXISTS ix_proveedor_nombre ON proveedor (nombre);


-- TABLA: categoria

CREATE TABLE IF NOT EXISTS categoria (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255)
);

CREATE INDEX IF NOT EXISTS ix_categoria_nombre ON categoria (nombre);


-- TABLA: producto

CREATE TABLE IF NOT EXISTS producto (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DOUBLE PRECISION NOT NULL,
    stock_actual INTEGER NOT NULL DEFAULT 0,
    stock_minimo INTEGER NOT NULL DEFAULT 10,
    categoria_id INTEGER NOT NULL,
    proveedor_id INTEGER NOT NULL,
    
  
    CONSTRAINT fk_producto_categoria FOREIGN KEY (categoria_id) 
        REFERENCES categoria (id) ON DELETE CASCADE,
        
    CONSTRAINT fk_producto_proveedor FOREIGN KEY (proveedor_id) 
        REFERENCES proveedor (id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS ix_producto_nombre ON producto (nombre);


-- PENDIENTE CON ESTO: Se utilizó ON DELETE CASCADE para respetar la directiva 
-- cascade= all, delete-orphan establecida en los modelos ORM.
