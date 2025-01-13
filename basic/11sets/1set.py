a = { 'aryan',5.1, 5}
print(a)
# set contain multiple data type but is not contain duplicate value
b = [1,4,5,6,7,3,8,9,3,2]
print(b)

c=set(b)
print(c)


# d= b.add(45)
# print(d)

e = {1,2,3,4,3,5,6}
e.remove(2)
print(e)

f = {1,2,3,4,3,5,6}
f.discard(6)
f.discard(25)
print(f)