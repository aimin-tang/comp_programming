arr = [-1, 2, 4, -3, 5, 2, -5, 2]

def mss2():
    n = len(arr)
    result, start, end = 0, 0, 0
    for i in range(n):
        temp_result = 0
        for j in range(i, n):
            temp_result += arr[j]
            if temp_result > result:
                result, start, end = temp_result, i, j

    return result, start, end

res = 0, 0, 0
import time
t1 = time.time()
for r in range(100000):
    res = mss2()
t2 = time.time()
print(t2 - t1)
print(res)