def get_partial(s, idx):
    # get a string of identical letters
    # "aaabb"
    for i in range(idx + 1, len(s)):
        if s[i] != s[idx]:
            return s[idx] * (i - idx)

    return s[idx] * (len(s) - idx)
    
def encode_partial(s):
    # "AAA" => "3A"
    count = len(s) // 9
    remainder =len(s) % 9
    result = ""

    for _ in range(count):
        result += f"9{s[0]}"

    if remainder:
        result += f"{remainder}{s[0]}"

    return result
            
def runLengthEncoding(s):
    result = ""
    idx = 0

    while idx < len(s):
        partial = get_partial(s, idx)
        result += encode_partial(partial)
        idx += len(partial)

    return result

print(runLengthEncoding('AAAAAAAAAAAAABBCCCCDD'))
# "9A4A2B4C2D"
