from modelo import mostrar
from modelo import matrix as mx
from modelo import save_stl as save
import copy

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
    n = len(matrix)
    matrixAUX = copy.deepcopy(matrix)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if matrix[x][y][z] == 1:
                    if not tieneVecinoCero(x, y, z, matrix):
                        matrixAUX[x][y][z] = 0
    return matrixAUX

def main():
    matrix = mx.matrix
    xy = mx.xy
    xz = mx.xz
    yz = mx.yz
    n = mx.n

    for x in range(n):
        for y in range(n):
            if xy[x][y] == 0:
                for z in range(n):
                    matrix[x][y][z] = 0

    for x in range(n):
        for z in range(n):
            if xz[x][z] == 0:
                for y in range(n):
                    matrix[x][y][z] = 0

    for y in range(n):
        for z in range(n):
            if yz[y][z] == 0:
                for x in range(n):
                    matrix[x][y][z] = 0


    matrix = optimizarMatrix(matrix)
    vertices, faces = save.voxel_to_mesh(matrix)
    save.save_mesh(vertices, faces, 'output.stl')
    mostrar.mostrar_voxeles(matrix)

if __name__ == "__main__":
    main()
