# python Exception an exception can we defined as anussual conditon in a program resulting in the intreption in flow of the program whenewer and Exception occures the the program stop 

# an exception is the run time error that are anable to handle python script
# and exception in a python is an object that represent an error there is two type of error 
# 1. syntax error
# 2. logical error


a = int(input("enter number 1 : "))
b = int(input("enter number 2 : "))

try:
    c=a/b
    # print(c)
except:
    print("zero se divide nhi hoga")
else:
    print(c)
finally:
    print("ye to chalega hi")


# common exception 
# python provide  the number of exception but her be are discuss 
# a list of common exception that can throw 

# na me error when a name is not defined or found it may we local or globle
# in detation error 
