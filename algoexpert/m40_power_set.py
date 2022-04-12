def powerset(array):
    if len(array) == 0:
        return [[]]

    partial_results = powerset(array[:-1])
    results = []
    for partial_result in partial_results:
        results.append(partial_result[:])
        results.append(partial_result[:] + [array[-1]])

    return results

array = [1, 2, 3]
print(powerset(array))

