def caesarCipherEncryptor(string, key):
    result = []
    for l in string:
        c = chr((ord(l) - ord('a') + key) % 26 + ord('a'))
        result.append(c)

    return ''.join(result)

print(caesarCipherEncryptor('abc', 3))
