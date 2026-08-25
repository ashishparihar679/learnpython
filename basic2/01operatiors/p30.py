# Write a program to find the sum of the first N natural numbers(using for loop and while loop) 

# n = int(input("ENTER A NUMBER : "))
# sum =0
# for i in range(1,n+1):
#     sum +=i
# print(sum)

n = int(input("ENTER A NUMBER : "))
sum=0
i=1
while(i<n+1):
    sum +=i
    i+=1
print(sum)
