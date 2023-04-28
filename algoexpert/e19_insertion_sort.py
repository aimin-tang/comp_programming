def handle_idx(array, idx):
    # array[:idx] is already pre-sorted. now handle array[idx]
    for i in range(idx - 1, -1, -1):
        if array[i + 1] < array[i]:
            array[i], array[i + 1] = array[i + 1], array[i]
        else:
            break

def insertion_sort(array):
    if len(array) in [0, 1]:
        return array

    for idx in range(1, len(array)):
        handle_idx(array, idx)

array = [8, 5, 2, 9, 5, 6, 3]
insertion_sort(array)
print(array)
# [2, 3, 5, 5, 6, 8, 9]
# insertion sort: grow "pre-sorted" array.
# [8, 5, 2, 9, 5, 6, 3]
#  -
# [5, 8, 2, 9, 5, 6, 3]
#  ----
# [2, 5, 8, 9, 5, 6, 3]
#  -------
# [5, 2, 8, 9, 5, 6, 3]
#  ----------
# [2, 5, 5, 8, 9, 6, 3]
#  -------------
# [2, 5, 5, 6, 8, 9, 3]
#  ----------------
# [2, 3, 5, 5, 6, 8, 9]
#  -------------------
# then second largest, etc ...
