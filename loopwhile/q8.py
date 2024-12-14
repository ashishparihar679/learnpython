n1 = int(input("enter number 1 "))
n2 = int(input("enter number 2 "))
if n1>n2:
    while n1>n2:
        if n2%2==0:
            print(n2)
            n2= n2+1
else:
     while n1<n2:
        if n1%2==0:
            print(n1)
            n1= n1+1