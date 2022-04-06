def get_idx(arr, num, start_at):
    # [5, 1, 22, 25, 6, -1, 8, 10]
    # for 22, start_at 1, return 2
    # for 22, start_at 3, return -1
    i = start_at
    while i < len(arr):
        if arr[i] == num:
            return i
        i += 1

    return -1

def isValidSubsequence(array, sequence):
    start_at = 0
    for num in sequence:
        start_at = get_idx(array, num, start_at)
        if start_at == -1:
            return False

    return True

array = [5, 1, 22, 25, 6, -1, 8, 10]
seq = [1, 6, -1, 10]

print(isValidSubsequence(array, seq))