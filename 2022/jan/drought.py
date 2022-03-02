def all_same(cows):
    for i in range(1, len(cows)):
        if cows[i] != cows[0]:
            return False
    return True

def get_most_hungry_idx(cows):
    most_hungry = max(cows)

def is_doable(cows):
    if len(cows) == 1:
        return True

    if len(cows) == 2:
        if cows[0] == cows[1]:
            return True
        else:
            return False

    if all_same(cows):
        return True




if __name__ == '__main__':
    # cows = [8, 10, 5]
    cows = [5]
    print(is_doable(cows))

