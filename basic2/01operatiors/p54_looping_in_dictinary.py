d = {1:2,'a':'apple',4:16}
for i in d:
    print(i,end=" ")
print()

for i in d.keys():
    print(i,end=" ")
print()

for i in d.values():
    print(i,end=" ")
print()

for i in d.items():
    print(i,end=" ")
print()

for i in d:
    print(f"key:{i}, val:{d[i]}",end=" ")
print()

for i in d:
    print(i,d.get(i),end=" ")
print()