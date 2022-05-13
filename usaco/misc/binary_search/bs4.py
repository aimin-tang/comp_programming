def b_search(array):
    # [1, 2, 3, 4, 3, 2, 1]
    #  F  F  F  T  T  T  T
    # handle corner cases
    if len(array) in [0, 1]:
        return -1

    if array[0] > array[1]:
        return 0

    if array[-1] > array[-2]:
        return len(array) - 1

    # regular cases
    l, r = 0, len(array) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if array[mid] > array[mid + 1]:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans


array = [1, 2, 3, 4, 3, 2, 1]
print(b_search(array))
