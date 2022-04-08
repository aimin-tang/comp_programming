def get_char_idx(array, char, start):
    idx = start
    while idx < len(array):
        if array[idx] == char:
            return idx
        idx += 1

    return -1


def get_non_char_idx(array, char, start):
    idx = start
    while idx < len(array):
        if array[idx] != char:
            return idx
        idx += 1

    return -1


def moveElementToEnd(array, toMove):
    move_from = get_char_idx(array, toMove, 0)
    if move_from == -1:
        return array

    while move_from < len(array):
        move_to = get_non_char_idx(array, toMove, move_from + 1)
        if move_to == -1:
            return array
        array[move_from], array[move_to] = array[move_to], array[move_from]
        move_from += 1

    return array

array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
print(moveElementToEnd(array, toMove))
