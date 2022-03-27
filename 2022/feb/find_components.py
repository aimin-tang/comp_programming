from collections import defaultdict

def _parse_input_lines(input_lines):
    N = int(input_lines[0].strip())
    E = int(input_lines[1].strip())
    adjs = defaultdict(list)
    for idx in range(2, E+2):
        from_node, to_node = map(int, input_lines[idx].strip().split())
        adjs[from_node].append(to_node)
        adjs[to_node].append(from_node)

    return N, E, adjs

def _dfs(adjs, colors, color, node):
    if node in colors:
        return

    colors[node] = color

    for neighbor in adjs[node]:
        _dfs(adjs, colors, color, neighbor)

def find_colors(N, adjs):
    color = -1
    colors = {}

    for i in range(1, N+1):
        if i not in colors:
            color += 1
            _dfs(adjs, colors, color, i)

    return max(colors.values()) + 1

input_str = """
5
3
1 2
4 3
2 3
"""

input_lines = input_str.strip().split('\n')

N, E, adjs = _parse_input_lines(input_lines)
print(N, E, adjs)
print(find_colors(N, adjs))
