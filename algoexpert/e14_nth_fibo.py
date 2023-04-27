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

print(getNthFib(1))
# 0
print(getNthFib(2))
# 1
print(getNthFib(6))
# 5
