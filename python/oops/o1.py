n = int(input("enter a number : "))
t = n
a = n%10
n=n//10
b=n%10
n=n//10
s=(a**3)+(b**3)+(n**3)
if(t==s):
    print("armstram")
else:
    print("not armstram")