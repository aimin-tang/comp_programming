def paint(input_str):
    lines = input_str.strip().split('\n')
    lines = [line.strip() for line in lines]

    john_start, john_end = map(int, lines[0].split())
    bessie_start, bessie_end = map(int, lines[1].split())

    wasted = max(min(john_end, bessie_end) - max(john_start, bessie_start), 0)

    return (john_end - john_start) + (bessie_end - bessie_start) - wasted

if __name__ == '__main__':
    input_str = """4 8
    7 10
    """
    print(paint(input_str))

# note: overlap of two segments:
# max(min(e1, e2) - max(s1, s2) , 0)
