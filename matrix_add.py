# matrix addition 

A = [[1,2,3],
     [2,1,3],
     [4,1,2]]
B = [[5,2,1],
     [1,1,5],
     [1,1,2]]

sum_matrix=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        sum_matrix[i][j] = A[i][j] + B[i][j]

print("Sum of A + B")
for i in range(3):
    for j in range(3):
        print(sum_matrix[i][j], end=" ")
    print()

