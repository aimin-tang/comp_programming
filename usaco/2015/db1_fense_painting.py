def parse_input(input_lines):
    lines = input_lines.strip().split('\n')
    john = list(map(int, lines[0].strip().split()))
    bessie = list(map(int, lines[1].strip().split()))
    return john, bessie

def combine(john, bessie):
    lows = [john[0], bessie[0]]
    highs = [john[1], bessie[1]]

    if max(lows) < min(highs):
        return max(highs) - min(lows)
    else:
        return john[1] - john[0] + bessie[1] - bessie[0]

input_lines = """
7 10
4 8
"""

john, bessie = parse_input(input_lines)
length = combine(john, bessie)
print(length)