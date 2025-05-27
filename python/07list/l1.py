# l = [12,67,45,69,87,63]
l = [60, 50, 14, 82, 14, 7, 3]
x=len(l)
print(x)
for i in range(x):
    for j in range(i+1,x):
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
            # temp = l[i]
            # l[i] = l[j]
            # l[j] = temp
print(l)