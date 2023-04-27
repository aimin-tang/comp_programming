def minimumWaitingTime(queries):
    # Write your code here.

    queries.sort()
    result = 0
    so_far = 0
    for query in queries:
        result += so_far
        so_far += query

    return result

queries = [3, 2, 1, 2, 6]
result = minimumWaitingTime(queries)
print(result)
# result: 17
