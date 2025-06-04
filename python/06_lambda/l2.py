# x =lambda a,b:a if a>b else b
# print(x(60,80))

# wap to find maximum from three inut taken from user using lambda function

x =lambda a,b,c:a if a>b and a>c   else( b if b>a and b>c else c)

a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))
c = int(input("enter number 3 : "))
print(x(a,b,c))


# FILTER functionTHE FILTER FUNCTION RETURN ON ITRETION WHERE THE ITEM ARE FILTER THROW A FUNCTION TO TAST ITEMS IS ACCEPT OR NOT
# WHEN WE USING FILTER FUNCTION MINIMUM

# REMOVE ALL THE EMPTY STRING FROM THE LIST USING filter FUNCTION