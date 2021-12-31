def parse_input(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0])
    A = list(lines[1].strip())
    B = list(lines[2].strip())

    return N, A, B

def flip_it(s):
    result = []
    for l in s:
        if l == 'G':
            result.append('H')
        else:
            result.append('G')

    return result

def sub_solve(a, b):
    # solve for a and b
    start, end = 0, len(a) - 1

    # find first place of mismatch
    for i in range(len(a)):
        if a[i] != b[i]:
            start = i
            break
    else:
        # all are same
        return 0

    # find last place of mismatch
    for i in range(len(a) - 1, start - 1, -1):
        if a[i] != b[i]:
            end = i
            break

    if end - start < 2:
        return 1

    shorter_a = a[start: end+1]
    shorter_b = b[start: end+1]

    return sub_solve(shorter_a, flip_it(shorter_b)) + 1

def solve():
    return sub_solve(A, B)


if __name__ == '__main__':
    input_str = """
    7
    GHHHGHH
    HHGGGHH
    """
    N, A, B = parse_input(input_str)
    # print(solve())

    same_or_not = [x != y for x, y in zip(A, B)]

    # testing:
    # print(parse_input(input_str))
