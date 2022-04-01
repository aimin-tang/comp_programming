def parse_input(lines):
    N = int(lines[0].strip())
    breakouts = list(map(int, lines[1].strip().split()))
    return N, breakouts

def fill_breakouts(N, breakouts):
    # based on known nums, fill as much as possible
    breakouts[0] = 0
    for day in range(1, N):
        if breakouts[day] != -1:
            # -1 -1 -1 1
            num = breakouts[day]
            i = 0
            while num > 0:
                breakouts[day - i - 1] = num - 1
                num -= 1
                i += 1


def find_min(breakouts):
    # count all 0, assume all -1 are no breakouts
    return sum([breakouts[i] == 0 for i in breakouts])

def find_max(breakouts):
    # count all 0 and -1
    return sum([breakouts[i] in [0, -1] for i in breakouts])

if __name__ == '__main__':
    input_str = """
        4
        -1 -1 -1 1
    """

    N, breakouts = parse_input(input_str.strip().split('\n'))
    fill_breakouts(N, breakouts)
    min_breakouts = find_min(breakouts)
    max_breakouts = find_max(breakouts)
    print(min_breakouts, max_breakouts)