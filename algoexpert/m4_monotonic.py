def isMonotonic(array):
    increase_ok = True
    decrease_ok = True

    idx = 1
    while idx < len(array):
        diff = array[idx] - array[idx - 1]
        if diff > 0:
            if not increase_ok:
                return False
            else:
                decrease_ok = False
        elif diff < 0:
            if not decrease_ok:
                return False
            else:
                increase_ok = False
        idx += 1

    return True

array = [-1, -5, -10, -20]
print(isMonotonic(array))