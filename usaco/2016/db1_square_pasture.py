def parse_input(input_lines):
    lines = input_lines.strip().split('\n')
    p1 = list(map(int, lines[0].strip().split()))
    p2 = list(map(int, lines[1].strip().split()))
    return p1, p2

def get_square_side(p1, p2):
    p1x1, p1y1, p1x2, p1y2 = p1
    p2x1, p2y1, p2x2, p2y2 = p2
    x_range = max(p1x2, p2x2) - min(p1x1, p2x1)
    y_range = max(p1y2, p2y2) - min(p1y1, p2y1)

    return max(x_range, y_range)

input_lines = """
6 6 8 8
1 8 4 9
"""

p1, p2 = parse_input(input_lines)
side = get_square_side(p1, p2)
print(side * side)