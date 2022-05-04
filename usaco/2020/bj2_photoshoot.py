def get_fjs(bs, cow1):
    # bs: [4, 6, 7, 6]
    result = [cow1]
    prev_cow = cow1
    for b in bs:
        curr_cow = b - prev_cow
        result.append(curr_cow)
        prev_cow = curr_cow

    return result

def solve(bs):
    N = len(bs) + 1
    for cow1 in range(1, bs[0]):
        fjs = get_fjs(bs, cow1)
        if len(set(fjs)) < N:
            continue
        else:
            return fjs


bs = [4, 6, 7, 6]
print(solve(bs))