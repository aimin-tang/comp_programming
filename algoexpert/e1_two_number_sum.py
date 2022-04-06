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
