n1=int(input("enter number 1 "))
n2=int(input("enter number 2 "))
n3 = n1+1
i= 1
while(i<=n2):
    temp=n3
    rev = 0
    while(temp>0):
        r = temp%10
        rev = rev*10+r
        temp = temp // 10
    if(rev == n3):
        print("palindrom",rev)
        i +=1
    n3 +=1