# matrix substrction

A = [[10,2,8],
     [6,1,3],
     [4,1,2]]
B = [[5,2,1],
     [1,1,1],
     [1,1,2]]

diff_matrix=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        diff_matrix[i][j] = A[i][j] - B[i][j]

print("Difference of A + B")
for i in range(3):
    for j in range(3):
        print(diff_matrix[i][j], end=" ")
    print()

