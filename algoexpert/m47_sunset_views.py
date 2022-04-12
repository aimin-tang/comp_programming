def west_views(buildings):
    highest = 0
    result = []
    for idx, building in enumerate(buildings):
        if building > highest:
            result.append(idx)
            highest = building

    return result

def sunsetViews(buildings, direction):
    if direction == 'EAST':
        result = west_views(reversed(buildings))
        return sorted([len(buildings) - i - 1 for i in result])
    else:
        return west_views(buildings)
