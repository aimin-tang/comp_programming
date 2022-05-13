from collections import defaultdict


def get_adjs(cows):
    adjs = defaultdict(list)
    for cow1 in range(len(cows)):
        for cow2 in range(len(cows)):
            if cow2 == cow1:
                continue
            x1, y1, p1 = cows[cow1]
            x2, y2, p2 = cows[cow2]
            if (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) <= p1 * p1:
                adjs[cow1 + 1].append(cow2 + 1)

    return adjs


def dfs(adjs, start, visited):
    if start in visited:
        return
    visited.append(start)
    for adj in adjs[start]:
        dfs(adjs, adj, visited)


def get_reached(adjs, start):
    visited = []
    dfs(adjs, start, visited)

    return visited


def solve(cows):
    adjs = get_adjs(cows)
    best = (0, 0)

    for start in range(1, len(cows) + 1):
        reached = get_reached(adjs, start)
        if len(reached) > best[1]:
            best = (start, len(reached))

    return best


cows = [(1, 3, 5), (5, 4, 3), (7, 2, 1), (6, 1, 1)]
print(solve(cows))
