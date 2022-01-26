def quick_sort(seq):
    if len(seq) <= 1:
        return seq

    pivot = seq[0]
    smaller, larger = [], []

    for idx in range(1, len(seq)):
        num = seq[idx]
        if num < pivot:
            smaller.append(num)
        else:
            larger.append(num)

    result = quick_sort(smaller) + [pivot] + quick_sort(larger)
    print(' '.join(map(str, result)))
    return result

n = 6
arr = "5 8 1 3 7 9 2".split()

quick_sort(arr)
