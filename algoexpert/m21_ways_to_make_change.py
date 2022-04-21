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
#  0   1   2   3   4   5   6   7   8   <= n
#  1   1   1   1   1   1   1   1   1   <= after 1c
#  1   1   2   2   3   3   4   4   5   <= after 2c
#  1   1   2   2   4   4   6   6   9   <= after 4c
#  1   1   2   2   4   4   6   6  10   <= after 8c
