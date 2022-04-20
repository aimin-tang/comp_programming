import math


def get_earliest(curr_cows):
    earliest_end = math.inf
    result = (-1, -1)

    for cow in curr_cows:
        if cow[0] + cow[1] < earliest_end:
            earliest_end = cow[0] + cow[1]
            result = cow

    return result


def get_end(curr_cows):
    return max([cow[0] + cow[1] for cow in curr_cows])


def get_duration(cows, k):
    t = 0
    curr_cows = []
    # [(0, 4), (0, 7)] => [(0, 7), (4, 8)] => [(4, 8), (7, 6)] =>
    # [(7, 6), (12, 4)] => [(12, 4)]

    for cow in cows:
        if len(curr_cows) == k:
            earliest = get_earliest(curr_cows)
            t = earliest[0] + earliest[1]
            idx = curr_cows.index(earliest)
            curr_cows = curr_cows[:idx] + curr_cows[idx + 1:]
        curr_cows.append((t, cow))

    return get_end(curr_cows)


def solve(cows, T):
    if get_duration(cows, 1) <= T:
        return 1
    if get_duration(cows, len(cows)) > T:
        return math.inf

    l, r = 1, len(cows)
    while l < r - 1:
        mid = (l + r) // 2
        if get_duration(cows, mid) <= T:
            r = mid
        else:
            l = mid

    if get_duration(cows, l) <= T:
        return l
    else:
        return l + 1


cows = [4, 7, 8, 6, 4]
(solve(cows, 8))
