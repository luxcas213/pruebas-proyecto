import numpy as np
from stl import mesh
import os
import numpy as np
from typing import List
import copy  
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import List, Tuple
from typing import List, Tuple

def newcubegraph() -> Tuple[List[List[int]], List[List[int]]]:
    vertices: List[List[int]] = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    
    connections: List[List[int]] = [[1, 2, 4], [0, 5, 3], [0, 3, 6], [2, 7, 1], [0, 5, 6], [4, 7, 1], [2, 4, 7], [3, 6, 5]]
    
    return connections, vertices

def newpyramidgraph() -> Tuple[List[List[int]], List[List[int]]]:
    vertices: List[List[int]] = [
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0.5, 0.5, 1]
    ]
    
    connections: List[List[int]] = [
        [1, 3, 4],
        [0, 2, 4],
        [1, 3, 4],
        [0, 2, 4],
        [0, 1, 2, 3]
    ]
    
    return connections, vertices


def GenerarMeshFromGraph(graph: Tuple[List[List[int]], List[List[int]]]) -> None:
    vertices = graph[1]
    connections = graph[0]
    all_faces = []
    
    for i in range(len(vertices)):
        con = connections[i] 
        num_con = len(con)
        for j in range(num_con):
            v1 = i
            v2 = con[j]
            v3 = con[((j + 1) % num_con)]
            #checkeo de que no exista esta cara
            if [v1, v2, v3] not in all_faces and [v3, v2, v1] not in all_faces:
                all_faces.append([v1, v2, v3])
            
    
    all_faces = np.array(all_faces)
    all_vertices = np.array(vertices)
    
    save_mesh(all_vertices, all_faces, 'output.stl')


def create_voxel_mesh(x: int, y: int, z: int, size_x: int, size_y: int, size_z: int) -> tuple[np.ndarray, np.ndarray]:
    # creo los vertices desde la pocicion inicial hasta el tamaño del rectángulo
    vertices = np.array([
        [x, y, z],
        [x + size_x, y, z],
        [x + size_x, y + size_y, z],
        [x, y + size_y, z],
        [x, y, z + size_z],
        [x + size_x, y, z + size_z],
        [x + size_x, y + size_y, z + size_z],
        [x, y + size_y, z + size_z]
    ])
    
    # asigno qué trios de vertices generan un triangulo de cara
    faces = np.array([
        [2, 1, 0],
        [3, 2, 0],
        [4, 5, 6],
        [4, 6, 7],
        [0, 1, 5],
        [0, 5, 4],
        [1, 2, 6],
        [1, 6, 5],
        [2, 3, 7],
        [2, 7, 6],
        [3, 0, 4],
        [3, 4, 7]
    ])
    
    return vertices, faces

def voxel_to_mesh(voxel_matrix: np.ndarray):
    
    """
    Uso el gready meshing para simplificar la matriz de voxeles y generar un mesh
    """
    voxel_matrix = np.array(voxel_matrix, dtype=bool)
    
    voxel_procesed = np.zeros_like(voxel_matrix, dtype=bool)
    all_vertices = []
    all_faces = []
    n = voxel_matrix.shape[0]
    for x in range(len(voxel_matrix)):
        for y in range(len(voxel_matrix[0])):
            for z in range(len(voxel_matrix[0][0])):
                if voxel_matrix[x, y, z] and not voxel_procesed[x, y, z]:
                    #print(f'Processing voxel at ({x}, {y}, {z})')
                    voxel_procesed[x][y][z] = True
                    size_x = size_y = size_z = 1
                    #print(f'size_x: {size_x}, size_y: {size_y}, size_z: {size_z}')
                    for i in range(x + 1, n):
                        if not voxel_matrix[i, y, z] or voxel_procesed[i, y, z]:
                            break
                        voxel_procesed[i, y, z] = True
                        voxel_matrix[i, y, z] = False
                        size_x += 1
                    for j in range(y + 1, n):
                        if not voxel_matrix[x:x + size_x, j, z].all() or voxel_procesed[x:x + size_x, j, z].all():
                            break
                        voxel_procesed[x:x + size_x, j, z] = True
                        voxel_matrix[x:x + size_x, j, z] = 0
                        size_y += 1
                    for k in range(z + 1, n):
                        if not voxel_matrix[x:x + size_x, y:y + size_y, k].all() or voxel_procesed[x:x + size_x, y:y + size_y, k].all():
                            break
                        voxel_procesed[x:x + size_x, y:y + size_y, k] = True
                        voxel_matrix[x:x + size_x, y:y + size_y, k] = 0
                        size_z += 1
                    #print(f'Voxel at ({x}, {y}, {z}) with size ({size_x}, {size_y}, {size_z})')
                    voxel_vertices, voxel_faces = create_voxel_mesh(x, y, z, size_x, size_y, size_z)
                    vertex_offset = len(all_vertices)
                    all_vertices.extend(voxel_vertices)
                    
                    for face in voxel_faces:
                        all_faces.append(face + vertex_offset)
    
    all_faces = np.array(all_faces)
    all_vertices = np.array(all_vertices)
    
    save_mesh(all_vertices, all_faces, 'output.stl')

