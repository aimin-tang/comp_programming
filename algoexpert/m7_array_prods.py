def get_left_prod(array):
    # [5, 1, 4, 2]
    # [1, 5, 5, 20]
    result = [1]
    curr_prod = 1

    for i in range(1, len(array)):
        curr_prod *= array[i - 1]
        result.append(curr_prod)

    return result


def arrayOfProducts(array):
    left_prod = get_left_prod(array)
    # [1, 5, 5, 20]
    # [8, 40, 10, 20]
    curr_prod = 1
    result = left_prod[:]
    for i in range(len(array) - 1, -1, -1):
        result[i] = left_prod[i] * curr_prod
        curr_prod *= array[i]

    return result


array = [5, 1, 4, 2]
print(arrayOfProducts(array))
