def mss11():
    arr = [-1, 2, 4, -3, 5, 2, -5, 2]
    n = len(arr)
    result, start, end = 0, 0, 0
    for i in range(n):
        for j in range(i, n):
            temp_result = sum(arr[i:j])
            if temp_result > result:
                result, start, end = temp_result, i, j

    return result, start, end

def mss12():
    # 1/3 slower: to save extra i, j for bad temp_result
    arr = [-1, 2, 4, -3, 5, 2, -5, 2]
    n = len(arr)
    result = (0, 0, 0)    # sum, start, end
    for i in range(n):
        for j in range(i, n):
            temp_result = (sum(arr[i:j]), i, j)
            result = max(temp_result, result)

    return result

res = 0, 0, 0
import time
t1 = time.time()
for r in range(100000):
    res = mss11()
t2 = time.time()
print(t2 - t1)
print(res)

# write code in function, then test repeated. 1/3 faster than repeat main code.
