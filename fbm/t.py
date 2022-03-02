import math


# Add any extra import statements you may need here
import itertools
import queue

# Add any helper functions you may need here


def flip(seq, n1, n2):
    # flip numbers between n1 and n2 (inclusive). n1 < n2
    flip_to = tuple(reversed(seq[n1:n2 + 1]))

    result = seq[:n1]
    result += flip_to
    result += seq[n2+1:]

    return result


def minOperations(arr):
    # Write your code here
    visited = []
    goal = tuple(sorted(arr))
    q = queue.Queue()
    q.put((0, [], tuple(arr)))

    while not q.empty():
        level, steps, curr_seq = q.get()

        if curr_seq == goal:
            return level, steps

        for n1, n2 in itertools.combinations(range(len(arr)), 2):
            new_seq = tuple(flip(curr_seq, n1, n2))
            if new_seq not in visited:
                q.put((level + 1, steps + [(n1, n2)], new_seq))
                visited.append(new_seq)


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
    print(output_1)

    n_2 = 3
    arr_2 = [3, 1, 2]
    expected_2 = 2
    output_2 = minOperations(arr_2)
    print(output_2)

    # Add your own test cases here

