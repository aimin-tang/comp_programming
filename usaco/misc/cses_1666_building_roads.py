from collections import defaultdict


def dfs(city, adjs, visited):
    if city in visited:
        return

    visited.append(city)

    for adj in adjs[city]:
        dfs(adj, adjs, visited)


def get_adjs(n, roads):
    adjs = defaultdict(list)
    for a, b in roads:
        adjs[a].append(b)
        adjs[b].append(a)

    return adjs


def get_new_roads(partitions):
    result = []
    if len(partitions) <= 1:
        return []

    for i in range(1, len(partitions)):
        p1 = partitions[i - 1]
        p2 = partitions[i]
        result.append((p1[0], p2[0]))

    return result


def solve(n, m, roads):
    all_cities = set([i + 1 for i in range(n)])
    covered = set()
    not_covered = all_cities - covered
    partitions = []

    adjs = get_adjs(n, roads)

    while len(not_covered):
        start = not_covered.pop()
        visited = []
        dfs(start, adjs, visited)
        covered.update(set(visited))
        not_covered.difference_update(set(visited))
        partitions.append(list(visited))

    new_roads = get_new_roads(partitions)
    return new_roads


n, m = 4, 2
roads = [(1, 2), (3, 4)]
print(solve(n, m, roads))
