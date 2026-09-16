# Python join() Practice (All Examples)

# Syntax
# separator.join(iterable)

# 1. Join with space
words = ["Hello", "World", "Python"]
print(" ".join(words))
# Output: Hello World Python

# 2. Join with hyphen
fruits = ["apple", "banana", "mango"]
print("-".join(fruits))
# Output: apple-banana-mango

# 3. Join with no separator
letters = ["P", "Y", "T", "H", "O", "N"]
print("".join(letters))
# Output: PYTHON

# 4. Join a tuple
colors = ("Red", "Green", "Blue")
print(", ".join(colors))
# Output: Red, Green, Blue

# 5. Join after split()
text = "I love Python"
words = text.split()
print("-".join(words))
# Output: I-love-Python

# 6. Join with custom separator
items = ["HTML", "CSS", "JavaScript"]
print(" | ".join(items))
# Output: HTML | CSS | JavaScript

# 7. Join characters of a string
name = "Python"
print("-".join(name))
# Output: P-y-t-h-o-n

# 8. Wrong example (Integers)
numbers = [1, 2, 3]
# print(",".join(numbers))
# Output: TypeError (join() works only with strings)

# 9. Correct way for integers
numbers = [1, 2, 3]
print(",".join(map(str, numbers)))
# Output: 1,2,3

# 10. Join with newline
lines = ["First", "Second", "Third"]
print("\n".join(lines))
# Output:
# First
# Second
# Third

# 11. Join with *
symbols = ["A", "B", "C"]
print("*".join(symbols))
# Output: A*B*C

# 12. Join an empty list
data = []
print(" ".join(data))
# Output: ''

# 13. Join a single element


# 14. Join numbers with custom separator
marks = [85, 90, 78]
print(" | ".join(map(str, marks)))
# Output: 85 | 90 | 78

# 15. Interview Example (Initials)
name = "Bat Man"
initials = "".join(word[0].upper() for word in name.split())
print(initials)
# Output: BM

