from collections import defaultdict


def processLogs(logs, threshold):
    # int_logs: [[9, 7, 50], [22, 7, 20], [33, 7, 50], [22, 7, 30]]
    int_logs = []
    for line in logs:
        int_logs.append(list(map(int, line.strip().split())))

    counts = defaultdict(int)
    for u1, u2, _ in int_logs:
        counts[u1] += 1
        if u2 != u1:
            counts[u2] += 1

    result = []
    for user, count in counts.items():
        if count >= threshold:
            result.append(user)

    result.sort()
    str_result = [str(user) for user in result]
    return str_result



logs = ["9 7 50", "22 7 20", "33 7 50", "22 7 30"]
threshold = 3
print(processLogs(logs, threshold))
