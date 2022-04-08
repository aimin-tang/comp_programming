def get_prod_except(array, to_exclude):
    result = 1
    for i in range(len(array)):
        if i != to_exclude:
            result *= array[i]

    return result


def arrayOfProducts(array):
    result = []
    for i in range(len(array)):
        result.append(get_prod_except(array, i))

    return result


array = [5, 1, 4, 2]
print(arrayOfProducts(array))
