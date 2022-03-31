import itertools


def parse_input(lines, cow_d):
    N = int(lines[0].strip())

    constraints = []
    for i in range(1, N + 1):
        line = lines[i]
        words = line.strip().split()
        cow1 = cow_d[words[0]]
        cow2 = cow_d[words[-1]]
        constraints.append((cow1, cow2))

    return N, constraints


def get_cow_l_d():
    cow_l = 'Bessie Buttercup Belinda Beatrice Bella Blue Betsy Sue'.split()
    cow_l.sort()

    cow_d = {}
    for idx, cow in enumerate(cow_l):
        cow_d[cow] = idx

    return cow_l, cow_d


def is_good(perm, constraints):
    for cow1, cow2 in constraints:
        if abs(perm.index(cow1) - perm.index(cow2)) > 1:
            return False
    return True


def output_cows(perm, cow_l):
    for n in perm:
        print(cow_l[n])


lines = """
3
Buttercup must be milked beside Bella
Blue must be milked beside Bella
Sue must be milked beside Beatrice
"""
cow_l, cow_d = get_cow_l_d()
N, constraints = parse_input(lines.strip().split('\n'), cow_d)
perms = itertools.permutations(range(8))
for perm in perms:
    if is_good(perm, constraints):
        output_cows(perm, cow_l)
        break

