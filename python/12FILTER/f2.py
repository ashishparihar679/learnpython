

# ecception hendling

# resing exception = an ecception can be rest forcefully by using the resclose in python it is usefull in that senerio where we need to rase an exception too stop the excution of the program 
# iof error = end of file error
# 
try:
    age=int(input("enter your age : ")) 
    if(age<=0):
        raise ValueError
    elif(age<18):
        print("valid age  for voting ")

    else:
        print("valid age")

except ValueError:
    print("value no valid",ValueError)