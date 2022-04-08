def runLengthEncoding(string):
    count_char_l = []

    curr_char = string[0]
    curr_count = 1

    for i in range(1, len(string)):
        if string[i] == curr_char:
            curr_count += 1
        else:
            count_char_l.append((curr_count, curr_char))
            curr_char = string[i]
            curr_count = 1

    count_char_l.append((curr_count, curr_char))

    result = []

    for count, char in count_char_l:
        while count > 9:
            result.append('9' + char)
            count -= 9
        result.append(str(count) + char)

    return ''.join(result)

print(runLengthEncoding('AAAAAAAAAAAAABBCCCCDD'))
