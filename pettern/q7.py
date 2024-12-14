# n = int (input("enter number"))
n=5
for i in range(n):
    for j in range(n):
        # if(j==0 and i<2) or (j==2 and i!=2) or (i==2) or (i==0 and j>2) or (i==4 and j<2) or (j==4 and i>2):
        if(j==0 and i<2) or (j==2):
         print("* ",end=" ")
        else:
            print("  ",end=" ")
    print()
    