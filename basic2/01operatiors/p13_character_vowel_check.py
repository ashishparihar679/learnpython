n = input("ENTER THE CHARACTER : ")
val = ord(n)
print(val)
val2 = chr(val)
# if(val2=='a' or val2=='e' or val2=='i' or val2=='o' or val2=='u' or val2=='A' or val2=='E' or val2=='I' or val2=='O' or val2=='U'):
if n in "aeiouAEIOU":
    print(f"{n} is vowel")
else:
    print(f"{n} is not vowel")