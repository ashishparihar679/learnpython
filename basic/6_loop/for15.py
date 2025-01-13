n = int(input("enetr any number "))
even = 0
odd = 0
count_e = 0
count_o = 0
for i in range(1,n+1):
    if i%2 == 0:
        even = even + i
        count_e = count_e + 1
    else:
        odd = odd + i
        count_o = count_o + 1
print(even)
print(odd)
print(count_o)
print(count_e)
