print(9-6)              # int - int = int
print(9-6.5)            # int - float = float

print(9-6+6j)           # int - int + complex = complex
print(9.3-6+6j)         # float - int + complex = complex
print((9+5j)-(6+6j))    # complex - complex = complex

print(7-'j')            # int - string = TypeError
print(7.3-'j')          # float - string = TypeError
print(7+8j-'j')         # complex - string = TypeError
print('s' - 'j')    # string - string = TypeError