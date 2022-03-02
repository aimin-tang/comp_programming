import itertools
import sys


def _is_good(xg, yg, combo):
    x, y = 0, 0
    for xk, yk in combo:
        x += xk
        y += yk

    if x == xg and y == yg:
        return True

    return False


# input_str = """
# 7
# 5 10
# -2 0
# 3 0
# 4 0
# 5 0
# 0 10
# 0 -10
# 0 10
# """
input_lines = sys.stdin.readlines()
# input_lines = input_str.strip().split('\n')
N = int(input_lines[0].strip())
xg, yg = map(int, input_lines[1].strip().split())
moves = []
for idx in range(2, N + 2):
    line = list(map(int, input_lines[idx].strip().split()))
    moves.append(line)

result = []
for i in range(1, N + 1):
    count = 0
    for combo in itertools.combinations(moves, i):
        if _is_good(xg, yg, combo):
            count += 1
    result.append(count)

for n in result:
    print(n)
# print(N, xg, yg, moves)
