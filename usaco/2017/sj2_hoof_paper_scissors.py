def parse_input(lines):
    N = int(lines[0].strip())
    fj_l = []
    for i in range(1, N + 1):
        fj_l.append(lines[i].strip())

    return N, fj_l


def bessie_game(fj, bessie):
    # given fj and bessie, see if bessie gets 1 point or not.
    if (fj == 'H' and bessie == 'P') or (fj == 'P' and bessie == 'S') \
            or (fj == 'S' and bessie == 'H'):
        return True
    else:
        return False


def bessie_games(fj_l, bessie_l):
    result = 0
    for i in range(len(fj_l)):
        if bessie_game(fj_l[i], bessie_l[i]):
            result += 1
    return result


def get_bessie_l(N, b1, b2, change):
    # return bessie_l. there is one change
    # ex: HHPPP. N: 5, b1: H, b2: P, change: 2
    result = [b1 for _ in range(change)]
    for i in range(change, N):
        result.append(b2)
    return result


if __name__ == '__main__':
    input_str = """
    5
    P
    P
    H
    P
    S
    """
    N, fj_l = parse_input(input_str.strip().split('\n'))
    # print(N, fj_l)
    best = 0
    for b1 in ['H', 'P', 'S']:
        for b2 in ['H', 'P', 'S']:
            if b1 == b2:
                continue
            for change in range(N):
                bessie_l = get_bessie_l(N, b1, b2, change)
                r = bessie_games(fj_l, bessie_l)
                best = max(best, r)
                # print(b1, b2, change, best, r)

    print(best)
