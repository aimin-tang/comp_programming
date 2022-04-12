def validIPAddresses(string):
    result = []

    for i in range(1, min(len(string), 4)):
        parts = ["", "", "", ""]
        parts[0] = string[:i]
        if not is_valid_part(parts[0]):
            continue

        for j in range(i + 1, i + min(len(string) - i, 4)):
            parts[1] = string[i:j]
            if not is_valid_part(parts[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):
                parts[2] = string[j:k]
                parts[3] = string[k:]

                if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                    result.append(".".join(parts))

    return result

def is_valid_part(string):
    if int(string) > 255:
        return False

    return len(string) == len(str(int(string)))





string = "1921680"
print(validIPAddresses(string))
