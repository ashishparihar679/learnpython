n=int(input("enter number"))
if n%3==0:
    print(f"{n} divisible by 3")
elif n%5==0:
    print(f"{n} divisible by 5")
elif n%7==0:
    print(f"{n} divisible by 7")
else:
    print(f"{n} is not divisible by 3,5, 7")