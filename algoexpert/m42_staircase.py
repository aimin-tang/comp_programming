def staircaseTraversal(height, maxSteps):
    # 0   1   2   3   4
    # 1   1   2   3   5
    if height in [0, 1]:
        return 1

    dpl = [1, 1]
    for _ in range(2, height + 1):
        dpl.append(0)

    for i in range(2, maxSteps):
        dpl[i] = sum(dpl[:i])

    for i in range(maxSteps, height + 1):
        dpl[i] = sum(dpl[i - maxSteps:i])

    return dpl[-1]

print(staircaseTraversal(4, 2))


