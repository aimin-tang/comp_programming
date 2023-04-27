def shift(c, key):
    # shift c by key, handle wraps
    if ord('a') <= ord(c) <= ord('z'):
        new_ord = (ord(c) + key - ord('a')) % 26 + ord('a')
    elif ord('A') <= ord(c) <= ord('Z'):
        new_ord = (ord(c) + key - ord('A')) % 26 + ord('A')
    else:
        return c

    return chr(new_ord)

def solve(s, key):
    return "".join([shift(c, key) for c in s])

print(solve('abc', 3))
print(solve('xyz', 2))
