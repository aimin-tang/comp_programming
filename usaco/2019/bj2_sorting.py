def parse_input(lines):
    N = int(lines[0].strip())
    cows = list(map(int, lines[1].strip().split()))
    return N, cows


if __name__ == '__main__':
    input_str = """
    4
    1 2 3 4
    """
    N, cows = parse_input(input_str.strip().split('\n'))

    result = len(cows) - 1

    idx = result - 1

    while cows[idx] < cows[idx+1]:
        idx -= 1
        result -= 1

    print(result)

