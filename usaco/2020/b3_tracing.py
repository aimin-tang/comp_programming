def get_sick_cows(current_sick_cows):
    sick_cows = []

    for idx, elem in enumerate(current_sick_cows):
        # skip first:
        if idx == 0:
            continue
        if elem[0] == 1:
            sick_cows.append(idx)

    return sick_cows

def cow_is_bad(current_sick_cows, x, K):
    # return if cow x is sick and is less than K. She is bad news for
    # who touches hooves with her.
    return current_sick_cows[x][0] and current_sick_cows[x][1] < K

def update_cow(current_sick_cows, bad_cow, a_cow):
    if current_sick_cows[a_cow][0] == 0:
        current_sick_cows[a_cow] = [1, 0]
    else:
        current_sick_cows[a_cow][1] += 1

    current_sick_cows[bad_cow][1] += 1

def K_is_good(p0, K):
    # current_sick_cows format [(cow1_sick, cow1_spread), ...]
    # current_sick_cows[0] is unused.
    current_sick_cows = [None] +[[0, 0]] * N
    current_sick_cows[p0] = [1, 0]

    for trace in traces:
        t, x, y = trace
        if cow_is_bad(current_sick_cows, x, K):
            update_cow(current_sick_cows, x, y)
        elif cow_is_bad(current_sick_cows, y, K):
            update_cow(current_sick_cows, y, x)
        else:
            pass

        # see if K is already broken
        if set(get_sick_cows(current_sick_cows)).difference(set(known_sick_cows_l)):
            return False

    return get_sick_cows(current_sick_cows) == known_sick_cows_l

def solve():
    result = []
    for p0 in known_sick_cows_l:
        for K in range(0, T+1):
            if K_is_good(p0, K):
                result.append((p0, K))

        if len(result):
            return result

if __name__ == '__main__':
    input_str = """
    4 3
    1100
    7 1 2
    5 2 3
    6 2 4
    """

    lines = input_str.strip().split('\n')
    N, T = map(int, lines[0].strip().split())
    known_sick_cows = lines[1].strip()
    known_sick_cows_l = [i+1 for i in range(N) if known_sick_cows[i] == '1']
    traces = []
    for i in range(T):
        trace = lines[2 + i].strip()
        t, x, y = map(int, trace.split())
        traces.append((t, x, y))
    traces.sort()

    # test parsing:
    # print(N, T, known_sick_cows_l, traces)
    # test get_sick_cows:
    # current_sick_cows = [None, (1, 3), (1, 0), (0, 0)]
    # print(get_sick_cows(current_sick_cows))
    # test get_sick_cows:
    # print(cow_is_bad(current_sick_cows, 1, 4))

    result = solve()
    x = result[0][0]
    y = result[0][1]
    z = result[-1][1]
    if z >= T:
        z = 'Infinity'

    print(f'{x} {y} {z}')
