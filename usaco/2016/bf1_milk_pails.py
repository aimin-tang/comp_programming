def can_solve(target, X, Y):
    if target < 0:
        return False

    if target == 0:
        return True

    return can_solve(target - X, X, Y) or can_solve(target - Y, X, Y)

def solve(X, Y, M):
    for target in range(M, -1, -1):
        if can_solve(target, X, Y):
            return target

X, Y, M = 17, 25, 77
print(solve(X, Y, M))