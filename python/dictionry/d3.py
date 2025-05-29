d={'100':"a",'200':"value2"}
print(d.get('100'))
print(d.items())
for i,j in d.items():
    print(i,"_____",j)
d1=d.copy()
print(d1)
d.clear()
print(d)