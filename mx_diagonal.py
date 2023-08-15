# A = [[1, 2, 3],
#      [0, 0, 6],
#      [0, 8, 0]]
# row = len(A)
# col = len(A[0])
# if row == col:
#     d1 = [None]*row
#     d2 = [None]*row
#     x=y=0
#     for i in range(row):
#         for j in range(col):
#             if i==j:
#                 d1[x]=A[i][j]
#                 x+=1
#             if i+j == col-1:
#                 d2[y]=A[i][j]
#                 y+=1
#     print("Diagnonal-1:",d1)
#     print("Diagnonal-2:",d2)
# else:
#     print("Not a square matrix")

A = [[1, 0, 0],
     [0, 0, 0],
     [0, 0, 3]]
row = len(A)
col = len(A[0])
flag =0
if row==col:
    for i in range(row):
        for j in range(col):
            if i != j:
                if A[i][j] != 0:
                    flag = 1
                    break
else:
    print("not a diagonal matrix")
if flag == 0:
    print("diagonal matrix")
else:
    print("not a diagonal matrix")