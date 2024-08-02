import numpy as np
from stl import mesh
import os
from scipy.spatial import ConvexHull

def create_voxel_mesh(x, y, z, size=1.0):
    vertices = np.array([
        [x, y, z],
        [x + size, y, z],
        [x + size, y + size, z],
        [x, y + size, z],
        [x, y, z + size],
        [x + size, y, z + size],
        [x + size, y + size, z + size],
        [x, y + size, z + size]
    ])
    
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
    voxel_matrix = np.array(voxel_matrix, dtype=bool)
    
    all_vertices = []
    all_faces = []
    
    for x in range(voxel_matrix.shape[0]):
        for y in range(voxel_matrix.shape[1]):
            for z in range(voxel_matrix.shape[2]):
                if voxel_matrix[x, y, z]:
                    voxel_vertices, voxel_faces = create_voxel_mesh(x, y, z)
                    vertex_offset = len(all_vertices)
                    all_vertices.extend(voxel_vertices)
                    
                    for face in voxel_faces:
                        all_faces.append(face + vertex_offset)
    
    all_faces = np.array(all_faces)
    all_vertices = np.array(all_vertices)
    
    return all_vertices, all_faces

def save_mesh(vertices, faces, filename):
    mesh_data = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    
    for i, face in enumerate(faces):
        for j in range(3):
            mesh_data.vectors[i][j] = vertices[face[j]]
    
    downloads_path = os.path.expanduser("~/Downloads")
    full_path = os.path.join(downloads_path, filename)
    mesh_data.save(full_path)
    print(f'Mesh saved to {full_path}')

def simplify_mesh_max(vertices, faces):
    hull = ConvexHull(vertices)
    simplified_faces = hull.simplices
    return vertices, simplified_faces

