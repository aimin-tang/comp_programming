def getHeaviestPackage(packageWeights):
    if len(packageWeights) == 1:
        return packageWeights[0]

    curr_idx = len(packageWeights) - 1
    combined = []
    while curr_idx > 0:
        last_pkg = packageWeights.pop()
        sec_last_pkg = packageWeights.pop()
        if last_pkg > sec_last_pkg:
            packageWeights.append(last_pkg + sec_last_pkg)
        else:
            combined.append(last_pkg)
            packageWeights.append(sec_last_pkg)
        curr_idx -= 1

    combined.append(packageWeights[0])

    result = max(combined)
    return result



packageWeights = [20, 13, 8, 9]
# packageWeights = [30, 15, 5, 9]
print(getHeaviestPackage(packageWeights))
