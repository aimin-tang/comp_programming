# list indexes
# l[i]
# l[i:j]
# l[:j]
# l[i:]
# l[-3:]
# l[i:j:k]
# l[::2]
# l[::-1]

# list functions
# len(l) 1
# sorted(l) nlogn
# l.sort(l) nlogn
# l.count(c) n
# c in l n
# l.append(c) amortized 1
# l.pop(c) amortized 1

l = [0 for _ in range(5)]
for idx, v in enumerate(l):
    print(f'{idx}: {v}')

s = 'cowboy bebop'
c = {letter: 0 for letter in s}

# range
# range(k, n)
# range(k, n, 2)
# range(n-1, -1, -1)

l = [i for i in range(5)]
def all_pairs(l):
    n = len(l)
    for i in range(n-1):
        for j in range(i+1, n):
            yield (l[i], l[j])

for x, y in all_pairs(l):
    print(x, y)

# Counter class
from collections import Counter
c = Counter('cowboy bebop')

# defaultdict
from collections import defaultdict
g = defaultdict(list)
g['paris'].append('marseille')

import sys
height, width = map(int, sys.stdin.readline().strip().split())
import os
l = list(map(int, os.read(0, 1000).strip().split()))

from collections import defaultdict

n_edges = int(input())
g = defaultdict(dict)
for _ in range(n_edges):
    f, t, d = input().split()
    g[f][t] = int(d)
    g[t][f] = int(d)

# stack -> list (append, pop)
# queue
# deque: appendleft, popleft, append, pop
# heapq (min heap): heappush, heappop, heapify, heapreplace, nlargest, nsmallest, merge
