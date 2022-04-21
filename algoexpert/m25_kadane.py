def kadanesAlgorithm(array):
    ends_at_sums = [array[0]]

    for i in range(1, len(array)):
        if ends_at_sums[i - 1] > 0:
            ends_at_sums.append(ends_at_sums[i - 1] + array[i])
        else:
            ends_at_sums.append(array[i])

    return max(ends_at_sums)


array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanesAlgorithm(array))

# what's the largest sum that "ends at" idx - dynamic programming
# array:          3, 5, -9, 1, 3, -2, 3, 4,  7,  2, -9, 6,  3,  1, -5,  4
# ends_at_sums:   3, 5, -1, 1, 4,  2, 5, 9, 16, 18, 9, 15, 18, 19, 14, 18