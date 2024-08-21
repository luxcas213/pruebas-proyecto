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

```python
n = 100
xy, xz, yz = mx.cuadrado(n), mx.cuadrado(n), mx.cuadrado(n)
matrix = fn.createMatrix(xy, xz, yz,n)
fn.voxel_to_mesh(matrix)
```

mostrar un string:
```python
n = 100
    xy, xz, yz = mx.create_word_matrix("hola",n), mx.cuadrado(n), mx.cuadrado(n)
    matrix = fn.createMatrix(xy, xz, yz,n)
    fn.voxel_to_mesh(matrix)
```

Matriz ya creada:

Aleatorio:

```python
matrix = fn.generar_matriz_booleana_aleatoria(10)
fn.voxel_to_mesh(matrix)
```

Pirámide:

```python
matrix = fn.generar_piramide_booleana(10)
fn.voxel_to_mesh(matrix)
```

Generar basado en grafos:

Cubo:

```python
graph = fn.newcubegraph()
fn.GenerarMeshFromGraph(graph)
```

Grafo de pirámide:

```python
graph = fn.newpyramidgraph()
fn.GenerarMeshFromGraph(graph)
```

Grafo de tetraedro:

```python
graph = fn.newtetrahedrongraph()
fn.GenerarMeshFromGraph(graph)
```

Grafo de octaedro:

```python
graph = fn.newoctahedrongraph()
fn.GenerarMeshFromGraph(graph)
```

Optimizaciones de matriz:

```python
matrix = fn.optimizar_matriz(matrix)
```

Mostrar voxels en matplotlib:

```python
fn.mostrar_voxels(matrix)
```

