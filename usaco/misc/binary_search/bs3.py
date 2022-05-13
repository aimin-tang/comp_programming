def b_search(array):
    # [3, 4, 5, 1, 2]
    #  F  F  F  T  T
    l, r = 0, len(array) - 1
    ans = -1

    while l <= r:
        mid = (l + r) // 2
        if array[mid] <= array[-1]:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans

# find the smallest on a sorted -> rotated array
array = [3, 4, 5, 1, 2]
print(b_search(array))