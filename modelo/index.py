from modelo import mostrar
from modelo import matrix as mx
from modelo import save_stl as save
def main():
    matrix = mx.matrix

    xy = mx.xy
    xz = mx.xz
    yz = mx.yz

    for x in range(len(xy)):
        for y in range(len(xy)):
            if xy[x][y] == 0:
                for z in range(len(matrix)):
                    matrix[x][y][z] = 0

    for x in range(len(xz)):
        for z in range(len(xz)):
            if xz[x][z] == 0:
                for y in range(len(matrix)):
                    matrix[x][y][z] = 0

    for y in range(len(yz)):
        for z in range(len(yz)):
            if yz[y][z] == 0:
                for x in range(len(matrix)):
                    matrix[x][y][z] = 0

    
    
    vertices, faces = save.voxel_to_mesh(matrix)
    save.save_mesh(vertices, faces, 'output.stl')
    mostrar.mostrar_voxeles(matrix)


if __name__ == "__main__":
    main()
