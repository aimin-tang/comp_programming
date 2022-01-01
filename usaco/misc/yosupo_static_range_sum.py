def parse_input(input_str):
    lines = input_str.strip().split('\n')
    N, Q = map(int, lines[0].strip().split())
    A = list(map(int, lines[1].strip().split()))

    queries = []
    for i in range(Q):
        line = lines[i + 2].strip()
        f, t = tuple(map(int, line.split()))
        queries.append((f, t))

    return N, Q, A, queries

def build_prefix_sum(A):
    result = []
    current_sum = 0

    for elem in A:
        current_sum += elem
        result.append(current_sum)

    return result

def solve(prefix_sum):
    result = []
    for f, t in queries:
        if f == 0:
            result.append(prefix_sum[t - 1])
        else:
            result.append(prefix_sum[t-1] - prefix_sum[f-1])

    return result


if __name__ == '__main__':
    input_str = """
    5 5
    1 10 100 1000 10000
    2 3
    0 3
    2 5
    3 4
    0 5
    """
    N, Q, A, queries = parse_input(input_str)
    prefix_sum = build_prefix_sum(A)
    print(solve(prefix_sum))


    # testing
    # print(N, Q, A, queries)
    # print(build_prefix_sum(A))