a = int (input("enter 1 side length "))
b = int (input("enter 2 side length "))
c = int (input("enter 3 side length "))
if(a==b and b==c and c==a):
    print("equlateral triangle")
elif(a==b or b==c or c==a ):
    print("isoscceles triangle")
else:
    print("scalene triangle")
