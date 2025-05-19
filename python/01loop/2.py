
# wap to revese a number taken from user
n = int(input("enter number"))
rev = 0
sum =0
while(n>0):
    r = n%10
    rev = rev*10+r
    sum = sum + r
    n = n//10
print(rev)
print(sum)

