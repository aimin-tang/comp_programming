def findThreeLargestNumbers(array):
    largest3 = sorted([array[0], array[1], array[2]])
    for i in range(3, len(array)):
        if largest3[0] < array[i]:
            largest3 = sorted([largest3[1], largest3[2], array[i]])

    return largest3

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(array))
# [18, 141, 541]