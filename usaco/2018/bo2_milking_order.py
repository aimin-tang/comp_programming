def parse_input(lines):
    N, M, K = map(int, lines[0].strip().split())

    hierarchy = list(map(int, lines[1].strip().split()))
    # reverse hierarchy:
    r_hierarchy = reversed(hierarchy)

    fixed = []
    for i in range(2, K + 2):
        cow, pos = map(int, lines[i].strip().split())
        # start from 0
        fixed.append((cow, pos - 1))

    return N, M, K, r_hierarchy, fixed


def fill_fixed(order, fixed):
    for cow, pos in fixed:
        order[cow] = pos


def fill_w_hierarchy(N, order, r_hierarchy):
    last = N - 1
    for cow in r_hierarchy:
        if order[cow] != -1:
            # Fill as late as possible
            last = order[cow]
        else:
            order[cow] = last
        last -= 1


def find_cow1(N, order):
    for i in range(N):
        if i not in order.values():
            # convert back to start at 1
            return i + 1


if __name__ == '__main__':
    input_str = """
        6 3 2
        4 5 6
        5 3
        3 1
    """

    N, M, K, r_hierarchy, fixed = parse_input(input_str.strip().split('\n'))

    order = {i + 1: -1 for i in range(N)}

    fill_fixed(order, fixed)
    fill_w_hierarchy(N, order, r_hierarchy)
    print(find_cow1(N, order))
