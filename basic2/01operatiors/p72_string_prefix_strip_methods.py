# removeprefix(prefix) -> str

s = "  python"
print(s, len(s))                                    # →   python  8

# res = s.lstrip()
# print(res, len(res))                                 # → python  6

# res1 = s.removeprefix("  ")
# print(res1, len(res1))                               # → python  6

print(s.removeprefix("  "))                           # → python
print(s.removeprefix(""))                             # →   python
print(s.removeprefix(" "))                             # →  python

print("...py...".lstrip('.'))                         # → py...
print("...py...".rstrip('.').removeprefix('.'))        # → ..py

print("..#.py.#.#.".lstrip("#p"))                      # → ..#.py.#.#.
print("..#.py.#.#.".removeprefix(".#p"))                # → ..#.py.#.#.