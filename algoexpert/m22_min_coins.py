import math

def minNumberOfCoinsForChange(n, denoms):
    result = [0] + [math.inf for _ in range(n)]

    for denom in sorted(denoms):
        for i in range(1, n + 1):
            if i < denom:
                continue
            if result[i - denom] + 1 < result[i]:
                result[i] = result[i - denom] + 1

    if result[n] is math.inf:
        return -1

    return result[n]

print(minNumberOfCoinsForChange(135, [39, 45, 130, 40, 4, 1, 60, 75]))
#   0   1   2   3   4   5   6   7   8    <= n
#   0   1   2   3   4   5   6   7   8    <= after 1c
#   0   1   1   2   2   3   3   4   4    <= after 2c
#   0   1   1   2   1   2   2   3   2    <= after 4c
#   0   1   1   2   1   2   2   3   1    <= after 8c
