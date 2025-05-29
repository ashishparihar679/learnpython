d={}
n=int(input("enter the number of data :- "))
for i in range(n):
    print(f"enter the {i+1} data :-")
    k=input("enter the keys :- ")
    v=input("enter the valus :- ")
    d[k]=v
print(d)
d1={100:"a",200:"200"}
d2={100:"hello",200:"bhopal",300:"hiresh"}
d1.update(d2)
print(d1)
d1.pop(100)
print(d1)
d1.popitem()
print(d1)