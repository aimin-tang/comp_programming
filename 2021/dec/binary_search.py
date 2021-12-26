def binary_search(arr, elem):
    start = 0
    end = len(arr) - 1

    while start < end:
        if arr[start] > elem or arr[end] < elem:
            return -1
        elif arr[start] == elem:
            return start
        elif arr[end] == elem:
            return end
        else:
            mid = (start + end) // 2
            if arr[mid] == elem:
                return mid
            elif arr[mid] > elem:
                    end = mid - 1
            else:
                start = mid + 1

arr = [1, 2, 3, 4, 5]
print(binary_search(arr, 0))
print(binary_search(arr, 1))
print(binary_search(arr, 2))
print(binary_search(arr, 3))
print(binary_search(arr, 4))
print(binary_search(arr, 5))
print(binary_search(arr, 6))
