print(5+6)          # int + int = int
print(5+6.6)        # int + float = float

print(5+9+5j)       # int + int + complex = complex
print(5.3+9+5j)     # float + int + complex = complex
print(5+9j+9+5j)    # complex + int + complex = complex

print(5+'h')        # int + string = TypeError
print(5.3+'h')      # float + string = TypeError
print(5+3j+'h')     # complex + string = TypeError