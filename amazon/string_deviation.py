from collections import defaultdict
import copy

def get_count_l(s):
    curr_d = defaultdict(int)
    result = [copy.copy(curr_d)]

    for letter in s:
        curr_d[letter] += 1
        result.append(copy.copy(curr_d))

    return result


def get_diff(count_l, start, end):
    if len(count_l) == 1:
        return 0

    diff_d = {}
    start_count, end_count = count_l[start], count_l[end + 1]
    for letter, count in end_count.items():
        if letter in start_count:
            diff_d[letter] = end_count[letter] - start_count[letter]
        else:
            diff_d[letter] = end_count[letter]

    diff_d_copy = {}
    for letter, count in diff_d.items():
        if count != 0:
            diff_d_copy[letter] = count

    result = max(diff_d_copy.values()) - min(diff_d_copy.values())
    return result

def getMaxFreqDeviation(s):
    if len(s) == 1:
        return 0

    result = 0
    count_l = get_count_l(s)
    for start in range(len(s) - 1):
        for end in range(start + 1, len(s)):
            diff = get_diff(count_l, start, end)
            if diff > result:
                result = diff

    return result

s = 'bbacccabab'
# s = 'aaaaa'
print(getMaxFreqDeviation(s))
# print(get_count_l(s))