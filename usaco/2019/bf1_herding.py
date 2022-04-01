def parse_input(line):
    a, b, c = map(int, line.strip().split())
    return sorted([a, b, c])

def find_min(a, b, c):
    if c == a + 2:
        # one next to each other: 1, 2, 3
        return 0

    if (b - a) == 2 or (c - b) == 2:
        # 1, 5, 7 -> 5, 6, 7 in one step
        return 1

    # all rest can be done in 2 steps
    # 1, 5, 9 -> 5, 7, 9 -> 5, 6, 7
    return 2

def find_max(a, b, c):
    # find biggest gap, be as frugal as possible
    return max((b - a), (c - b)) - 1


if __name__ == '__main__':
    line = "4 7 9"
    a, b, c = parse_input(line.strip())

    print(find_min(a, b, c))
    print(find_max(a, b, c))
