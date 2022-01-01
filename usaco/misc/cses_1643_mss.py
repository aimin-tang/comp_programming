def parse_input(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0].strip())
    arr = list(map(int, lines[1].strip().split()))

    return n, arr


def build_prefix_sum(arr):
    # psum[i+1] = arr[1] + ... + arr[i]
    result = [0]
    current_sum = 0

    for elem in arr:
        current_sum += elem
        result.append(current_sum)

    return result


def solve():
    # arr[i] + ... arr[j] = psum[j] - psum[i-1]
    rsum, rfrom, rto = 0, 0, 0
    curr_from, curr_low = 0, 0

    for idx in range(1, n+1):
        curr_sum = psum[idx]
        if curr_sum - curr_low > rsum:
            rsum = curr_sum - curr_low
            rfrom = curr_from
            rto = idx
        elif curr_sum < curr_low:
            curr_low = curr_sum
            curr_from = idx + 1

    return rsum, rfrom, rto


if __name__ == '__main__':
    input_str = """
    8
    -1 3 -2 5 3 -5 4 2
    """
    n, arr = parse_input(input_str)
    psum = build_prefix_sum(arr)
    print(solve())

    # testing
    # print(n, arr)
    # print(build_prefix_sum(arr))
