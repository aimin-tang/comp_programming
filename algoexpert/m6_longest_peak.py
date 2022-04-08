def get_tips(array):
    # find all peak tips
    result = []
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            result.append(i)

    return result


def get_peak(array, tip):
    l = tip - 1
    r = tip + 1
    while l >= 0:
        if array[l] < array[l + 1]:
            l -= 1
        else:
            break

    while r < len(array):
        if array[r] < array[r - 1]:
            r += 1
        else:
            break

    # array: 3, 1, 2, 1, 3, tip: 2

    return l + 1, r - 1

def longestPeak(array):
    tips = get_tips(array)

    r_start, r_end = -1, -1
    longest = 0

    for tip in tips:
        start, end = get_peak(array, tip)
        if end - start + 1 > longest:
            r_start, r_end = start, end
            longest = end - start + 1

    if longest > 0:
        return array[r_start: r_end + 1]
    else:
        return []


array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(array))
