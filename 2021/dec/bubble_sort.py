def bubble_sort():
    arr = [2, 3, 1, 4]
    arr = []
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(bubble_sort())

# note the ranges of i and j
# complexity: (n-1) + (n-2) + ... 1. O(n^2)
