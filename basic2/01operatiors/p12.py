n = int(input("ENTER THE NUMBER : "))
if (n>99 and n<1000) or (n<-99 and n>-1000):
    print(f"{n} is three digit number")
else:
    print(f"{n} is not three digit number")