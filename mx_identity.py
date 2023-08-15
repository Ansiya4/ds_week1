print("Enter matrix:")
mx= [[int(input()) for x in range(3)] for y in range(3)]

for i in range(3):
    for j in range(3):
        print(mx[i][j], end=" ")
    print()
flag=0
for i in range(3):
    for j in range(3):
        if i == j and mx[i][j] != 1:
            break
        elif mx[i][j] != 0:
            flag = 1
            break
if flag==1:
    print("not a identity matrix")
else:
    print("identity matrix")
