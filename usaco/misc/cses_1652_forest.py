def star_to_coords(line, i):
    result = []
    for j in range(len(line)):
        if line[j] == '*':
            result.append((i, j + 1))

    return result


def star_to_array(line):
    result = [char == '*' for char in line]

    return result


def parse_input(input_str):
    lines = input_str.strip().split('\n')
    n, q = map(int, lines[0].strip().split())

    trees = []
    for i in range(n):
        line = lines[i + 1].strip()
        trees_i = star_to_array(line)
        trees.append(trees_i)

    queries = []
    for i in range(q):
        line = list(map(int, lines[n + i + 1].strip().split()))
        queries.append(line)

    return n, q, trees, queries

def count(query):
    result = 0

    y1, x1, y2, x2 = query
    for tree in trees[y1-1:y2]:
        result += sum(tree[x1-1:x2])

    return result

if __name__ == '__main__':
    input_str = """
    4 3
    .*..
    *.**
    **..
    ****
    2 2 3 4
    3 1 3 1
    1 1 2 2
    """
    n, q, trees, queries = parse_input(input_str)

    for query in queries:
        print(count(query))

    # testing
    # print(star_to_coords('**..', 3))
    # print(star_to_array('**..'))
    # print(n, q, trees, queries)
    # print(count([1, 1, 2, 2]))
