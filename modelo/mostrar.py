import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

def main():
    matrix = [[[0, 0, 0, 0, 0],
               [0, 1, 1, 1, 0],
               [0, 1, 0, 1, 0],
               [0, 1, 1, 1, 0],
               [0, 0, 0, 0, 0]],

              [[0, 1, 1, 1, 0],
               [1, 1, 0, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 1, 0, 1, 1],
               [0, 1, 1, 1, 0]],

              [[0, 1, 0, 1, 0],
               [1, 0, 0, 0, 1],
               [0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1],
               [0, 1, 0, 1, 0]],

              [[0, 1, 1, 1, 0],
               [1, 1, 0, 1, 1],
               [1, 0, 0, 0, 1],
               [1, 1, 0, 1, 1],
               [0, 1, 1, 1, 0]],

              [[0, 0, 0, 0, 0],
               [0, 1, 1, 1, 0],
               [0, 1, 0, 1, 0],
               [0, 1, 1, 1, 0],
               [0, 0, 0, 0, 0]]]
    mostrar_voxeles(matrix, umbral=0.5)

if __name__ == "__main__":
    main()
