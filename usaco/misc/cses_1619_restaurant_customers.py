def parse_input(lines):
    n = int(lines[0].strip())
    times = []
    for i in range(1, n + 1):
        start, end = map(int, lines[i].strip().split())
        # shift all numbers down by 1, so our time_l starts at 0
        times.append((start - 1, end - 1))

    return n, times


def get_coord_map(times):
    l = []
    coord_map = {}
    for start, end in times:
        l.append(start)
        l.append(end)

    l.sort()

    idx = 0
    for num in l:
        if num not in coord_map:
            coord_map[num] = idx
            idx += 1

    return coord_map


def get_latest(times):
    latest = 0
    for _, end in times:
        if end > latest:
            latest = end

    return latest


def update_time_l(time_l, start, end):
    i = start
    while i <= end:
        time_l[i] += 1
        i += 1


def solve(times):
    # 0  1  2  3  4  5
    coord_map = get_coord_map(times)
    latest = get_latest(times)
    time_l = [0 for i in range(coord_map[latest] + 1)]

    for start, end in times:
        update_time_l(time_l, coord_map[start], coord_map[end])

    return max(time_l)


input_lines = """
3
5 8
2 4
3 9
"""

n, times = parse_input(input_lines.strip().split('\n'))
print(n, times)
print(solve(times))
