import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


from collections import deque
import itertools

def _flip(arr, i, j):
  # flip arr for elements between i and j (inclusive on both)
  result = list(arr[:i])
  result += list(reversed(arr[i:j+1]))
  result += list(arr[j+1:])

  return tuple(result)

def minOperations(arr):
  if len(arr) == 1:
    # only 1 element. alrady sorted and needs no steps
    return []

  visited = []
  goal = tuple(sorted(arr))
  q = deque()
  q.append((0, tuple(arr)))

  while len(q) > 0:
    level, popped_arr = q.popleft()
    if popped_arr == goal:
      return level

    for i, j in itertools.combinations(range(len(popped_arr)), 2):
      to_add_arr = _flip(popped_arr, i, j)
      to_add_arr = tuple(to_add_arr)
      if to_add_arr not in visited:
        level += 1
        q.append((level, to_add_arr))
        visited.append(to_add_arr)

  # should never hit here
  return None



# Write your code here


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 5
    arr_1 = [1, 2, 5, 4, 3]
    expected_1 = 1
    output_1 = minOperations(arr_1)
    check(expected_1, output_1)

    n_2 = 3
    arr_2 = [3, 1, 2]
    expected_2 = 2
    output_2 = minOperations(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here

