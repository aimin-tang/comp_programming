def nextGreaterElement(array):
    array2 = array + array
    result = []

    for i in range(len(array)):
        for j in range(i + 1, len(array2)):
            if array2[j] <= array[i]:
                continue
            else:
                result.append(array2[j])
                break
        else:
            result.append(-1)

    return result

