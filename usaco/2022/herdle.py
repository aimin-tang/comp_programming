def parse_input():
    # parse input of 6 lines
    grids = []
    for _ in range(2):
        grid = ''
        for _ in range(3):
            line = input().strip()
            grid += line

        grids.append(grid)

    return grids


def find_green(s1, s2):
    result = []
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result.append(i)

    return result


def exclude_green(s, green):
    result = []

    for i in range(len(s)):
        if i not in green:
            result.append(s[i])

    return result


def find_yellow(s1, s2, green):
    news1 = exclude_green(s1, green)
    news2 = exclude_green(s2, green)

    result = []
    while len(news2) > 0:
        c = news2.pop()
        if c in news1:
            idx = news1.index(c)
            result.append(c)
            news1 = news1[:idx] + news1[idx + 1:]

    return result


if __name__ == '__main__':
    s1, s2 = parse_input()
    green = find_green(s1, s2)
    print(len(green))
    yellow = find_yellow(s1, s2, green)
    print(len(yellow))
