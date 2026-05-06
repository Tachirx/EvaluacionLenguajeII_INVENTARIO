from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.configuracion import configuracion

engine = create_engine(configuracion.URL_BASE_DATOS, pool_pre_ping=True)
SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
