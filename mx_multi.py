a = [[1,2,3],
     [1,1,1]]
b = [[1],
     [2],
     [3]]
row_a= len(a)
col_a=len(a[0])
row_b= len(b)
col_b=len(b[0])

if col_a==row_b:
    c=[[0 for i in range(col_b)] for j in range(row_a)]
for i in range(row_a):
        for j in range(col_b):
            for k in range(row_b):
                c[i][j] += a[i][k]*b[k][j]

for i in c:
    print(i) 