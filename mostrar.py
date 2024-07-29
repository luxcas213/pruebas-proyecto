import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection



def mostrar(matrix):
    print("\n\n\n")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                print(matrix[i][j][k], end=" ")
            print()
        print()


def crear_cubo(x, y, z):
    return [
        [[x, y, z], [x+1, y, z], [x+1, y+1, z], [x, y+1, z]],

        [[x, y, z+1], [x+1, y, z+1], [x+1, y+1, z+1], [x, y+1, z+1]],

        [[x, y, z], [x+1, y, z], [x+1, y, z+1], [x, y, z+1]],

        [[x, y+1, z], [x+1, y+1, z], [x+1, y+1, z+1], [x, y+1, z+1]],

        [[x, y, z], [x, y+1, z], [x, y+1, z+1], [x, y, z+1]],

        [[x+1, y, z], [x+1, y+1, z], [x+1, y+1, z+1], [x+1, y, z+1]],
    ]


def tiene_vecino_cero(matrix, x, y, z):
    x_dim, y_dim, z_dim = len(matrix), len(matrix), len(matrix)
    if x==x_dim-1 or y==y_dim-1 or z==z_dim-1 or x==0 or y==0 or z==0:
        return True
    vecinos = [
        (x-1, y, z), (x+1, y, z),
        (x, y-1, z), (x, y+1, z),
        (x, y, z-1), (x, y, z+1)
    ]
    
    for vx, vy, vz in vecinos:
        if vx < 0 or vx >= x_dim or vy < 0 or vy >= y_dim or vz < 0 or vz >= z_dim:
            continue
        if matrix[vx][vy][vz] == 0:
            return True
    return False


def mostrar_puntos(matrix):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_dim, y_dim, z_dim = np.array(matrix).shape

    x_points = []
    y_points = []
    z_points = []

    for i in range(x_dim):
        for j in range(y_dim):
            for k in range(z_dim):
                if matrix[i][j][k] == 1 :
                    x_points.append(i)
                    y_points.append(j)
                    z_points.append(k)

    ax.scatter(x_points, y_points, z_points, c='b', marker='o')

    ax.set_xlim(0, x_dim)
    ax.set_ylim(0, y_dim)
    ax.set_zlim(0, z_dim)

    plt.show()


def mostrar_caras(matrix):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_dim, y_dim, z_dim = np.array(matrix).shape

    faces = []

    for i in range(x_dim):
        for j in range(y_dim):
            for k in range(z_dim):
                if matrix[i][j][k] == 1 and tiene_vecino_cero(matrix, i, j, k):
                    faces.extend(crear_cubo(i, j, k))

    poly3d = Poly3DCollection(faces, alpha=.5, linewidths=.5, edgecolors='r')
    ax.add_collection3d(poly3d)

    ax.set_xlim(0, x_dim)
    ax.set_ylim(0, y_dim)
    ax.set_zlim(0, z_dim)

    plt.show()


def usar_pyvoxels(matrix):
    voxel_grid = pyvoxels.VoxelGrid(matrix)
    voxel_grid.plot()