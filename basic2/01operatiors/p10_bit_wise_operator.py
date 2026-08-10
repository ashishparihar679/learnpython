# We have 6 Bitwise Operators:
# &, |, ^, <<, >>, ~

# Bitwise operators work with integer operands

print(10 & 20)       # 0
print(23 & 47)       # 7

print(10 | 20)       # 30
print(17 | 27)       # 27

print(15 ^ 7)        # 8
print(24 ^ 45)       # 53

a = 1
b = a << 1
print(b)             # 2

aa = 32
print(aa >> 3)       # 4

print(~10)           # -11

# SHORT-HAND ASSIGNMENT OPERATOR

c = 10
print(c)             # 10

c = c + 5            # c += 5
print(c)             # 15