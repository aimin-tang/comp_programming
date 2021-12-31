def parse_input(input_str):
    lines = input_str.strip().split('\n')

    N, K = map(int, lines[0].strip().split())
    paints = []
    for i in range(N):
        line = lines[i + 1].strip()
        paints.append(list(map(int, line.strip().split())))

    return N, K, paints

def count_paint(paint):
    x1, y1, x2, y2 = paint

    for i in range(x1, x2):
        for j in range(y1, y2):
            layers[i][j] += 1

def solve():
    for paint in paints:
        count_paint(paint)

    result = 0
    for i in range(LIMIT):
        for j in range(LIMIT):
            if layers[i][j] == K:
                result += 1

    return result

if __name__ == '__main__':
    input_str = """
    3 2
    1 1 5 5
    4 4 7 6
    3 3 8 7
    """
    LIMIT = 1000
    N, K, paints = parse_input(input_str)

    layers = [[0] * LIMIT for _ in range(LIMIT)]
    print(solve())

    # testing
    # print(N, K, paints)