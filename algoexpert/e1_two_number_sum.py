from collections import defaultdict


def get_arr_d(array):
    arr_d = defaultdict(list)
    for idx, num in enumerate(array):
        arr_d[num].append(idx)
    return arr_d


def twoNumberSum(array, targetSum):
    arr_d = get_arr_d(array)
    for num, idx_l in arr_d.items():
        diff = targetSum - num
        if diff in arr_d:
            if diff == num:
                if len(arr_d[num]) > 1:
                    return [num, diff]
            else:
                return [num, diff]

    return [None, None]


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))

# find 2 numbers in array that add up to targetSum.
# [-1, 11] (reverse order is fine)
# 1. n ** 2: 2 rounds of for loops.
# 2. nlgn: sort, then two pointers.
# 3. n: store "seen" list. one for loop.
# 4. n: get_idx_arr(). can report index
