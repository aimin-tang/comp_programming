import bisect


def parse_input(input_str):
    lines = input_str.strip().split('\n')
    n, sum = map(int, lines[0].strip().split())
    arr = list(map(int, lines[1].strip().split()))

    return n, sum, arr

def solve():
    p1 = 0    # next number to try from the beginning
    p2 = len(new_arr) - 1   # next number to try from end

    while p1 < p2:
        if new_arr[p1][0] + new_arr[p2][0] > sum:
            p2 -= 1
        elif new_arr[p1][0] + new_arr[p2][0] == sum:
            result = [new_arr[p1][1] + 1, new_arr[p2][1] + 1]
            return ' '.join(map(str, sorted(result)))
        else:
            p1 += 1
    else:
        return 'IMPOSSIBLE'


if __name__ == '__main__':
    input_str = """
    4 8
    2 7 5 1
    """

    n, sum, arr = parse_input(input_str)
    new_arr = [(val, idx) for idx, val in enumerate(arr)]
    new_arr.sort()
    # print(n, sum, arr)
    # print(new_arr)
    print(solve())
