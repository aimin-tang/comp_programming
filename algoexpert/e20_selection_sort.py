def get_min_idx(array, idx):
    # get the index of the smallest number starting at idx
    curr_min = array[idx]
    result = idx
    for i in range(idx + 1, len(array)):
        if array[i] < curr_min:
            curr_min = array[i]
            result = i

    return result

def helper(array, idx):
    # array[:idx] is pre-sorted. now sort array[idx] in
    min_idx = get_min_idx(array, idx)
    array[idx], array[min_idx] =  array[min_idx], array[idx]

def selection_sort(array):
    if len(array) in [0, 1]:
        return array

    for idx in range(len(array) - 1):
        helper(array, idx)

array = [8, 5, 2, 9, 5, 6, 3]
selection_sort(array)
print(array)
# [2, 3, 5, 5, 6, 8, 9]
# selection sort: pick smallest number, grow into pre-sorted portion "in-place"
# [8, 5, 2, 9, 5, 6, 3]
# (no pre-sorted portion)
# [2, 5, 8, 9, 5, 6, 3]
#  -
# [2, 3, 8, 9, 5, 6, 5]
#  ----
# [2, 3, 5, 9, 8, 6, 5]
#  -------
# [2, 3, 5, 5, 8, 6, 9]
#  ----------
# [2, 3, 5, 5, 6, 8, 9]
#  -------------
# [2, 3, 5, 5, 6, 8, 9]
#  ----------------
# [2, 3, 5, 5, 6, 8, 9]
#  -------------------
