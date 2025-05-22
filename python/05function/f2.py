# def return_withoutn_argument():
#     a=13
#     return a
# x= return_withoutn_argument()
# print(x)

# def return_withoutn_argument():
#     a=13
#     b=12
#     c=56
#     d=98
#     return a,b,c,d
# x= return_withoutn_argument()
# print(x)


def return_withoutn_argument():
    a=13
    b=12
    c=56
    d=98
    return a,b,c,d
x= return_withoutn_argument()
# print(x)
sum =0
for i in x:
    sum = sum +i
    print(i)
print("sum = ",sum)