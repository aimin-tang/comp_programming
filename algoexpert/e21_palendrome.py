def is_same(c1, c2):
    return c1.lower() == c2.lower()

def should_skip(c):
    # if c should be skipped, such as a space
    return c in [" ", "\t"]

def look_right(s, idx):
    # from idx going to the right, skip to the index for real char
    # "a  "
    while idx < len(s):
        if not should_skip(s[idx]):
            return idx
        else:
            idx += 1

    return idx

def look_left(s, idx):
    # from idx going to the left, skip to the index for real char
    # "  a"
    while idx >= 0:
        if not should_skip(s[idx]):
            return idx
        else:
            idx -= 1

    return idx

def isPalindrome(s):
    i, j = 0, len(s) - 1
    # "a  a"

    while True:
        i = look_right(s, i)
        j = look_left(s, j)
        if i >= j:
            return True
        if not is_same(s[i], s[j]):
            return False
        else:
            i += 1
            j -= 1

s = "abcdcba"
print(isPalindrome(s))
# True

# "abc".reverse() doesn't work! list is okay.
# reversed("abc") gives a reversed object. need to do "".join().
