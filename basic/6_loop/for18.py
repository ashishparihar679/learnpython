n =(input("enetr any number "))
str = 0
digit = 0
special = 0
for i in n:
     if i.isdigit():
         digit = digit+1
# print(digit)
     elif i.isalpha():
          str = str +1
     else:
          special = special +1
# print(f"str is {str} digit is {digit} special character is {special}")
print("str = ",str)
print("digit = ",digit)
print("special char = ",special)
