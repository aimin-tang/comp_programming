def get_letter_count(word):
    # "that" -> {'t':2, 'h':1, 'a':1}
    result = {}
    for l in word:
        if l not in result:
            result[l] = 1
        else:
            result[l] += 1

    return result

def minimumCharactersForWords(words):
    result = {}

    for word in words:
        letter_count = get_letter_count(word)
        for k, v in letter_count.items():
            if k not in result:
                result[k] = v
            else:
                result[k] = max(result[k], v)

    output = []
    for k, v in result.items():
        output.extend([k] * v)

    return output

words = ["this", "that", "did", "deed", "them!", "a"]
print(minimumCharactersForWords(words))