# d={} #<class 'dict'>
# print(type(d))
# d1={1,2,2} #<class 'dict'>
# print(type(d1)) #<class 'set'>

d={'a':100,2:200,3:300,4:400}
print(d)
# print(d[2])

# d[2]=211  # UPDATE
# print(d[2])

# d[5]=500  # CREATE
# print(d[5])

# del d[3]
# print(d)

# for i in d:
#     print(d[i])

# or


# for i in d.values(): # default d.key
#     print(i)

# help(dict) 

a = [1,2,3,4,5]

b=a # deap copy = if be change in b the same changes are apply in a

b[0]=100
print(a)

c=a.copy() #cello copy = if be change in b the same changes are apply only in c

c[0]=200
print(c)