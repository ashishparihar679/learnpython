v=[]
c=[]
n=int(input("enter the number of character:-"))
for i in range(n):
    print("enter the",i+1,"chraecter")
    data = input("enter the character ")
    data1 = data.lower()
    if(data=='a'):
        v.append(data1)
    else:
        c.append(data1)
print("vowel ",v)
print("consunant ",c)
