n = int (input("enter number"))
if(n==0):
    print("zero")
elif(n<0):
    print("negetive")
else:
    print("positive")
    if(n%2==0):
        print("even")
    else:
        print("odd")