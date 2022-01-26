#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for todo_idx in range(1, n):
        todo_num = arr[todo_idx]
        i = todo_idx - 1
        while i >= 0:
            if arr[i] > todo_num:
                arr[i + 1] = arr[i]
                i -= 1
            else:
                break

        arr[i + 1] = todo_num

        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
