row = int(input("enter number of row(m):"))
col = int(input("enter number of col(n):"))
a = [[int(input("input to A:")) for n in range(col)] for m in range(row)]
print(a)
for i in a:
    print(i)

b = [[int(input("input to B:")) for n in range(col)] for m in range(row)]
print(b)
for i in b:
    print(i)
c = [ [ 0 for n in range(col)] for m in range(row)]
for i in c:
    print(i)

for i in range(row):
    for j in range(col):
        c[i][j]= a[i][j] +b[i][j]
print("sum:")
for i in c:
    print(i)
