from collections import defaultdict

def _parse_input_lines(input_lines):
    N, M = map(int, input_lines[0].strip().split())
    adjs = defaultdict(list)
    for idx in range(1, M+1):
        from_node, to_node = map(int, input_lines[idx].strip().split())
        adjs[from_node-1].append(to_node-1)
        adjs[to_node-1].append(from_node-1)

    return N, M, adjs

def _assign_grass(N, adjs):
    grass_l = [1 for _ in range(N)]
    for i in range(N):
        for neighbor in adjs[i]:
            if neighbor <= i:
                # this was considered already
                continue
            if grass_l[neighbor] != grass_l[i]:
                # no need to adjust
                continue
            grass_l[neighbor] = grass_l[i] + 1

    return grass_l

input_str = """
5 6
4 1
4 2
4 3
2 5
1 2
1 5
"""

input_lines = input_str.strip().split('\n')

N, M, adjs = _parse_input_lines(input_lines)
print(N, M, adjs)
print(_assign_grass(N, adjs))
