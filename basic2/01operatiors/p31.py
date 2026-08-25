# Write a program to print the multiplication table of a given number. (using for loop and while loop)
# n = int(input("ENTER A NUMBER : "))
# for i in range(1,11):
#     print(f"{n} * {i} = {i*n}" )

n = int(input("ENTER A NUMBER : "))
i=1
while(i<11):
    print(f"{n} * {i} = {i*n}" )
    i+=1
