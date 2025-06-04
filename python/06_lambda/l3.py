
# REMOVE ALL THE EMPTY STRING FROM THE LIST USING filter FUNCTION

name = ["raj","","ranu","","hiresh","","aryan",""]

def mydata(lst):
    if lst=="":
        return False
    else:
        return True
mylist= filter(mydata,name)

print(list(mylist))

x = filter(lambda x: False if x=="" else True, name)
print(list(x))