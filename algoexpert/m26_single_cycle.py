def jump_to(array, jump_from):
    # return index after the jump
    # [2, 3, 1, -4, -4, 2]
    end = array[jump_from] + jump_from
    l = len(array)

    return (end + 1) % l - 1

def hasSingleCycle(array):
    taken = [0 for _ in range(len(array))]
    taken[0] = 0
    to_idx = 0
    for _ in range(len(array)):
        to_idx = jump_to(array, to_idx)
        if taken[to_idx] > 0:
            return False
        else:
            taken[to_idx] += 1

    return to_idx == 0

array = [0, 1, 1, 1, 1]
print(hasSingleCycle(array))