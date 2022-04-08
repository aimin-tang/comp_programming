def get_outer_layer(array):
    if len(array) == 0:
        return []

    result = []

    if len(array) > 1 and len(array[0]) > 1:
        result.extend(array[0])
        for i in range(1, len(array) - 1):
            result.append(array[i][-1])
        result.extend(reversed(array[-1]))
        for i in range(len(array) - 2, 0, -1):
            result.append(array[i][0])
    else:
        for row in array:
            result.extend(row)

    return result

def get_inner_array(array):
    if len(array) < 3 or len(array[0]) < 3:
        return []

    result = []
    for i in range(1, len(array) - 1):
        result.append(array[i][1:-1])

    return result

def spiralTraverse(array):
    if len(array) == 0:
        return []

    result = []
    result.extend(get_outer_layer(array))
    inner = get_inner_array(array)
    result.extend(spiralTraverse(inner))

    return result

array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]

print(spiralTraverse(array))