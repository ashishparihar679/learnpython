number = int(input("enter a number"))
if number<=100 and number>=90:
    print("grade A")
elif number<90 and number>=80:
    print("grade B")
elif number<80 and number>=70:
    print("grade C")
elif number<70 and number>=60:
    print("grade D")
elif number<60:
    print("number below 60... ")
else:
    print("numbe is above 100... ")

# if number >= 90:
#     print("grade A")
# elif number >= 80:
#     print("grade B")
# elif number >= 70:
#     print("grade c")
# elif number >= 60:
#     print("grade d")
# else:
#     print("below 60")