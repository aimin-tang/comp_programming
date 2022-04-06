def selectionSort(array):
    if len(array) in [0, 1]:
        return array

    min_num = min(array)
    min_idx = array.index(min_num)

    return [array[min_idx]] + selectionSort(array[:min_idx] + array[min_idx+1:])

array = [8, 5, 2, 9, 5, 6, 3]
print(selectionSort(array))