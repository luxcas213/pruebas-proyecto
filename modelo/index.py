from modelo import matrix as mx
from modelo import funciones as fn

def main():
    xy = mx.xy
    xz = mx.xz
    yz = mx.yz
    n = mx.n
    
    matrix=fn.createMatrix(xy, xz, yz, n)
    
    # # matrix = fn.optimizarMatrix(matrix)
    fn.voxel_to_mesh(matrix)
    # #fn.mostrar_voxeles(matrix)
    # graph=fn.newcubegraph()
    # fn.GenerarMeshFromGraph(graph)

if __name__ == "__main__":
    main()
