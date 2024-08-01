from modelo import mostrar
from modelo import matrix as mx
from modelo import save_stl as save
def main():
    matrix = mx.matrix

    xy = mx.xy
    xz = mx.xz
    yz = mx.yz
    n=mx.n
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

    
    
    vertices, faces = save.voxel_to_mesh(matrix)
    save.save_mesh(vertices, faces, 'output.stl')
    mostrar.mostrar_voxeles(matrix)


if __name__ == "__main__":
    main()
