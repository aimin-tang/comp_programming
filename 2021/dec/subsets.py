def subsets0(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]


def subsets1(numbers):
    if not numbers:
        return [[]]
    half_result1 = subsets(numbers[1:])
    half_result2 = [[numbers[0]] + r for r in half_result1]
    return half_result1 + half_result2


def build_binary_list(n):
    if n == 1:
        return ['0', '1']
    else:
        half = build_binary_list(n - 1)
        half1 = ['0' + e for e in half]
        half2 = ['1' + e for e in half]
        return half1 + half2


def subsets2(numbers):
    bin_l = build_binary_list(len(numbers))
    result = []
    for b in bin_l:
        subset = []
        for i in range(len(b)):
            if b[i] == '1':
                subset.append(numbers[i])
        result.append(subset)
    return result


subsets = subsets2


# wrapper function
def subsets_of_given_size(numbers, n):
    return [x for x in subsets(numbers) if len(x) == n]


if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    n = 3
    print(subsets_of_given_size(numbers, n))

# in subset1, easy to make this mistake:
#     half_result1 = subsets(numbers[1:])
#     half_result2 = [r.append(numbers[0]) + r for r in half_result1]
# instead of:
#     half_result1 = subsets(numbers[1:])
#     half_result2 = [[numbers[0]] + r for r in half_result1]
