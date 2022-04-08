import math


def smallestDifference(arrayOne, arrayTwo):
    # [-1, 3, 5, 10, 20, 28]
    # [15, 17, 26, 134, 135]
    arrayOne.sort()
    arrayTwo.sort()

    sdiff = math.inf
    p1, p2 = 0, 0
    spair = []
    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        n1 = arrayOne[p1]
        n2 = arrayTwo[p2]
        if n1 < n2:
            curr_diff = n2 - n1
            p1 += 1
        elif arrayOne[p1] > arrayTwo[p2]:
            curr_diff = n1 - n2
            p2 += 1
        else:
            return [n1, n2]

        if sdiff > curr_diff:
            sdiff = curr_diff
            spair = [n1, n2]

    return spair

arrayOne = [-1, 3, 5, 10, 20, 28]
arrayTwo = [15, 17, 26, 134, 135]
print(smallestDifference(arrayOne, arrayTwo))
