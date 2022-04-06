import math

def helper(array, depth):
    result = 0
    for elem in array:
        if isinstance(elem, int):
            result += math.factorial(depth) * elem
        elif isinstance(elem, list):
            result += helper(elem, depth + 1)
        else:
            raise RuntimeError('Unknown type')

    return result

def productSum(array):
    return helper(array, 1)

array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))