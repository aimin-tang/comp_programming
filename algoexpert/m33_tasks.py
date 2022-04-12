def taskAssignment(k, tasks):
    indexed_tasks = []
    for i in range (2 * k):
        indexed_tasks.append((tasks[i], i))

    indexed_tasks.sort()
    # [(1, 0), (1, 4), (3, 1), (3, 3), (4, 5), (5, 2)]
    result = []

    for i in range(k):
        result.append([indexed_tasks[i][1], indexed_tasks[2 * k - i - 1][1]])

    return result

tasks = [1, 3, 5, 3, 1, 4]
k = 3
print(taskAssignment(k, tasks))
