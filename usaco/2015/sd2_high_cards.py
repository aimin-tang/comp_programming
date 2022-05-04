def get_bessie(N, elsie):
    bessie = []
    for i in range(1, 2 * N + 1):
        if i not in elsie:
            bessie.append(i)
    return bessie


def get_b_idx(e_card, bessie):
    idx = 0

    while idx < len(bessie):
        if bessie[idx] > e_card:
            return idx
        else:
            idx += 1

    return -1


def solve(N, elsie):
    bessie = get_bessie(N, elsie)
    bessie.sort()
    result = 0

    for e_card in elsie:
        b_idx = get_b_idx(e_card, bessie)
        if b_idx >= 0:
            result += 1
            bessie = bessie[:b_idx] + bessie[b_idx + 1:]
        else:
            bessie = bessie[1:]

    return result


N = 3
elsie = [1, 6, 4]
print(solve(N, elsie))
