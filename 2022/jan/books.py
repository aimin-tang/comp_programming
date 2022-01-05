def parse_input(input_str):
    lines = input_str.strip().split('\n')
    n, t = map(int, lines[0].strip().split())
    books = list(map(int, lines[1].strip().split()))

    return n, t, books

def solve():
    result = 0

    for i in range(n):
        curr_n, curr_t, curr_pos = 0, 0, i
        while curr_t < t and curr_pos < n:
            curr_t += books[curr_pos]
            curr_n += 1
            if curr_t > t:
                result = max(result, curr_n - 1)
                break
            elif curr_t == t:
                result = max(result, curr_n)
                break
            else:
                curr_pos += 1
                result = max(result, curr_pos - i)

    return result

if __name__ == '__main__':
    input_str = """
    4 5
    3 1 2 1
    """
    n, t, books = parse_input(input_str)

    # testing
    print(n, t, books)
    print(solve())