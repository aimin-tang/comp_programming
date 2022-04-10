def maxSubsetSumNoAdjacent(array):
    # corner cases
    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return max(array[0], array[1])

    num1, num2 = array[0], max(array[0], array[1])
    for i in range(2, len(array)):
        curr_sum = max(num2, num1 + array[i])
        num1 = num2
        num2 = curr_sum

    return num2


array = [75, 105, 120, 75, 90, 135]
print(maxSubsetSumNoAdjacent(array))