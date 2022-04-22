def get_next_idx(array, curr_idx, step):
    # handle wraps
    return (curr_idx + step + len(array)) % len(array)

def hasSingleCycle(array):
    # [2, 3, 1, -4, -4, 2]
    reached = [False for _ in range(len(array))]
    curr_idx = 0
    for _ in range(len(array)):
        step = array[curr_idx]
        next_idx = get_next_idx(array, curr_idx, step)
        if reached[next_idx]:
            return False
        else:
            reached[next_idx] = True
            curr_idx = next_idx

    return next_idx == 0

print(hasSingleCycle([2, 3, 1, -4, -4, 2]))