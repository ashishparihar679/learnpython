# WRITE APROGRAM TO FIND A FACTORIAL NUMBER OF A NUMBER INPUT TAKING FROM THE USER

ans = 1
sum = 0
num = int (input("enter number :- "))
i =1
while(i<=num):
    ans = ans *i
    sum = sum +i
    i = i+1
print(f"FACTORIAL {ans}")
print(f"SUM {sum}")
