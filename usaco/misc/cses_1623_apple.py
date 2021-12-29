import itertools


def parse_input(input_str):
    lines = input_str.strip().split('\n')

    N = int(lines[0].strip())
    apples = list(map(int, lines[1].strip().split()))

    return N, apples


def solve():
    result = []
    for i in range(1, N // 2 + 1):
        for set1 in itertools.combinations(apples, i):
            set2 = set(apples).difference(set1)
            result.append((abs(sum(set1) - sum(set2)), set1, set2))

    print(min(result)[0])


if __name__ == '__main__':
    input_str = """
    5
    3 2 7 4 1
    """

    N, apples = parse_input(input_str)
    solve()

    # testing
    # print(N, apples)
    # print('============')

# itertools.combinations(a_list, a_num)