def createMatrix(xy: List[List[int]], xz: List[List[int]], yz: List[List[int]], n: int) -> List[List[List[int]]]:
    matrix = [[[1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if xy[x][y] == 0:
                for z in range(len(matrix[0][0])):
                    matrix[x][y][z] = 0

    for x in range(len(matrix)):
        for z in range(len(matrix[0][0])):
            if xz[x][z] == 0:
                for y in range(len(matrix[0])):
                    matrix[x][y][z] = 0

    for y in range(len(matrix[0])):
        for z in range(len(matrix[0][0])):
            if yz[y][z] == 0:
                for x in range(len(matrix)):
                    matrix[x][y][z] = 0
    return matrix


def save_mesh(vertices: np.ndarray, faces: np.ndarray, filename: str) -> None:
    #armo el mesh
    mesh_data = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    
    #asigno los vertices a las caras
    for i, face in enumerate(faces):
        for j in range(3):
            mesh_data.vectors[i][j] = vertices[face[j]]
    
    #descargo el mesh en downloads
    downloads_path = os.path.expanduser("~/Downloads")
    full_path = os.path.join(downloads_path, filename)
    mesh_data.save(full_path)
    print(f'Mesh saved to {full_path}')


def tieneVecinoCero(x, y, z, matrix):
    n = len(matrix)
    direcciones = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    
    for dx, dy, dz in direcciones:
        auxX = x + dx
        auxY = y + dy
        auxZ = z + dz
        if 0 <= auxX < n and 0 <= auxY < n and 0 <= auxZ < n:
            if matrix[auxX][auxY][auxZ] == 0:
                return True
        else:
            return True
    return False

def optimizarMatrix(matrix):
    
    matrixAUX = copy.deepcopy(matrix)

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            for z in range(len(matrix[0][0])):
                if matrix[x][y][z] == 1:
                    if not tieneVecinoCero(x, y, z, matrix):
                        matrixAUX[x][y][z] = 0
    return matrixAUX


def mostrar_voxeles(matrix, umbral=0.5):
    matrix = np.array(matrix)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

   
    voxeles = matrix 

    ax.voxels(voxeles, edgecolor='k')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


def generar_matriz_booleana_aleatoria(n:int) -> np.ndarray:
    # Generar una matriz booleana 3D con valores aleatorios
    matriz = np.random.choice([True, False], size=(n, n, n))
    return matriz

def generar_piramide_booleana(n: int) -> np.ndarray:
    # Inicializar una matriz 3D de False
    matriz = np.zeros((n, n, n), dtype=bool)

    # Rellenar la pirámide en la matriz
    for i in range(n):
        nivel = n - i
        start = i
        end = n - i
        matriz[i, start:end, start:end] = True

    return matriz



