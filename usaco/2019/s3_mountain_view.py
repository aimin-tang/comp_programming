def parse_input(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0].strip())
    mountains = []
    for i in range(N):
        line = lines[i+1].strip()
        x, y = map(int, line.split())
        mountains.append((x, y))

    return N, mountains

def is_hidden_by(m1, m2):
    x1, y1 = mountains[m1]
    x2, y2 = mountains[m2]

    abs_distx = abs(x1 - x2)
    return y1 <= y2 - abs_distx

def is_hidden(idx):
    for i, mountain in enumerate(mountains):
        if i == idx:
            continue
        if is_hidden_by(idx, i):
            return True
    else:
        return False

def solve():
    result = 0

    for idx in range(len(mountains)):
        if not is_hidden(idx):
            result += 1

    return result

if __name__ == '__main__':
    input_str = """
    3
    4 6
    7 2
    2 5
    """

    N, mountains = parse_input(input_str)
    print(solve())

    # testing
    # print(N, mountains)