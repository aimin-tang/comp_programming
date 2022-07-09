def parse_input(input_lines):
    lines = input_lines.strip().split('\n')
    bb1 = list(map(int, lines[0].strip().split()))
    bb2 = list(map(int, lines[1].strip().split()))
    truck = list(map(int, lines[2].strip().split()))

    return bb1, bb2, truck

def get_visible_area(bb, truck):
    bbx1, bby1, bbx2, bby2 = bb
    truckx1, trucky1, truckx2, trucky2 = truck

    bb_area = (bbx2 - bbx1) * (bby2 - bby1)
    wastedx = max(min(bbx2, truckx2) - max(bbx1, truckx1), 0)
    wastedy = max(min(bby2, trucky2) - max(bby1, trucky1), 0)
    wasted_area = wastedx * wastedy

    return bb_area - wasted_area

input_lines = """
1 2 3 5
6 0 10 4
2 1 8 3
"""

bb1, bb2, truck = parse_input(input_lines)
result = get_visible_area(bb1, truck) + get_visible_area(bb2, truck)
print(result)