def parse_input(input_str):
    lines = input_str.strip().split('\n')
    c0, m0 = map(int, lines[0].strip().split())
    c1, m1 = map(int, lines[1].strip().split())
    c2, m2 = map(int, lines[2].strip().split())

    return c0, m0, c1, m1, c2, m2

def pour(cfrom, mfrom, cto, mto, bfrom, bto):
    if mfrom + mto >= cto:
        mfrom = mfrom + mto - cto
        mto = cto
    else:
        mto = mfrom + mto
        mfrom = 0

    return mfrom, mto

def mixing(c0, m0, c1, m1, c2, m2):
    cl = [c0, c1, c2]
    ml = [m0, m1, m2]

    for i in range(100):
        bfrom = i % 3
        bto = (i + 1) % 3

        ml[bfrom], ml[bto] = pour(cl[bfrom], ml[bfrom], cl[bto], ml[bto],
                                  bfrom, bto)

    print('\n'.join([str(m) for m in ml]))


if __name__ == '__main__':
    input_str = """
    10 3
    11 4
    12 5
    """
    c0, m0, c1, m1, c2, m2 = parse_input(input_str)
    print(mixing(c0, m0, c1, m1, c2, m2))

