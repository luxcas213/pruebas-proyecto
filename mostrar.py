import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def mostrar(matrix):
    print("\n\n\n")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
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





def mostrar_caras(matrix):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x_dim, y_dim, z_dim = np.array(matrix).shape

    faces = []

    for i in range(x_dim):
        for j in range(y_dim):
            for k in range(z_dim):
                if matrix[i][j][k] == 1:
                    faces.extend(crear_cubo(i, j, k))

    poly3d = Poly3DCollection(faces, alpha=.9, linewidths=2, edgecolors='r')
    ax.add_collection3d(poly3d)

    ax.set_xlim(0, x_dim)
    ax.set_ylim(0, y_dim)
    ax.set_zlim(0, z_dim)

    plt.show()
