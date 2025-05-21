n1=int(input("enter number 1 "))
n2=int(input("enter number 2 "))
n3 = n1+1
i= 1
while(i<=n2):
    temp=n3
    cout = 0
    i=1
    while(temp>0):
        if(temp%i==0):
            cout +=1
        i +=1
    if(cout == 2):
        print("palindrom",rev)
    n3 +=1