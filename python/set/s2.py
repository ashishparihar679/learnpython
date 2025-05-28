bjp={1,2,3,4}
cong={3,4,5,6}
print(bjp.intersection(cong))
print(bjp.union(cong))
s={i for i in range(10)}
print(s)
s2 = {3,5,6,7}
s3 = {3,5,6,8}
print(s2-s3)    # diffrence b/t set
print(s3-s2)
print(s3.difference(s2))

s2.remove(7)
print(s2)

# s2.remove(7)
# print(s2)

a=s2.discard(7)
print(a)
print(s2)
s2=frozenset(s2)
print(s2)