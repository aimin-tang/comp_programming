def parse_input(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0].strip())

    cows = []
    for i in range(N):
        arrive, duration = list(map(int, lines[i+1].strip().split()))
        cows.append((arrive, duration))

    return N, sorted(cows)

def solve():
    t = 0

    for cow in cows:
        t = max(cow[0], t)
        t += cow[1]

    return t

if __name__ == '__main__':
    input_str = """
    3
    2 1
    8 3
    5 7
    """

    N, cows = parse_input(input_str)
    print(solve())

    # testing
    # print(N, cows)
