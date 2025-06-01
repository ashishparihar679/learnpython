# t1=(9,5,7,2,9.2,8,6,4)
# print(type(t1))
# t2=list(t1)
# print(t2)
# t2.append(3)
# print(t2)
# t1=tuple(t2)
# print(t1)

t1=(9,5,7,2,9,2,8,6,4)
t2=list(t1)
print(t2)
t3 = []
for i in t2:
    if i%2!=0:
        t3.append(i)
print(t3)
