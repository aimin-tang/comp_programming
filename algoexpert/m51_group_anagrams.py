def groupAnagrams(words):
    # d = { (('o', 1), ('y', 1)): ['yo', oy'] }
    d = {}
    for word in words:
        letter_count_d = {}
        for l in word:
            if l not in letter_count_d:
                letter_count_d[l] = 1
            else:
                letter_count_d[l] += 1

        letter_count_l = []
        for key in letter_count_d:
            letter_count_l.append((key, letter_count_d[key]))

        key = tuple(sorted(letter_count_l))

        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]

    return list(d.values())


words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(words))