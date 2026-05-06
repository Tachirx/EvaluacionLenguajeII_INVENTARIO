# Bitácora Técnica

### [2026-05-03 19:24]
- **Resumen:** Implementación completa del MVP del Gestor de Inventario (Backend).
- **Detalles Técnicos:**
  - Desarrollo de API REST utilizando FastAPI y SQLAlchemy.
  - Modelado de base de datos relacional (PostgreSQL) para entidades: `Proveedor`, `Categoria` y `Producto` con relaciones One-to-Many y comportamiento `cascade`.
  - Implementación de capa ORM con inyección de dependencias estricta para el manejo de sesiones de base de datos (`app/api/dependencias.py`).
  - Creación de esquemas Pydantic (`app/esquemas/`) con validación de tipos e integridad de datos de entrada.
  - Segregación de responsabilidades aislando la lógica transaccional en la capa `CRUD`.
  - Endpoints implementados:
    - `POST /productos`: Registro con validación.
    - `GET /productos`: Listado general.
    - `GET /inventario/alertas`: Consulta especializada de monitoreo (`stock_actual <= stock_minimo`).
  - Script de Seeders de prueba (`app/seeder.py`) y script DDL nativo desarrollado (`esquema_postgresql.sql`).
  - Código final depurado y refactorizado respetando los lineamientos de nomenclatura e identidad del proyecto.

### [2026-05-06 10:25]
- **Resumen:** Conversión de documento PDF a formato de imagen (JPG).
- **Detalles Técnicos:**
  - Instalación de la librería `PyMuPDF` (fitz) para el procesamiento de documentos PDF.
  - Creación y ejecución de un script de automatización (`convertir_pdf.py`) para extraer 36 páginas del solucionario.
  - Generación de imágenes en alta resolución (escalado 2x) almacenadas en el directorio `imagenes_pdf/`.

### [2026-05-06 19:04]
- **Resumen:** Rediseño Premium e Integración Total de Interfaz.
- **Detalles Técnicos:**
  - Integración de archivos estáticos en FastAPI para servir la interfaz desde la raíz (`/`).
  - Rediseño estético completo del Frontend usando tipografía *Inter*, Glassmorphism y sistema de Badges condicionales para estados de stock.
  - Reorganización de la estructura del proyecto: Carpeta `Ejercicio` renombrada a `frontend`.
  - Refactorización de `GestionDeInventario.js` para utilizar rutas relativas y prefijo `/api/`.
  - Migración exitosa de credenciales de conexión local (`postgres:root`) en `.env`.
