def parse_input(lines):
    N, Q = map(int, lines[0].strip().split())
    breeds = []
    for i in range(1, N + 1):
        line = lines[i].strip()
        breeds.append(int(line.strip()))
    queries = []
    for i in range(N + 1, N + Q + 1):
        b, e = map(int, lines[i].strip().split())
        queries.append((b, e))

    return N, Q, breeds, queries


if __name__ == '__main__':
    input_str = """
    6 3
    2
    1
    1
    3
    2
    1
    1 6
    3 3
    2 4
    """

    N, Q, breeds, queries = parse_input(input_str.strip().split('\n'))
    # print(N, Q, breeds, queries)

    psum_breeds = [(0, 0, 0)]
    total = [0, 0, 0]
    for breed in breeds:
        total[breed - 1] += 1
        psum_breeds.append(total[:])

    for b, e in queries:
        print(psum_breeds[e][0] - psum_breeds[b - 1][0],
              psum_breeds[e][1] - psum_breeds[b - 1][1],
              psum_breeds[e][2] - psum_breeds[b - 1][2],
              )
