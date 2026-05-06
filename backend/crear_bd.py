import sys
import os

#  path para poder importar el módulo app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from sqlalchemy import text
from app.db.sesion import engine
from app.core.configuracion import configuracion

def verificar_conexion():
    """
    Verifica la conexión a la base de datos PostgreSQL configurada en .env
    """
    print(f"Intentando conectar a: {configuracion.URL_BASE_DATOS}")
    try:
        with engine.connect() as conexion:
            #  consulta simple para verificar la conexión
            resultado = conexion.execute(text("SELECT 1"))
            if resultado.fetchone():
                print("\n[ÉXITO] Conexión establecida correctamente con PostgreSQL.")
                print("El servidor está respondiendo.")
    except Exception as e:
        print(f"\n[ERROR] No se pudo conectar a la base de datos.")
        try:
            print(f"Detalle: {str(e)}")
        except UnicodeEncodeError:
            print(f"Detalle: {str(e).encode('ascii', 'ignore').decode('ascii')}")
        
        print("\nPor si no estoy:):")
        print("1. Verificar que el servicio de PostgreSQL esté ejecutándose.")
        print("2. Asegurarse de que el usuario y la contraseña en .env sean correctos.")
        print(f"3. Validen que la base de datos '{configuracion.URL_BASE_DATOS.split('/')[-1]}' exista.")

if __name__ == "__main__":
    verificar_conexion()
