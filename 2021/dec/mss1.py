arr = [-1, 2, 4, -3, 5, 2, -5, 2]

n = len(arr)
result, start, end = 0, 0, 0
for i in range(n):
    for j in range(i, n):
        temp_result = sum(arr[i:j])
        if temp_result > result:
            result, start, end = temp_result, i, j

print(result, start, end)

# 1/3 slower:
# n = len(arr)
# result = (0, 0, 0)    # sum, start, end
# for i in range(n):
#     for j in range(i, n):
#         temp_result = (sum(arr[i:j]), i, j)
#         result = max(temp_result, result)
#
# print(result)

