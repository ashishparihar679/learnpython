# Write a program to print all numbers between 1 and 100 that are divisible by 7 but not divisible by 5.
# n = int(input("ENTER A NUMBER : "))
for i in range(1,101):
    if i%7==0:
        if i%5!=0:
            print(i)