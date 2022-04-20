def find_most(movies):
    movies_by_end = sorted(movies, key=lambda x: x[1])
    result = []
    curr_end = 0
    idx = 0

    while idx < len(movies):
        if movies_by_end[idx][0] >= curr_end:
            curr_end = movies_by_end[idx][1]
            result.append(movies_by_end[idx])
        idx += 1

    return result

movies = [[3, 5], [4, 9], [5, 8]]
print(find_most(movies))
