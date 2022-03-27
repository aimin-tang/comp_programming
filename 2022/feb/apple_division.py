import math

input_str = """
2
3 2 
"""
input_lines = input_str.strip().split('\n')

n = int(input_lines[0])
p = list(map(int, input_lines[1].strip().split()))

result = (math.inf, [], [])
for mask in range(1 << n):
    l1, l2 = [], []
    for i in range(n):
        if mask & (1 << i):
            l1.append(p[i])
        else:
            l2.append(p[i])

    diff = abs(sum(l1) - sum(l2))
    if diff < result[0]:
        result = (diff, l1, l2)

print(result)
