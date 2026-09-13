s = "Iron man and spiderman"
print(s.split())
# print(s)
# print(s.split('a'))
print(s.split('a',maxsplit=1))
# print(s.split('and'))

print(s.rsplit())
print(s.rsplit('a',maxsplit=1))
# print(s)