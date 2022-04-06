def helper(array, i, j, target):
    if i == j:
        if array[i] == target:
            return i
        else:
            return -1

    mid = (i + j) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return helper(array, i, mid - 1, target)
    else:
        return helper(array, mid + 1, j, target)


def binarySearch(array, target):
    return helper(array, 0, len(array) - 1, target)
