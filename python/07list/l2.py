l1 = list()
print(type(l1))
l1.append(12)
l1.append([56,8,6,8,8])
print(l1[1][1])

l2 =[]
n=int(input("ENTER THE NUMBER OF DATA :- "))
for i in range(n):
    print("Enter the ",i+1," data")
    data=input("enter the data :-")
    l2.append(data)
print(l2)