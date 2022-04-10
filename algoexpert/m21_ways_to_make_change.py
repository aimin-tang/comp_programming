def numberOfWaysToMakeChange(n, denoms):
    result = [1] + [0 for _ in range(n)]

    for denom in denoms:
        for i in range(1, n + 1):
            if i < denom:
                continue
            else:
                result[i] += result[i - denom]

    return result[-1]

print(numberOfWaysToMakeChange(8, [1, 2, 4, 8]))
