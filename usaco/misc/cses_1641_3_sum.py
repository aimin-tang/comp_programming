def get_indexed_array(array):
    result = []
    for idx, num in enumerate(array):
        result.append((num, idx))
    result.sort()
    return result

def get_2_sums(indexed_array, idx1, target):
    result = []
    start, end = 0, len(indexed_array) - 1
    while start < end:
        if start == idx1:
            start += 1
        elif end == idx1:
            end -= 1
        else:
            n2 = indexed_array[start][0]
            idx2 = indexed_array[start][1]
            n3 = indexed_array[end][0]
            idx3 = indexed_array[end][1]
            if n2 + n3 == target:
                result.append([idx2, idx3])
                start += 1
                end -= 1
            elif n2 + n3 < target:
                start += 1
            else:
                end -= 1

    return result

def find_3_sum(n, target, array):
    indexed_array = get_indexed_array(array)
    # [(2, 0), (3, 3), (5, 2), (7, 1)]
    result = set()
    for idx1 in range(n - 2):
        diff = target - indexed_array[idx1][0]
        two_sums = get_2_sums(indexed_array, idx1, diff)
        if len(two_sums):
            for idx2, idx3 in two_sums:
                result.add(tuple(sorted([indexed_array[idx1][1] + 1,
                                         idx2 + 1, idx3 + 1])))

    return result

n, target = 4, 8
array = [2, 7, 5, 1]
print(find_3_sum(n, target, array))