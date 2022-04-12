def validStartingCity(distances, fuel, mpg):
    extra = [0]
    for i in range(1, len(distances)):
        extra.append(extra[i-1] + fuel[i-1] * mpg - distances[i-1])

    min_extra_idx = extra.index(min(extra))
    return min_extra_idx

# gas     10  20  10   0  30
# to_go    5  25  15  10  15
# have     0   5   0  -5  -15
# left    15  20  15  10   0

distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10
print(validStartingCity(distances, fuel, mpg))

