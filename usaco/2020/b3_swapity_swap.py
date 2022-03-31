def parse_input(lines):
    N, K = map(int, lines[0].strip().split())
    steps = []
    for i in range(1, K + 1):
        i_from, i_to = map(int, lines[i].strip().split())
        steps.append((i_from, i_to))

    return N, K, steps


def do_one_round(seq, steps):
    for i_from, i_to in steps:
        seq = seq[:i_from-1] + list(reversed(seq[i_from-1:i_to])) + seq[i_to:]

    return seq

def find_cycle(N, K, steps):
    target = [i+1 for i in range(N)]
    seq = target[:]
    count = 0

    while True:
        seq = do_one_round(seq, steps)
        count += 1
        if seq == target:
            return count

if __name__ == '__main__':
    input_str = """
    7 2
    2 5
    3 7
    """
    N, K, steps = parse_input(input_str.strip().split('\n'))

    seq = [1, 2, 3, 4, 5, 6, 7]
    cycle = find_cycle(N, K, steps)

    for i in range(K % cycle):
        seq = do_one_round(seq, steps)

    for n in seq:
        print(n)
