def merge(interval1, interval2):
    return [min(interval1[0], interval2[0]),
            max(interval1[1], interval2[1])]


def mergeOverlappingIntervals(intervals):
    if len(intervals) in [0, 1]:
        return intervals

    intervals.sort()
    result = []
    curr = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= curr[1]:
            curr = merge(curr, intervals[i])
        else:
            result.append(curr)
            curr = intervals[i]

    result.append(curr)

    return result


intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
print(mergeOverlappingIntervals(intervals))
