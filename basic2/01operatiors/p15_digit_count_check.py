n = int(input("enter number :"))
if -10<n<10:
    print(f"{n} is 1 digit number")
elif -100<n<-9 or 9<n<100:
    print(f"{n} is 2 digit number")
elif -1000<n<-99 or 99<n<1000:
    print(f"{n} is 3 digit number")
else:
    print(f"{n} is more than 3 digit number")

    