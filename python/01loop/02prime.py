# n=int(input("ENTER A NUMBER "))
# i=2
# if n>1:
#    while(n>i):
#         ifn%i==0:
#             print(f"THE NUMBER IS NOT PRIME :- {n}")
#             break
#         i += 1
#     else:
#          print(f"THE NUMBER IS PRIME :- {n}")
# else:
#     print(f"THE NUMBER IS NOT PRIME :- {n}")
    
    

# num = int(input("Enter a number: "))
# i = 2

# if num > 1:
#     while i < num:
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#         i += 1
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")



# n = int(input("ENTER THE NUMBER :- "))
# i=1
# cnt =0
# while(i<=n):
#     if(n%i==0):
#         cnt += 1
#         i+=1
#     if(cnt==2): 
#         print("PRIME")
#     else:
#         print("NOT PRIME")

# n = int(input("ENTER THE NUMBER :- "))
# i=1
# cnt =0
# while(i<=n):
#     if(n%i==0):
#         cnt += 1
#     i+=1
# if(cnt==2): 
#    print("PRIME")
# else:
#    print("NOT PRIME")


n=int(input("enter number : "))
i=1
cnt=0
while(n>=i):
    if(n%i==0):
       cnt+=1
      #  print(n)
    i+=1

if(cnt==2):
   print("prime")
else:
   print("not prime")
   




















# num = int(input("Enter a number: "))

# # Prime number is greater than 1
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")
