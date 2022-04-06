def insert_into(array, idx):
    # insert array[idx] into previous numbers
    # assume previous numbers are sorted
    i = 0
    num = array[idx]
    while i < idx:
        if array[i] < num:
            i += 1
        else:
            array[i:idx + 1] = [num] + array[i:idx]
            break

def insertionSort(array):
    if len(array) in [0, 1]:
        return array

    for start in range(1, len(array)):
        insert_into(array, start)

array = [8, 5, 2, 9, 5, 6, 3]
insertionSort(array)
print(array)
