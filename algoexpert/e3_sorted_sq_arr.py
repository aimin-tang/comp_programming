def sortedSquaredArray(array):
    return sorted(set([n * n for n in array]))


array = [1, 2, 3, 5, 6, 8, 9]
print(sortedSquaredArray(array))

# square all numbers in array, and sort them.