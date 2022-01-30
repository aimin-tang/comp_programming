def all_same(cows):
    for i in range(1, len(cows)):
        if cows[i] != cows[0]:
            return False

    return True

def feed_cows(cows, i):
    # feed cows i and i+1
    fed_cows = cows[:]
    fed_cows[i] -= 1
    fed_cows[i+1] -= 1

    return fed_cows

def is_possible(cows):
    if len(cows) == 1:
        if cows[0] == 0:
            return 0
        else:
            return -1

    if all_same(cows):
        return 0

    if any([cow<0 for cow in cows]):
        return -1

    worst_cow = max(cows)
    idx = cows.index(worst_cow)

    if idx == 0:
        r = is_possible(feed_cows(cows, 0))
        if r >= 0:
            return 2 + r
    elif idx == len(cows) - 1:
        r = is_possible(feed_cows(cows, len(cows) - 2))
        if r >= 0:
            return 2 + r
    else:
        r1 = is_possible(feed_cows(cows, idx-1))
        r2 = is_possible(feed_cows(cows, idx))
        if r1 >= 0 and r2 >= 0:
            return 2 + min(r1, r2)
        elif r1 >= 0:
            return 2 + r1
        elif r2 >= 0:
            return 2 + r2
        else:
            return -1

    return -1

if __name__ == '__main__':
    # cows = [1, 2, 1]
    # print(is_possible(cows))
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        cows = list(map(int, input().strip().split()))
        print(is_possible(cows))

