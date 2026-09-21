s = "  python  "
print(s, len(s))                                    # →   python   10

res = s.lstrip()
print(res, len(res))                                 # → python   8

res1 = s.rstrip()
print(res1, len(res1))                               # →   python 8

p = "..#..py..#..#.".lstrip('.')
p = "..#..py..#..#.".rstrip('.')

print("..#..py..#..#.".lstrip('#'))                  # → ..#..py..#..#.
print("..#..py..#..#.".rstrip('#'))                  # → ..#..py..#..#.

print("..#..pyp.#..#.".lstrip('.#p'))                 # → yp.#..#.
print("..#..pyp.#..#.".rstrip('.#p'))                 # → ..#..py

print("..#..py.#..#.".lstrip(None))                  # → ..#..py.#..#.
print("..#..py.#..#.".rstrip(None))                  # → ..#..py.#..#.

print("  py  ".lstrip(None))                          # → py  
print("  py  ".rstrip(None))                          # →   py