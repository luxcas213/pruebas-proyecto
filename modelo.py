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



"""funcion para guardar el stl"""
def save_mesh(vertices: np.ndarray, faces: np.ndarray, filename: str) -> None:
    # Armo el mesh
    mesh_data = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    
    # Asigno los vértices a las caras
    for i, face in enumerate(faces):
        for j in range(3):
            mesh_data.vectors[i][j] = vertices[face[j]]
    
    # Defino el path para el directorio static
    static_path = os.path.join(os.getcwd(), "static")
    
    # Creo el directorio si no existe
    if not os.path.exists(static_path):
        os.makedirs(static_path)
    
    # Guardo el archivo en static
    full_path = os.path.join(static_path, filename)
    mesh_data.save(full_path)
    
    print(f'Mesh saved to {full_path}')




"""funcion para generar el mesh a partir de un grafo"""
def GenerarMeshFromGraph(graph: Tuple[List[List[int]], List[List[float]]]) -> None:
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






"""funcion para crear el mesh a partir de voxels"""
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





"""codigo de creacion de matris a base del sistma monje"""
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
