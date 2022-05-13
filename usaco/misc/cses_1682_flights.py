from collections import defaultdict


def get_adjs(n, flights):
    adjs = defaultdict(list)
    for ff, ft in flights:
        adjs[ff].append(ft)

    return adjs

def dfs(start, adjs, visited):
    if start in visited:
        return
    visited.append(start)
    for adj in adjs[start]:
        dfs(adj, adjs, visited)

def get_missed(visited, n):
    for i in range(1, n + 1):
        if i not in visited:
            return i

def cannot_reach(n, flights):
    adjs = get_adjs(n, flights)

    for ff in range(1, n + 1):
        visited = []
        dfs(ff, adjs, visited)
        if len(visited) < n:
            return (ff, get_missed(visited, n))
        else:
            print('good: from {}'.format(ff))

n, m = 4, 5
flights = [(1, 2), (2, 3), (3, 1), (1, 4), (3, 4)]
print(cannot_reach(n, flights))