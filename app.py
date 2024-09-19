from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import numpy as np
import modelo as fn

app = FastAPI()

# Montar la carpeta 'static' para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Modelo de datos para la solicitud POST
class Matrices(BaseModel):
    size: int
    matriz1: List[List[bool]]
    matriz2: List[List[bool]]
    matriz3: List[List[bool]]

@app.get("/", response_class=HTMLResponse)
async def serve_html():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())


@app.post("/procesar")
async def procesar(request: Matrices):
    matriz1 = np.array(request.matriz1, dtype=bool)
    matriz2 = np.array(request.matriz2, dtype=bool)
    matriz3 = np.array(request.matriz3, dtype=bool)

    matrix = fn.createMatrix(matriz1, matriz2, matriz3, request.size)
    fn.voxel_to_mesh(matrix)
    

    resultado = "Matrices procesadas y STL generado."
    return {"resultado": resultado}

