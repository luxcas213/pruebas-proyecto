import mostrar
import matrix as mx


def main():
    matrix = mx.matrix

    xy = mx.xy
    xz = mx.xz
    yz = mx.yz

    for x in range(len(xy)):
        for y in range(len(xy[x])):
            if xy[x][y] == 0:
                for z in range(len(matrix[x][y])):
                    matrix[x][y][z] = 0

    for x in range(len(xz)):
        for z in range(len(xz[x])):
            if xz[x][z] == 0:
                for y in range(len(matrix[x])):
                    matrix[x][y][z] = 0

    for y in range(len(yz)):
        for z in range(len(yz[y])):
            if yz[y][z] == 0:
                for x in range(len(matrix)):
                    matrix[x][y][z] = 0

    
    mostrar.mostrar_caras(matrix)


if __name__ == "__main__":
    main()
