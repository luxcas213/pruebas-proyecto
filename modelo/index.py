from modelo import matrix as mx
from modelo import funciones as fn
def main():
    xy = mx.xy
    xz = mx.xz
    yz = mx.yz
    n = mx.n
    
    matrix=fn.createMatrix(xy, xz, yz, n)
    #matrix = fn.optimizarMatrix(matrix)
    vertices, faces = fn.voxel_to_mesh(matrix)
    fn.save_mesh(vertices, faces, 'output.stl')
    #fn.mostrar_voxeles(matrix)
    

if __name__ == "__main__":
    main()
