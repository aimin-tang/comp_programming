from collections import defaultdict


def parse_input(input_str):
    lines = input_str.strip().split('\n')
    n, m = map(int, lines[0].strip().split())
    n_segments = []
    for i in range(n):
        linei = lines[i + 1]
        miles, speed = map(int, linei.strip().split())
        n_segments.append((miles, speed))

    m_segments = []
    for i in range(n):
        linei = lines[i + 1 + n]
        miles, speed = map(int, linei.strip().split())
        m_segments.append((miles, speed))

    return n_segments, m_segments


def build_dict(segments):
    d = {}

    start = 0
    for segment in segments:
        end = start + segment[0]
        for i in range(start, end):
            d[i] = segment[1]
        start += segment[0]

    return d


def speeding(input_str):
    n_segments, m_segments = parse_input(input_str)

    speed_limit = build_dict(n_segments)
    drove = build_dict(m_segments)

    over_limit = [drove[i] - speed_limit[i] for i in range(100)]
    return max(max(over_limit), 0)


if __name__ == '__main__':
    input_str = """
    3 3
    40 75
    50 35
    10 45
    40 76
    20 30
    40 40
    """
    print(speeding(input_str))
