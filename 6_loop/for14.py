n = int(input("enetr any number "))
even = 0
odd = 0
for i in range(1,n+1):
    if i%2 == 0:
        even = even + i
    else:
        odd = odd + i
print(even)
print(odd)
