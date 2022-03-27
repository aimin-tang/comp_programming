import itertools
from collections import deque

def _flip(arr, i, j):
    arr = list(arr)
    result = arr[:i]
    result += list(reversed(arr[i:j+1]))
    result += arr[j+1:]

    return result

def minOperations(arr):
    if len(arr) in [0, 1]:
        return []

    q = deque()
    visited = []
    goal = sorted(arr)
    q.append(([], arr))

    while len(q):
        step, todo_arr = q.popleft()
        if todo_arr in visited:
            continue
        if todo_arr == goal:
            return step

        visited.append(todo_arr)
        for i, j in itertools.combinations(range(len(arr)), 2):
            new_todo_arr = _flip(todo_arr, i, j)
            q.append((step + [(i, j)], new_todo_arr))

print(minOperations([3, 1, 2]))
