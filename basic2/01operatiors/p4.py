print(5*6)              # int * int = int
print(5*6.0)            # int * float = float

print(5*6+6J)           # int * int + complex = complex
print(5.6*6+6J)         # float * int + complex = complex
print(5+4j*6+6J)        # int + (complex * int) + complex = complex

print(7 * 'j')          # int * string = string (repetition)
# print(7.3 * 'j')      # float * string = TypeError
# print((7+8j) * 'j')   # complex * string = TypeError
# print('j' * 7.3)      # string * float = TypeError