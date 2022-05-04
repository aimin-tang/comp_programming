def solve(cows):
    cows = reversed(sorted(cows))
    waiting = []

    for cow in cows:
        if cow < len(waiting):
            continue
        else:
            waiting.append(cow)

    return len(waiting)

cows = [7, 1, 400, 2, 2]
print(solve(cows))