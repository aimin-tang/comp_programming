def mss31():
    # arr = [-1, 2, 4, -3, 5, 2, -5, 2]
    arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
    # arr = [4, -3]
    rsum = 0
    max_so_far = 0
    startp=0
    endp=0
    tmp_start=0
    for i in range(len(arr)):
        max_so_far = max_so_far + arr[i]
        if rsum < max_so_far:
            rsum = max_so_far
            startp = tmp_start
            endp = i
        if max_so_far < 0:
            max_so_far = 0
            tmp_start = i+1

    return rsum, startp, endp

def mss32():
    # arr = [-1, 2, 4, -3, 5, 2, -5, 2]
    arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
    # arr = [4, -3]
    tmpsum, tmpstart = 0, 0
    rsum, rstart, rend = 0, 0, 0
    for i in range(len(arr)):
        tmpsum += arr[i]
        if tmpsum > rsum:
            rsum = tmpsum
            rstart = tmpstart
            rend = i + 1
        elif tmpsum < 0:
            tmpsum = 0
            tmpstart = i + 1

    return rsum, rstart, rend


import time
t1 = time.time()
for r in range(100000):
    res = mss32()
t2 = time.time()
print(t2 - t1)
print(res)
