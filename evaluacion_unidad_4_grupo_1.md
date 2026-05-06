# REPÚBLICA BOLIVARIANA DE VENEZUELA
**MINISTERIO DEL PODER POPULAR PARA LA DEFENSA**
**UNIVERSIDAD NACIONAL EXPERIMENTAL POLITÉCNICA DE LA FUERZA ARMADA NACIONAL (UNEFA)**

**Carrera:** Ingeniería de Sistemas
**Asignatura:** Lenguajes de Programación II
**Profesor:** Jesus Piñate

## Evaluación grupal - Unidad 4 - Grupo 1

### 1. Gestor de Inventario con Alertas de Stock

Una empresa de suministros industriales ha detectado pérdidas significativas debido a la falta de previsión en su inventario. El sistema actual no permite identificar a tiempo cuándo un producto está por agotarse. Se le solicita desarrollar un Producto Mínimo Viable (MVP) que permita gestionar el catálogo de productos y emita alertas visuales basadas en niveles de stock críticos.

---

### Requerimientos Técnicos (Backend - FastAPI)

Deberá construir una API REST utilizando FastAPI y SQLAlchemy que cumpla con los siguientes puntos:

*   **Modelado de Datos:** Implementar un esquema de base de datos relacional (SQLite/PostgreSQL) que incluya al menos tres entidades relacionadas:
    *   **Proveedor:** `(id, nombre, contacto)`.
    *   **Categoría:** `(id, nombre, descripción)`.
    *   **Producto:** `(id, nombre, precio, stock_actual, stock_minimo, categoria_id, proveedor_id)`.
*   **Relaciones:** Configurar relaciones One-to-Many (Un proveedor/categoría puede tener múltiples productos).
*   **Endpoints Obligatorios:**
    *   `POST /productos`: Registro de nuevos artículos con validación de datos (Pydantic).
    *   `GET /productos`: Listado total de inventario.
    *   `GET /inventario/alertas`: Un endpoint especializado que retorne únicamente los productos cuyo `stock_actual` sea menor o igual al `stock_minimo`.

---

### Requerimientos de Interfaz (Frontend)

La aplicación cliente debe consumir la API y presentar la información de manera funcional:

*   **Visualización Dinámica:** Una tabla que muestre el listado de productos incluyendo el nombre de su categoría y proveedor.
*   **Lógica de Alerta:** Implementar renderizado condicional en la interfaz. Si un producto se encuentra en estado de "stock bajo" (según la lógica del backend), la fila o el indicador de cantidad debe resaltarse visualmente (ej. color rojo o etiqueta de advertencia).
*   **Filtro Rápido:** Un botón o interruptor que permita al usuario conmutar entre "Ver todo" y "Ver solo alertas de stock".
