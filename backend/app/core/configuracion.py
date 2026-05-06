from pydantic_settings import BaseSettings, SettingsConfigDict

class Configuraciones(BaseSettings):
    URL_BASE_DATOS: str = "postgresql://postgres:root@localhost:5432/inventario_db"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

configuracion = Configuraciones()
