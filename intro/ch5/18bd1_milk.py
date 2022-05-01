import copy


def find_repeats(sizes, filled):
    s1, s2 = -1, -1
    cache = [(3, 4, 5)]

    for i in range(100):
        from_idx = i % 3
        to_idx = (i + 1) % 3

        transfer = min(sizes[to_idx] - filled[to_idx], filled[from_idx])
        filled[to_idx] += transfer
        filled[from_idx] -= transfer
        if tuple(filled) in cache:
            return cache.index(tuple(filled)), len(cache)
        else:
            cache.append(tuple(filled))


def get_equivalent(s1, s2, N):
    cycle = s2 - s1
    return s1 + (N - s1) % cycle


def solve(sizes, filled):
    # sizes: [10, 11, 12]
    # filled: [3, 4, 5]
    filled_copy = copy.copy(filled)
    s1, s2 = find_repeats(sizes, filled_copy)
    if s1 == -1:
        end = 100
    else:
        end = get_equivalent(s1, s2, 100)

    for i in range(end):
        from_idx = i % 3
        to_idx = (i + 1) % 3

        transfer = min(sizes[to_idx] - filled[to_idx], filled[from_idx])
        filled[to_idx] += transfer
        filled[from_idx] -= transfer

    return filled


sizes = [10, 11, 12]
filled = [3, 4, 5]

print(solve(sizes, filled))
# print(find_repeats(sizes, filled))
