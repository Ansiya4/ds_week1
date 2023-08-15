def determinant(matrix):
    n = len(matrix)
    if n ==1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for j in range(n):
        sign = (-1)**j
        sub_matrix = [[matrix[i][k] for k in range(n) if k!=j] for i in range(1,n) ]
        print("aaaa")
        for i in sub_matrix:
            print(i)
        sub_det = determinant(sub_matrix)
        det += sign * matrix[0][j] * sub_det
        print(det)
    return det
A = [[1, 2, -3],
     [4, 5, -6],
     [7, 8, -9],
     ]
print(".....",determinant(A))
B =[[1,2],
    [2,5]]
print(determinant(B))
