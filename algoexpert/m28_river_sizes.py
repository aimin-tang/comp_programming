def get_dimensions(matrix):
    row = len(matrix)
    col = len(matrix[0])
    return row, col

def get_max(lengths, row, col):
    result = 0
    for ri in range(row):
        for ci in range(col):
            if lengths[row][col] > result:
                result = lengths[row][col]
    return result

def find_river(matrix, row_idx, col_idx, lengths, visited):
    # river starts at row_idx, col_idx. update its length in
    # lengths, and update visited.

    neighbors = get_neighbors(matrix, row_idx, col_idx)
    for nri, nci in neighbors:
        visited[nri][nci] = True
        if matrix[nri][nci] == 0:
            continue
        else:

def riverSizes(matrix):
    row, col = get_dimensions(matrix)
    lengths = [[0 for _ in range(col)] for _ in range(row)]
    visited = [[False for _ in range(col)] for _ in range(row)]

    for row_idx in range(row):
        for col_idx in range(col):
            if visited[row_idx][col_idx]:
                continue
            else:
                find_river(matrix, row_idx, col_idx, lengths, visited)

    return get_max(lengths, row, col)

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

print(riverSizes(matrix))
