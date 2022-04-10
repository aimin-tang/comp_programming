def numberOfWaysToTraverseGraph(width, height):
    result = [[1 for _ in range(width)]]

    for i in range(1, height):
        new_row = [1] + [0 for _ in range(1, width)]
        result.append(new_row)

    for i in range(1, height):
        for j in range(1, width):
            result[i][j] = result[i][j - 1] + result[i - 1][j]

    return result[height - 1][width - 1]

print(numberOfWaysToTraverseGraph(2, 3))
