# pruebas proyecto

Para instalar todas las bibliotecas:

```bash
pip install -r requirements.txt
```

Para ejecutar:

```bash
python -m modelo.index
```

Funciones principales:

Generar basado en voxels:

Sistema Monk:

```
n = 100
xy, xz, yz = mx.cuadrado(n), mx.cuadrado(n), mx.cuadrado(n)
matrix = fn.createMatrix(xy, xz, yz,n)
fn.voxel_to_mesh(matrix)
```

mostrar un string:
```
n = 100
    xy, xz, yz = mx.create_word_matrix("hola",n), mx.cuadrado(n), mx.cuadrado(n)
    matrix = fn.createMatrix(xy, xz, yz,n)
    fn.voxel_to_mesh(matrix)
```

Matriz ya creada:

Aleatorio:

```
matrix = fn.generar_matriz_booleana_aleatoria(10)
fn.voxel_to_mesh(matrix)
```

Pirámide:

```
matrix = fn.generar_piramide_booleana(10)
fn.voxel_to_mesh(matrix)
```

Generar basado en grafos:

Cubo:

```
graph = fn.newcubegraph()
fn.GenerarMeshFromGraph(graph)
```

Grafo de pirámide:

```
graph = fn.newpyramidgraph()
fn.GenerarMeshFromGraph(graph)
```

Grafo de tetraedro:

```
graph = fn.newtetrahedrongraph()
fn.GenerarMeshFromGraph(graph)
```

Grafo de octaedro:

```
graph = fn.newoctahedrongraph()
fn.GenerarMeshFromGraph(graph)
```

Optimizaciones de matriz:

```
matrix = fn.optimizar_matriz(matrix)
```

Mostrar voxels en matplotlib:

```
fn.mostrar_voxels(matrix)
```

