s = "Iron \nman and \nspiderman"
s1 ="Iron \nman and \nspiderman"

print(s)
# print(s.splitlines())
print(s1.split())

# split()                                                    splitlines()
# Splits by separator (default: space).                   Splits by newline characters.
# Returns a list of words.                                Returns a list of lines.
# Can use separator and maxsplit.                         Can use keepends.