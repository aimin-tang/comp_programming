def firstDuplicateValue(array):
    for num in array:
        num = abs(num)
        if array[num - 1] < 0:
            return num
        else:
            array[num - 1] = - array[num - 1]

    return -1

array = [2, 1, 5, 3, 3, 2, 4]
print(firstDuplicateValue(array))