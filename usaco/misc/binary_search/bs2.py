def b_search(array, n):
    l, r = 0, len(array) - 1
    ans = -1

    while l <= r:
        mid = (l + r) // 2
        if array[mid] >= n:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans

# find smallest number that's bigger than 3
array = [1, 2, 3, 4, 5]
print(b_search(array, 3))
