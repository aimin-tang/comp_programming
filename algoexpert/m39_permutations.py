def getPermutations(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [array]

    partial_results = getPermutations(array[:-1])
    results = []
    for partial_result in partial_results:
        for i in range(len(partial_result) + 1):
            c = partial_result[:]
            c.insert(i, array[-1])
            results.append(c)

    return results

print(getPermutations([1, 2, 3]))