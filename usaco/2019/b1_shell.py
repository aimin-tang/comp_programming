from collections import defaultdict


def guess_is_good(entry, start):
    p1, p2, guess = entry

    pebble = defaultdict(bool)
    pebble[start] = True

    if start == p1:
        pebble[p1], pebble[p2] = pebble[p2], pebble[p1]
        start = p2

    elif start == p2:
        pebble[p1], pebble[p2] = pebble[p2], pebble[p1]
        start = p1

    return pebble[guess], start


def shell(in_str):
    lines = in_str.strip().split('\n')
    num = int(lines[0].strip())
    entries = []
    for i in range(1, num + 1):
        entry = list(map(int, lines[i].strip().split()))
        entries.append(entry)

    results = []

    for i in range(1, 4):
        start = i
        results_on_i = []
        for j in range(num):
            guess_result, start = guess_is_good(entries[j], start)
            results_on_i.append(guess_result)
        results.append(sum(results_on_i))

    return max(results)


if __name__ == '__main__':
    in_str = """
    3
    1 2 1
    3 2 1
    1 3 1
    """
    print(shell(in_str))
    # print(guess_is_good([1, 2, 1], 3))
