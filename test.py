a =  [[1,2,3],
      [1,2,3],
      [1,2,3],
      [1,2,3]]
for i in a:
    print(i)
row = len(a)
col = len(a[0])
a_T=[[a[i][j] for i in range(row)] for j in range(col)]
for i in a_T:
    print(i)
