def parse_input(input_lines):
    lines = input_lines.strip().split('\n')
    w = list(map(int, lines[0].strip().split()))
    b1 = list(map(int, lines[1].strip().split()))
    b2 = list(map(int, lines[2].strip().split()))

    return w, b1, b2

def get_covered(w, b):
    wx1, wy1, wx2, wy2 = w
    bx1, by1, bx2, by2 = b
    x_low = max(wx1, min(wx2, bx1))
    x_high = min(max(wx1, bx2), wx2)
    y_low = max(wy1, min(wy2, by1))
    y_high = min(max(wy1, by2), wy2)

    return x_low, y_low, x_high, y_high

def get_wasted(covered1, covered2):
    c1x1, c1y1, c1x2, c1y2 = covered1
    c2x1, c2y1, c2x2, c2y2 = covered2
    x_wasted = max(min(c1x2, c2x2) - max(c1x1, c2x1), 0)
    y_wasted = max(min(c1y2, c2y2) - max(c1y1, c2y1), 0)

    return x_wasted * y_wasted

def get_area(r):
    rx1, ry1, rx2, ry2 = r
    return (ry2 - ry1) * (rx2 - rx1)

input_lines = """
0 0 1000000 1000000
0 0 499999 1000000
500000 0 1000000 1000000
"""

w, b1, b2 = parse_input(input_lines)
covered1 = get_covered(w, b1)
covered2 = get_covered(w, b2)
wasted = get_wasted(covered1, covered2)
covered_area = get_area(covered1) + get_area(covered2) - wasted
result = get_area(w) - covered_area
print(result)
