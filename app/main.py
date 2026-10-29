from typing import Annotated
from fastapi import FastAPI, HTTPException, Query

from app.repository import repository
from app.schemas import (
    Categoria,
    Proyecto,
    ProyectoIN,
    Evaluacion,
    EvaluacionIn,
    Resumen,
)

app = FastAPI(title="THE ULTIMATE SUPER EVALUATION")



def buscar_proyecto(proyecto_id: int) -> Proyecto:
    proyecto = repository.obtener_proyecto(proyecto_id)
    if proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return proyecto


@app.get("/")
def raiz():
    return {"mensaje": "Hola mundo muejejejejjee"}


@app.post("/proyectos", response_model=Proyecto, status_code=201)
def crear_proyecto(datos: ProyectoIN):
    return repository.crear_proyecto(datos)


@app.get("/proyectos", response_model=list[Proyecto])
def listar_proyectos(
    categoria: Categoria | None = None,
    limite: Annotated[int, Query(ge=1, le=100)] = 10
):
    return repository.listar_proyectos(categoria, limite)


@app.get("/proyectos/{proyecto_id}", response_model=Proyecto)
def obtener_proyecto(proyecto_id: int):
    return buscar_proyecto(proyecto_id)


@app.post(
    "/proyectos/{proyecto_id}/evaluaciones",
    response_model=Evaluacion,
    status_code=201
)
def crear_evaluacion(proyecto_id: int, datos: EvaluacionIn):
    buscar_proyecto(proyecto_id)
    return repository.crear_evaluacion(proyecto_id, datos)


@app.get(
    "/proyectos/{proyecto_id}/evaluaciones",
    response_model=list[Evaluacion]
)
def listar_evaluaciones(proyecto_id: int):
    buscar_proyecto(proyecto_id)
    return repository.listar_evaluaciones(proyecto_id)


@app.get("/proyectos/{proyecto_id}/resumen", response_model=Resumen)
def resumen_proyecto(proyecto_id: int):
    buscar_proyecto(proyecto_id)
    return repository.resumen(proyecto_id)
