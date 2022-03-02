def compare_dice(d1, d2):
    # see if d1 beats d2
    result = 0
    for n1 in d1:
        for n2 in d2:
            if n1 > n2:
                result += 1
            elif n1 < n2:
                result -= 1
            else:
                # tie
                continue

    return result

def d3_exists(d1, d2):
    for n1 in range(1, 11):
        for n2 in range(1, 11):
            for n3 in range(1, 11):
                for n4 in range(1, 11):
                    d = [n1, n2, n3, n4]
                    if compare_dice(d, d1) > 0 and compare_dice(d1, d2) > 0 \
                        and compare_dice(d2, d) > 0:
                        return 'yes'
                    if compare_dice(d, d1) < 0 and compare_dice(d1, d2) < 0 \
                            and compare_dice(d2, d) < 0:
                        return 'yes'

    return 'no'

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        line = list(map(int, input().strip().split()))
        d1 = line[:4]
        d2 = line[4:]
        print(d3_exists(d1, d2))
