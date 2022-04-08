def get_two_sums(array_d, n1, targetSum):
    result = set()
    for n2, i2 in array_d.items():
        if n2 == n1:
            continue
        diff = targetSum - n2
        if diff in [n1, n2]:
            continue

        if diff in array_d:
            result.add(tuple(sorted((n2, diff))))

    return result


def threeNumberSum(array, targetSum):
    result = set()
    array.sort()

    array_d = {}
    for idx, num in enumerate(array):
        array_d[num] = idx

    for n1 in array:
        diff = targetSum - n1
        two_sums = get_two_sums(array_d, n1, diff)
        for n2, n3 in two_sums:
            result.add(tuple(sorted([n1, n2, n3])))

    return sorted([list(s) for s in result])


array = [12, 3, 1, 2, -6, 5, -8, 6]
print(threeNumberSum(array, 0))
