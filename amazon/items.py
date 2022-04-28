import math


def trim_to_compartment(s, start_idx, end_idx):
    result_start, result_end = math.inf, -math.inf

    idx = start_idx
    while idx < end_idx + 1:
        if s[idx] == '|':
            result_start = idx
            break
        else:
            idx += 1

    idx = end_idx
    while idx >= start_idx:
        if s[idx] == '|':
            result_end = idx
            break
        else:
            idx -= 1

    return result_start, result_end


def get_item_count_l(s):
    item_count_l = []
    curr_count = 0
    for i in range(len(s)):
        if s[i] == '*':
            curr_count += 1
        item_count_l.append(curr_count)

    return item_count_l


def numberOfItems(s, startIndices, endIndices):
    if len(startIndices) != len(endIndices):
        raise RuntimeError("indices lengths don't match")

    item_count_l = get_item_count_l(s)

    result = []
    for idx in range(len(startIndices)):
        # use 0-based
        start_idx, end_idx = startIndices[idx] - 1, endIndices[idx] - 1
        start_idx, end_idx = trim_to_compartment(s, start_idx, end_idx)
        if start_idx < end_idx:
            count = item_count_l[end_idx] - item_count_l[start_idx]
        else:
            count = 0
        result.append(count)

    return result


s = '|**|*|*'
startIndices = [1, 1]
endIndices = [5, 6]
# s = '*|*|*|'
# startIndices = [1]
# endIndices = [6]
print(numberOfItems(s, startIndices, endIndices))
