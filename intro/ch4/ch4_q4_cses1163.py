def get_gaps(points):
    result = []
    for idx in range(1, len(points)):
        result.append(points[idx] - points[idx-1])

    return result

def solve(x, lights):
    points = [0, x]
    result = []

    for light in lights:
        points.append(light)
        points.sort()
        gaps = get_gaps(points)
        result.append(max(gaps))

    return result


x, n = 8, 3
lights = [3, 6, 2]

print(solve(x, lights))