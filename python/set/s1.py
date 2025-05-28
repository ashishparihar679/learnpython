# when we wnat to reprensent a group of entity
# into and single entitiy where insertion order is not presarved and only hytrogenus object is to be allowed then we can iplent the set 
# note 
# set is muteble

s = {51,55,1,5,11,6,1,15,5,1,52,1,1,7,2,1}
print(s)
print(type(s))
x=s.pop()
print(x)
print(s)
s.add("hello")
print(s)
r=s.remove(55)
print(s)
# print(r)
s.update([52,8,999])
print(s)
s2=s.copy()
print(s)
s.clear()
print(s)
print(s2)