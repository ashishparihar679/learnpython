# wap to nummber reverse
n = int(input("enter number"))
r = 0
while n!=0:
    digit=n%10
    r =(r*10)+digit
    n=n //10
print(r)