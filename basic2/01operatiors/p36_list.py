t1=(10,1.4,4+6j,True,'don')
# t1[0]=1000 TypeError: 'tuple' object does not support item assignment
t1=(10,20,30)
l1=[10,20,30]
print(t1.__sizeof__())
print(l1.__sizeof__())