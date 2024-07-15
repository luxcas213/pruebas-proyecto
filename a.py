import mostrar





def main():
    matrix = [
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ],
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ],
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ],
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
    ]

    xy = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]

    xz = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1]
    ]

    yz = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]

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

    mostrar.mostrar(matrix)
    mostrar.mostrar_caras(matrix)


if __name__ == "__main__":
    main()
