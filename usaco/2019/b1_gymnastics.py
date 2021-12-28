import itertools


def is_consistent(i, j):
    diffs = [ranks[k][i-1] - ranks[k][j-1] for k in range(K)]
    i_is_better = all([diff<0 for diff in diffs])
    i_is_worse = all([diff>0 for diff in diffs])

    return i_is_better or i_is_worse

def gymnastics():
    result = []
    for c in itertools.combinations(range(1, N+1), 2):
        result.append((is_consistent(*c), c))

    return result

if __name__ == '__main__':
    input_str = """
    3 4
    4 1 2 3
    4 1 3 2
    4 2 1 3
    """

    lines = [line.strip() for line in input_str.strip().split('\n')]
    ranks = []
    K, N = map(int, lines[0].split())
    for i in range(1, K+1):
        ranks.append(list(map(int, lines[i].split())))

    print(gymnastics())

