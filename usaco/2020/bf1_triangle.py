import itertools

def get_coord_sets(perm):
    # perm: [(0, 0), (0, 1), (1, 2)]
    xs = set()
    ys = set()
    for x, y in perm:
        xs.add(x)
        ys.add(y)

    return xs, ys

def is_valid(xs, ys):
    return len(xs) < 3 and len(ys) < 3

def get_area(xs, ys):
    return (max(xs) - min(xs)) * (max(ys) - min(ys))

def solve(posts):
    biggest = 0
    perms = itertools.permutations(posts, 3)

    for perm in perms:
        xs, ys = get_coord_sets(perm)
        if is_valid(xs, ys):
            area_x2 = get_area(xs, ys)
            if area_x2 > biggest:
                biggest = area_x2

    return biggest


posts = [(0, 0), (0, 1), (1, 0), (1, 2)]
print(solve(posts))