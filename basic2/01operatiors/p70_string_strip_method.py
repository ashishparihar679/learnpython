s="     pyhton     "
print(s,len(s))
res=s.strip()
print(res)
print(res,len(res))

print("..#..py.#..#.".strip('.'))
print("..#..py.#..#.".strip('#'))
print("..#..py.#..#.".strip('#p'))
print("..#..pyp.#..#.".strip(None))
print("    pyp    ".strip(None))