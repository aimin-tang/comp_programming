def get_next_idx(array, curr_idx):
    step = array[curr_idx]
    return (curr_idx + step) % len(array)


def hasSingleCycle(array):
    visited = [False for _ in range(len(array))]

    curr_idx = 0
    for i in range(len(array)):
        next_idx = get_next_idx(array, curr_idx)
        if visited[next_idx]:
            return False
        visited[next_idx] = True
        curr_idx = next_idx

    return curr_idx == 0

array = [2, 2, -1]
print(hasSingleCycle(array))