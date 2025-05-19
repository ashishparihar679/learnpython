# pettern programing using for loop
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

for i1 in range(1,6):
    for j1 in range(1,i1+1):
        print(j1,end=" ")
    print()

for i2 in range(5,0,-1):
    for j2 in range(1,i2+1):
        print(j2,end=" ")
    print()

for i3 in range(1,6):
    for j3 in range(1,i3+1):
        print(i3,end=" ")
    print()

for i4 in range(1,6):
    k=65
    for j4 in range(1,i4+1):
        print(chr(k),end=" ")
        k+=1
    print()

for i5 in range(5,0,-1):
    for j5 in range(1,i5):
        print(" ",end="")
    for k1 in range()