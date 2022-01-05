def majority(L):
    count = {}
    for word in L:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    val_1st_max, arg_1st_max = min((-count[word], word) for word in count)
    return arg_1st_max

L = "hisisatestnotadrill"

print(majority(L))