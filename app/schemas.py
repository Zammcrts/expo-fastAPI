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


class EvaluacionIn(BaseModel):
    innovacion: int = Field(ge=1, le=10)
    viabilidad: int = Field(ge=1, le=10)
    presentacion: int = Field(ge=1, le=10)


class Evaluacion(EvaluacionIn):
    id: int
    proyecto_id: int


class Resumen(BaseModel):
    proyecto_id: int
    total_evaluaciones: int
    innovacion: float | None
    viabilidad: float | None
    presentacion: float | None
    general: float | None
