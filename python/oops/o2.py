n = int(input("Enter a number : "))
a=0
b=1
# for i in range(n):
i=0
while(i<n):
    print(a,end=" ")
    t=a+b
    a=b
    b=t
    i+=1