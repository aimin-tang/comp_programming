def settle_last(array, idx):
    # go from the beginning, settle the last number till idx.
    for i in range(idx):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

def bubble_sort(array):
    if len(array) in [0, 1]:
        return array

    for idx in range(len(array) - 1, 0, -1):
        settle_last(array, idx)

array = [8, 5, 2, 9, 5, 6, 3]
bubble_sort(array)
print(array)
# [2, 3, 5, 5, 6, 8, 9]
# bubble sort: first round bubbles the lagest in place
# [8, 5, 2, 9, 5, 6, 3]
# [5, 8, 2, 9, 5, 6, 3]
# [5, 2, 8, 9, 5, 6, 3]
# [5, 2, 8, 9, 5, 6, 3]
# [5, 2, 8, 5, 9, 6, 3]
# [5, 2, 8, 5, 6, 9, 3]
# [5, 2, 8, 5, 6, 3, 9]
# then second largest, etc ...
