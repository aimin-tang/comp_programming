def max_interval_intersec(S):
    B = ([(left, +1) for left, right in S] +
         [(right, -1) for left, right in S])
    B.sort()
    c = 0
    best = (c, None)

    for x, d in B:
        c += d
        if best[0] < c:
            best = (c, x)

    return best

print(max_interval_intersec([(2, 6), (3, 7), (4, 8)]))
