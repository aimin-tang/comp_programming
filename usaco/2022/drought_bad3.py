def all_same(cows):
    if len(cows) == 1:
        return True

    for i in range(1, len(cows)):
        if cows[i] != cows[0]:
            return False

    return True

def feed_cows(cows, i, b):
    # feed cows i and i+1, each with b bags
    fed_cows = cows[:]
    fed_cows[i] -= b
    fed_cows[i+1] -= b

    return fed_cows

def is_possible(cows):
    if all_same(cows):
        return 0

    if any([cow < 0 for cow in cows]):
        return -1

    most_hungry = max(cows)
    idx = cows.index(most_hungry)

    if idx == 0:
        diff = max(cows[0] - cows[1], 1)
        r = is_possible(feed_cows(cows, 0, diff))
        if r >= 0:
            return 2 + r
    elif idx == len(cows) - 1:
        diff = max(cows[-1] - cows[-2], 1)
        r = is_possible(feed_cows(cows, len(cows) - 2, diff))
        if r >= 0:
            return 2 + r
    else:
        diff1 = max(cows[idx] - cows[idx-1], 1)
        diff2 = max(cows[idx] - cows[idx+1], 1)
        if diff1 > diff2:
            r1 = is_possible(feed_cows(cows, idx-1, diff1))
            r2 = is_possible(feed_cows(cows, idx, diff2))
        else:
            r2 = is_possible(feed_cows(cows, idx, diff2))
            r1 = is_possible(feed_cows(cows, idx - 1, diff1))
        if r1 >= 0 and r2 >= 0:
            if r1 >= r2:
                return 2 * diff2 + r2
            else:
                return 2 * diff1 + r1
        elif r1 >= 0:
            return 2 * diff1 + r1
        elif r2 >= 0:
            return 2 * diff2 + r2
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
