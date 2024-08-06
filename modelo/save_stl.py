import numpy as np
from stl import mesh
import os

def create_voxel_mesh(x, y, z, size_x,size_y,size_z):
    #creo los vertices desde la pocicion inicial hatsa el tamaño de el recrangulo
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
    
    #asigno que trios de vertices generan un triangulo de cara
    faces = np.array([
        [0, 1, 2],
        [0, 2, 3],
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

def voxel_to_mesh(voxel_matrix):
    
    """"
    uso el gready meshing para simplificar la matrix de voxeles y generar un mesh
    """
    voxel_matrix = np.array(voxel_matrix, dtype=bool)
    voxel_procesed = np.zeros_like(voxel_matrix,dtype=bool)
    all_vertices = []
    all_faces = []
    n=voxel_matrix.shape[0]
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if voxel_matrix[x, y, z] and not voxel_procesed[x, y, z]:
                    voxel_procesed[x][y][z] = True
                    size_x = size_y = size_z = 1
                    for i in range(x + 1, n):
                        if not voxel_matrix[i, y, z] and not voxel_procesed[i, y, z]:
                            break
                        voxel_procesed[i, y, z] = True
                        size_x += 1
                    for j in range(y + 1, n):
                        if not voxel_matrix[x:x + size_x, j, z].all() and not voxel_procesed[x:x + size_x, j, z].all():
                            break
                        voxel_procesed[x:x + size_x, j, z] = True
                        size_y += 1
                    for k in range(z + 1, n):
                        if not voxel_matrix[x:x + size_x, y:y + size_y, k].all() and not voxel_procesed[x:x + size_x, y:y + size_y, k].all():
                            break
                        voxel_procesed[x:x + size_x, y:y + size_y, k] = True
                        size_z += 1
                    voxel_vertices, voxel_faces = create_voxel_mesh(x, y, z, size_x, size_y, size_z)
                    vertex_offset = len(all_vertices)
                    all_vertices.extend(voxel_vertices)
                    
                    for face in voxel_faces:
                        all_faces.append(face + vertex_offset)
    
    all_faces = np.array(all_faces)
    all_vertices = np.array(all_vertices)
    
    return all_vertices, all_faces

def save_mesh(vertices, faces, filename):
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


