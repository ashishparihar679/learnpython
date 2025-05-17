# wap to check prime number or not

n = int(input("enter number"))
i=1
while(n>0):
    if(n%i==0 and n%n==0):
        print("prime ")
        # break
    else:
        print(" not prime ")
    i=i+1
