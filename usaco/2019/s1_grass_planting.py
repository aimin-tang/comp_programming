from collections import defaultdict

def _parse_input_lines(input_lines):
    N = int(input_lines[0].strip())
    edges = []
    for idx in range(1, N):
        line = input_lines[idx]
        edges.append(tuple(map(int, line.strip().split())))

    return N, edges

def _get_degrees(edges):
    degrees = defaultdict(int)
    for from_node, to_node in edges:
        degrees[from_node] += 1
        degrees[to_node] += 1

    return degrees

def _get_grass_count(degrees):
    result = 0
    for _, degree in degrees.items():
        if degree > result:
            result = degree

    return result + 1

input_str = """
4
1 2
4 3
2 3
"""

input_lines = input_str.strip().split('\n')

N, edges = _parse_input_lines(input_lines)
degrees = _get_degrees(edges)
print(_get_grass_count(degrees))