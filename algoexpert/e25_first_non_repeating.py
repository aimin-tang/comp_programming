from collections import defaultdict

def firstNonRepeatingCharacter(string):
    c_count = defaultdict(int)
    for c in string:
        c_count[c] += 1

    for i in string:
        if c_count[string[i]] == 1:
            return i

    return -1

