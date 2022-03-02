import itertools
import sys


def _parse_input(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0].strip())
    prefs = []
    for num in range(1, N+1):
        line = lines[num].strip()
        pref_l = list(map(int, line.split()))
        pref_l = [n-1 for n in pref_l]
        prefs.append(pref_l)

    return N, prefs

def _is_better(perm, N, prefs):
    # permutation (such as [0, 2, 1, 3]) is better than original
    for idx in range(N):
        gift = perm[idx]
        gift_rank = prefs[idx].index(gift)
        idx_rank = prefs[idx].index(idx)
        if gift_rank > idx_rank:
            return False

    return True

# input_str = """
# 4
# 1 2 3 4
# 1 3 2 4
# 1 2 3 4
# 1 2 3 4
# """
# print(_parse_input(input_str))
# N, prefs = _parse_input(input_str)
# print(_is_better([0, 2, 1, 3], N, prefs))
# print(_is_better([0, 3, 2, 1], N, prefs))

N = int(sys.stdin.readline().strip())
prefs = []
for _ in range(N):
    line = sys.stdin.readline().strip()
    pref_l = list(map(int, line.split()))
    pref_l = [n - 1 for n in pref_l]
    prefs.append(pref_l)

for perm in itertools.permutations(range(N), N):
    if tuple(perm) == tuple([i for i in range(N)]):
        continue
    if _is_better(perm, N, prefs):
        for i in perm:
            print(i+1)
