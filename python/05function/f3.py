
def return_withoutn_argument(a,b,c,d):
    
    return a,b,c,d
x= return_withoutn_argument(5,8,9,6)
# print(x)
sum =0
for i in x:
    sum = sum +i
    print(i)
print("sum = ",sum)

# note
# when we decleare the function with having same 
# name but pasing paramer is diffrent this concept
#  is non as function overoating and python is
#  dynamically typed so function overloading shut not supported in python

# types of argument 
