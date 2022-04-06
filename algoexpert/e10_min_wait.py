def minimumWaitingTime(queries):
    # Write your code here.

    queries.sort()
    result = 0
    so_far = 0
    for query in queries:
        result += so_far
        so_far += query

    return result
