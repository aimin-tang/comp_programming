def bubbleSort(array):
    if len(array) in [0, 1]:
        return array

    # [1, 2, 3]
    for stop in range(len(array) - 1, 0, -1):
        for start in range(stop):
            if array[start] > array[start + 1]:
                array[start], array[start + 1] = array[start + 1], array[start]

    return array
