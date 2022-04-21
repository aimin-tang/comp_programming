def levenshteinDistance(str1, str2):
    # str1: abc, str2: yabd
    dpm = []
    dpm.append([i for i in range(len(str1) + 1)])
    for row in range(1, len(str2) + 1):
        dpm.append([row])

    for row in range(1, len(str2) + 1):
        for col in range(1, len(str1) + 1):
            if str1[col - 1] == str2[row - 1]:
                dpm[row].append(dpm[row - 1][col - 1])
            else:
                ul = dpm[row - 1][col - 1]
                l = dpm[row][col - 1]
                u = dpm[row - 1][col]
                dpm[row].append(min(ul, l, u) + 1)

    return dpm[-1][-1]


#      " "   a    b    c
# " "   0    1    2    3
#  y    1    1    2    3
#  a    2    1    2    3
#  b    3    2    1    2
#  d    4    3    2    2
print(levenshteinDistance('abc', 'yabd'))
