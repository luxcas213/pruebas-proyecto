from modelo import matrix as mx
from modelo import funciones as fn

def main():
    n = 100
    xy = mx.cuadrado(n)
    xz = mx.triangulo(n)
    yz = mx.circulo(n)
    
    matrix=fn.generar_piramide_booleana(n)
    
    # matrix = fn.optimizarMatrix(matrix)
    # fn.voxel_to_mesh(matrix)
    # fn.mostrar_voxeles(matrix)
    graph=fn.newoctahedrongraph()
    fn.GenerarMeshFromGraph(graph)

if __name__ == "__main__":
    main()
