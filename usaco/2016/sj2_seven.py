def parse_input(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0].strip())
    cows = [int(line.strip()) for line in lines[1:]]

    return N, cows


def build_psum(cows):
    # psum for i is right before cow i is included.
    # length is N + 1
    curr_sum = 0
    psum = [0]

    for idx, cow in enumerate(cows):
        curr_sum += cows[idx]
        psum.append(curr_sum)

    return psum


def build_psum_remainder_d(psum):
    remainder_d = {k: [] for k in range(7)}

    for idx, sum in enumerate(psum):
        remainder_d[sum % 7].append(idx)

    return remainder_d

def solve(remainder_d):
    result = 0

    for i in range(7):
        if len(remainder_d[i]) < 2:
            continue
        result = max(result, remainder_d[i][-1] - remainder_d[i][0])

    return result



if __name__ == '__main__':
    input_str = """
    7
    3
    5
    1
    6
    2
    14
    10
    """
    N, cows = parse_input(input_str)
    psum = build_psum(cows)
    remainder_d = build_psum_remainder_d(psum)
    print(solve(remainder_d))

    # testing
    # print(parse_input(input_str))
    # print(build_psum(cows))
    # psum = build_psum(cows)
    # print(build_psum_remainder_d(psum))

# best to do psum as "i included"
# eg: A=[2, 5, 7, 1, 4], P = [2. 7, 14, 15, 19]
