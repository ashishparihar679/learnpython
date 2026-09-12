#COUNT()

s = 'Iron man and spiderman'
# print(s.count('a'))
# print(s.count('a',9))
# print(s.count('a',9,17))
# print(s.count('x'))
# print(s.count('I'))
# print(s.count('I',4))

# print(s.count('man'))
# print(s.count('mAn'))
# print(len(s))
# print(s.count('oo'))#non over laping
# print(s.count(''))

# INDEX()
# RINDEX()
s1 = "pyspiders"

print(s1.index('s'))      # 2
print(s1.rindex('s'))     # 8

print(s1.index('d'))      # 5
print(s1.rindex('d'))     # 5

print(s1.index('sp'))     # 2
print(s1.rindex('sp'))    # 2

# print(s1.rindex('sP'))    # ValueError: substring not found
# print(s1.index('l'))      # ValueError: substring not found
# print(s1.rindex('l'))     # ValueError: substring not found
#FIND
#RFIND

s2 = "pyspiders"

print(s2.find('s'))      # 2
print(s2.rfind('s'))     # 8
print(s2.find('l'))      # -1
# print(s2.find('sP'))     # -1

s3 = "Iron man and spiderman"
print(s3.find('man'))    # 5
print(s3.find('mAn'))    # -1
