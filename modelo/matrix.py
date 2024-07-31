n=3
matrix = [[[1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
""" 

xy = [[1 if (i > 2 and i < 7 and j > 2 and j < 7) else 0 for j in range(n)] for i in range(n)]

xz = [[1 if (i > 2 and i < 7 and j > 2 and j < 7) else 0 for j in range(n)] for i in range(n)]

yz = [[1 if (i > 2 and i < 7 and j > 2 and j < 7) else 0 for j in range(n)] for i in range(n)]

 """
xy = [[1,1,1],
      [1,0,1],
      [1,1,1]]

xz = [[1,1,1],
      [1,0,1],
      [1,1,1]]

yz = [[1,1,1],
      [1,0,1],
      [1,1,1]]
