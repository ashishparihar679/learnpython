s="hello sam" #HeLL@Sa
print(s)

d = {'h':'H','l':'L','o':'@','m':''}
# d = {'h':'H','l':'L','o':'@','m':''}
# d = {'h':'H','l':'L','o':'@','m':''}

table=str.maketrans(d)
print(table)

trans=s.translate(table)
print(trans)