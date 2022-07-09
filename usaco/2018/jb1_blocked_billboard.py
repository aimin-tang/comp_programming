def parse_input(input_lines):
    lines = input_lines.strip().split('\n')
    bb1 = list(map(int, lines[0].strip().split()))
    bb2 = list(map(int, lines[1].strip().split()))
    return bb1, bb2

def x_covered(bb1, bb2):
    bb1x1, bb1y1, bb1x2, bb1y2 = bb1
    bb2x1, bb2y1, bb2x2, bb2y2 = bb2

    x_low = min(max(bb1x1, bb2x1), bb1x2)
    x_high = max(bb1x1, min(bb1x2, bb2x2))

    return x_low, x_high

def y_covered(bb1, bb2):
    bb1x1, bb1y1, bb1x2, bb1y2 = bb1
    bb2x1, bb2y1, bb2x2, bb2y2 = bb2

    y_low = min(max(bb1y1, bb2y1), bb1y2)
    y_high = max(bb1y1, min(bb1y2, bb2y2))

    return y_low, y_high

def x_fully_covered(bb1, covered):
    bb1x1, bb1y1, bb1x2, bb1y2 = bb1
    cx1, cy1, cx2, cy2 = covered
    return cx1 == bb1x1 and cx2 == bb1x2

def y_fully_covered(bb1, covered):
    bb1x1, bb1y1, bb1x2, bb1y2 = bb1
    cx1, cy1, cx2, cy2 = covered
    return cy1 == bb1y1 and cy2 == bb1y2

def get_area(bb1, covered):
    bb1x1, bb1y1, bb1x2, bb1y2 = bb1
    cx1, cy1, cx2, cy2 = covered
    bb1_area = (bb1x2 - bb1x1) * (bb1y2 - bb1y1)
    if x_fully_covered(bb1, covered) and y_fully_covered(bb1, covered):
        return 0
    elif x_fully_covered(bb1, covered):
        return (bb1x2 - bb1x1) * (cy2 - cy1)
    elif y_fully_covered(bb1, covered):
        return (bb1y2 - bb1y1) * (cx2 - cx1)
    else:
        return bb1_area

input_lines = """
2 1 7 4
5 -1 10 3
"""

bb1, bb2 = parse_input(input_lines)
x_low, x_high = x_covered(bb1, bb2)
y_low, y_high = y_covered(bb1, bb2)
covered = x_low, y_low, x_high, y_high
result = get_area(bb1, covered)
print(result)
