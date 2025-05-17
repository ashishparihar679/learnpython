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
    
    

num = int(input("Enter a number: "))
i = 2

if num > 1:
    while i < num:
        if num % i == 0:
            print(num, "is not a prime number")
            break
        i += 1
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
























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
