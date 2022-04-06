def getNthFib(n):
    if n == 1:
        return [0]

    if n == 2:
        return [0, 1]

    f = [0, 1]
    i = 3
    while i <= n:
        f.append(f[-1] + f[-2])
        i += 1

    return f

