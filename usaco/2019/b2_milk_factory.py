def parse_input(lines):
    N = int(lines[0].strip())
    adjs = {}

    for n in range(1, N):
        line = lines[n].strip()
        s_from, s_to = map(int, line.split(' '))
        s_from -= 1
        s_to -= 1
        # build adjs in reverse
        if s_to in adjs:
            adjs[s_to].append(s_from)
        else:
            adjs[s_to] = [s_from]

    return N, adjs


def reachable(s):
    result = [False for _ in range(N)]

    def dfs(s):
        if result[s]:
            return
        result[s] = True
        if s in adjs:
            for s_from in adjs[s]:
                dfs(s_from)

    dfs(s)
    return result


def solve():
    for i in range(N):
        if all(reachable(i)):
            return i + 1
    return -1


lines = """
3
1 2
3 2
"""

N, adjs = parse_input(lines.strip().split('\n'))
print(solve())
