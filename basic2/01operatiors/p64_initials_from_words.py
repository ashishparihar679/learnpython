l=['Bat Man']
#  l=['BM']
l1=[]
for i in l:
    r =''
    s=i.split()
    for j in s:
        r=r+j[0].upper()
    l1.append(r)
print(l1)

