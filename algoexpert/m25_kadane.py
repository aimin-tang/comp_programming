def kadanesAlgorithm(array):
    sums = [array[0]]

    for i in range(1, len(array)):
        if sums[i - 1] > 0:
            sums.append(sums[i - 1] + array[i])
        else:
            sums.append(array[i])

    return max(sums)


array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanesAlgorithm(array))