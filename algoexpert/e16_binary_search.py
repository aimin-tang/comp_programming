def search_within(array, start, end, target):
    if start > end:
        return -1

    if start == end:
        if array[start] == target:
            return start
        else:
            return -1

    mid = (start + end) // 2
    if array[mid] > target:
        return search_within(array, start, mid - 1, target)
    elif array[mid] < target:
        return search_within(array, mid + 1, end, target)
    else:
        return mid

def solve(array, target):
    start, end = 0, len(array) - 1
    return search_within(array, start, end, target)

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

print(solve(array, target))
# 3 -- as index
# note: must make progress to avoid infinite loops
