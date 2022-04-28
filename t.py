def isValidSubsequence(array, sequence):
    idx1 = 0
    for num in sequence:
        try:
            idx1 = array.index(num, idx1) + 1
        except ValueError:
            return False

    return True

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, 6, -1, 10]

print(isValidSubsequence(array, sequence))