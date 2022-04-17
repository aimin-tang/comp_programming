def parse_input(lines):
    n, t = map(int, lines[0].strip().split())
    books = list(map(int, lines[1].strip().split()))
    return n, t, books


def get_psum(books):
    total = 0
    result = [0]
    for i in range(len(books)):
        total += books[i]
        result.append(total)

    return result


def get_result(n, psum, t):
    # 0 3 4 6 7
    # [start, end] => psum[end + 1] - psum[start]
    result = 0
    for start in range(n):
        for end in range(start, n):
            if psum[end + 1] - psum[start] <= t:
                if (end - start + 1) > result:
                    result = end - start + 1
            else:
                break

    return result


input_str = """
3 3
2 2 3
"""

n, t, books = parse_input(input_str.strip().split('\n'))
print(n, t, books)
psum = get_psum(books)
result = get_result(n, psum, t)
print(result)
