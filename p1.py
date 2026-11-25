a= int (input("a: "))
b= int (input("b: "))
c= int (input("c: "))
print(f"Before swap\n a:{a}\t b:{b}\t c:{c}")
# t=a
# a=b
# b=c
# c=t

a = a+b+c
b= a-(b+c)
c= a-(b+c)
a= a-(b+c)

print(f"After swap\n a:{a}\t b:{b}\t c:{c}")
