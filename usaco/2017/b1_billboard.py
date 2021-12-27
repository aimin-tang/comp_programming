def covered(bb, truck):
    x1bb, y1bb, x2bb, y2bb = bb
    x1t, y1t, x2t, y2t = truck

    bb_area = (y2bb - y1bb) * (x2bb - x1bb)
    covered_x = max(min(x2t, x2bb) - max(x1t, x1bb), 0)
    covered_y = max(min(y2t, y2bb) - max(y1t, y1bb), 0)
    covered_area = covered_x * covered_y

    return bb_area - covered_area

def billboard(input_str):
    lines = input_str.strip().split('\n')
    bb1 = list(map(int, lines[0].strip().split()))
    bb2 = list(map(int, lines[1].strip().split()))
    truck = list(map(int, lines[2].strip().split()))

    return (covered(bb1, truck) + covered(bb2, truck))

if __name__ == '__main__':
    input_str = """
    1 2 3 5
    6 0 10 4
    2 1 8 3
    """
    print(billboard(input_str))

# only unpack lists, not mapped objects!
