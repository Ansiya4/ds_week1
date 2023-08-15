A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10,11,12]]
row=len(A)
col=len(A[0])
print("ORIGINAL")
for i in A:
    print(i)
A_T=[[A[i][j] for i in range(row)]for j in range(col)]
print("TRANSPOSE")
for row in A_T:
    print(row)