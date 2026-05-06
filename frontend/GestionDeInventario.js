const BASE_URL = "/api"; 

const cuerpoTabla = document.getElementById("CuerpoTabla");
const btnTodo = document.getElementById("btnTodo");
const btnAlertas = document.getElementById("btnAlertas");

function renderizarTabla(productos) {
    cuerpoTabla.innerHTML = "";

    if (!productos || productos.length === 0) {
        cuerpoTabla.innerHTML = `<tr><td colspan="7">No hay datos (ejecuta seeder.py)</td></tr>`;
        return;
    }

    productos.forEach(prod => {
        const actual = prod.stock_actual;
        const minimo = prod.stock_minimo;
        const esBajoStock = actual <= minimo;

        const fila = `
            <tr class="${esBajoStock ? 'stock-bajo' : ''}">
                <td><strong>#${prod.id}</strong></td>
                <td>${prod.nombre}</td>
                <td>${actual}</td>
                <td>${minimo}</td>
                <td>${prod.categoria?.nombre || prod.categoria_id}</td>
                <td>${prod.proveedor?.nombre || prod.proveedor_id}</td>
                <td>
                    <span class="badge-estado ${esBajoStock ? 'badge-alerta' : 'badge-ok'}">
                        ${esBajoStock ? '⚠️ Stock Bajo' : '✓ En Stock'}
                    </span>
                </td>
            </tr>
        `;
        cuerpoTabla.insertAdjacentHTML("beforeend", fila);
    });
}

async function realizarPeticion(endpoint) {
    try {

        const respuesta = await fetch(`${BASE_URL}${endpoint}`);
        
        if (!respuesta.ok) throw new Error(`Error HTTP: ${respuesta.status}`);

        const datos = await respuesta.json();
        renderizarTabla(datos);

    } catch (error) {
        console.error("Error detallado:", error);
        cuerpoTabla.innerHTML = `
            <tr>
                <td colspan="7" style="color: red; padding: 20px;">
                    <strong>Error de conexión:</strong> No se pudo conectar al backend en ${BASE_URL}.<br>
                    Verifica que el servidor de FastAPI esté corriendo.
                </td>
            </tr>`;
    }
}

const btnAgregar = document.getElementById("btnAgregar");
const formularioProducto = document.getElementById("formulario-producto");
const formCrear = document.getElementById("formCrear");
const btnCancelar = document.getElementById("btnCancelar");
const mensajeFormulario = document.getElementById("mensaje-formulario");

btnAgregar.onclick = () => {
    formularioProducto.classList.toggle("visible");
    mensajeFormulario.textContent = "";
    mensajeFormulario.className = "mensaje";
};

btnCancelar.onclick = () => {
    formularioProducto.classList.remove("visible");
    formCrear.reset();
    mensajeFormulario.textContent = "";
    mensajeFormulario.className = "mensaje";
};

formCrear.onsubmit = async (e) => {
    e.preventDefault();
    mensajeFormulario.textContent = "";
    mensajeFormulario.className = "mensaje";

    const datos = {
        nombre: document.getElementById("campo-nombre").value,
        precio: parseFloat(document.getElementById("campo-precio").value),
        stock_actual: parseInt(document.getElementById("campo-stock").value),
        stock_minimo: parseInt(document.getElementById("campo-stock-minimo").value),
        categoria_id: parseInt(document.getElementById("campo-categoria").value),
        proveedor_id: parseInt(document.getElementById("campo-proveedor").value)
    };

    try {
        const respuesta = await fetch(`${BASE_URL}/productos`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(datos)
        });

        if (!respuesta.ok) {
            const err = await respuesta.json();
            throw new Error(err.detail || "Error al crear el producto");
        }

        mensajeFormulario.textContent = "Producto creado correctamente";
        mensajeFormulario.className = "mensaje exito";
        formCrear.reset();
        realizarPeticion("/productos/");
    } catch (error) {
        mensajeFormulario.textContent = "Error: " + error.message;
        mensajeFormulario.className = "mensaje error";
    }
};

btnTodo.onclick = () => realizarPeticion("/productos");
btnAlertas.onclick = () => realizarPeticion("/inventario/alertas");

window.onload = () => realizarPeticion("/productos");
