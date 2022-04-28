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
            d = end_count[letter] - start_count[letter]
            if d > 0:
                diff_d[letter] = d
        else:
            diff_d[letter] = end_count[letter]

    result = max(diff_d.values()) - min(diff_d.values())
    return result

def get_diff_end_at(s, count_l, end):
    start = end - 1
    last_letter = s[end]

    result = 0
    while start > 0:
        if s[start] == last_letter:
            curr_diff = get_diff(count_l, start - 1, end)
            if curr_diff > result:
                result = curr_diff
        start -= 1

    return result

def getMaxFreqDeviation(s):
    if len(s) == 1:
        return 0

    count_l = get_count_l(s)

    result = 0
    for end in range(len(s) - 1, 0, -1):
        diff_end_at = get_diff_end_at(s, count_l, end)
        if diff_end_at > result:
            result = diff_end_at

    return result

s = 'bbacccabab'
# s = 'aaaaa'
print(getMaxFreqDeviation(s))
# print(get_count_l(s))