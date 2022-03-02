def all_same(cows):
    for i in range(1, len(cows)):
        if cows[i] != cows[0]:
            return False

    return True

def is_possible(cows):
    if all_same(cows):
        return True

    for i in range(len(cows) - 1):
        if cows[i] and not cows[i+1] or not cows[i] and cows[i+1]:
            continue
        fed_cows = cows[:]
        fed_cows[i] -= 1
        fed_cows[i+1] -= 1
        return is_possible(fed_cows)

    return False

if __name__ == '__main__':
    # N = 3
    # cows = [10, 9, 9]
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        cows = list(map(int, input().strip().split()))
        print(is_possible(cows))

