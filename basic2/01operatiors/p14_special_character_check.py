n = input("ENTER THE CHARACTER : ")

if not n.isalnum():
    print(f"{n} is a special character")
else:
    print(f"{n} is not a special character")