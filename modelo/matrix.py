import numpy as np
n=30
matrix = [[[1 for _ in range(n)] for _ in range(n)] for _ in range(n)]

def create_garba_matrix(n):
    # Asegurarse de que n sea lo suficientemente grande
    if n < 27:
        raise ValueError("n debe ser al menos 27 para contener la palabra 'Garba' con espacios entre letras")

    # Matrices 5x5 para cada letra
    G = np.array([
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ])

    A = np.array([
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1]
    ])

    R = np.array([
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1, 0]
    ])

    B = np.array([
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0]
    ])

    # Matriz de espacio entre letras
    space = np.zeros((5, 1))

    # Combinamos las letras con espacios en una sola matriz
    garba = np.concatenate((G, space, A, space, R, space, B, space, A), axis=1)

    # Crear una matriz n x n de ceros
    matrix = np.zeros((n, n), dtype=int)

    # Colocar la palabra "Garba" en el centro de la matriz n x n
    start_row = (n - 5) // 2
    start_col = (n - garba.shape[1]) // 2

    matrix[start_row:start_row+5, start_col:start_col+garba.shape[1]] = garba
   
    return matrix

def create_lucas_matrix(n):
    # Asegurarse de que n sea lo suficientemente grande
    if n < 27:
        raise ValueError("n debe ser al menos 27 para contener la palabra 'Lucas' con espacios entre letras")

    # Matrices 5x5 para cada letra
    L = np.array([
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0]
    ])

    U = np.array([
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ])

    C = np.array([
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
    ])

    A = np.array([
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1]
    ])

    S = np.array([
        [0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0]
    ])

    # Matriz de espacio entre letras
    space = np.zeros((5, 1))

    # Combinamos las letras con espacios en una sola matriz
    lucas = np.concatenate((L, space, U, space, C, space, A, space, S), axis=1)

    # Crear una matriz n x n de ceros
    matrix = np.zeros((n, n), dtype=int)

    # Colocar la palabra "Lucas" en el centro de la matriz n x n
    start_row = (n - 5) // 2
    start_col = (n - lucas.shape[1]) // 2

    matrix[start_row:start_row+5, start_col:start_col+lucas.shape[1]] = lucas

    return matrix


def cuadrado(n):
    x = [[1 for _ in range(n)] for _ in range(n)]
    return x

def circulo(n):
    x = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i - n//2)**2 + (j - n//2)**2 <= (n//2)**2:
                x[i][j] = 1
    return x

def triangulo(n):
    x = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i <= n//2 and j <= i and j >= n//2 - i:
                x[i][j] = 1
            elif i > n//2 and j >= i - n//2 and j <= n - i + n//2 - 1:
                x[i][j] = 1
    return x

xy =cuadrado(n)

xz =triangulo(n)

yz =triangulo(n)
    