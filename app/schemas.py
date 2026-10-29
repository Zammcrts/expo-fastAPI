from enum import Enum
from pydantic import BaseModel, Field


class Categoria(str, Enum):
    software = "SW"
    hardware = "HW"
    impacto_social = "IS"
    inteligencia_artificial = "IA"

#manipulador para el proyecto
class ProyectoIN(BaseModel):
    nombre:str = Field(min_length=3, max_length=120)
    equipo: list[str] = Field(min_items=1, max_items=5)
    categoria: Categoria
#el id se separa cuando ya tengo un objeto manipulable, se hereda
class Proyecto(ProyectoIN):
    id:int