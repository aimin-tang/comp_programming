import math


def fit_in(customer, room):
    # (3, 3) can fit in [(-math.inf, -math.inf), (1, 2), (4, 4), (math.inf, math.inf)]
    cstart, cend = customer

    for idx in range(1, len(room)):
        rstart = room[idx][0]
        rend = room[idx - 1][1]
        if rend < cstart and cend < rstart:
            room.insert(idx, customer)
            return True

    return False


def solve(customers):
    # rooms: [[(1, 2), (4, 4)], [(2, 4)]]
    rooms = []
    result = []
    for customer in customers:
        for idx in range(len(rooms)):
            if fit_in(customer, rooms[idx]):
                result.append(idx)
                break
        else:
            new_room = [(-math.inf, -math.inf), customer, (math.inf, math.inf)]
            rooms.append(new_room)
            result.append(len(rooms))

    return rooms, result


customers = [(1, 2), (2, 4), (4, 4)]
print(solve(customers))

# rooms: [[(-math.inf, -math.inf), (1, 2), (4, 4), (math.inf, math.inf)],
#         [(-math.inf, -math.inf), (2, 4)], (math.inf, math.inf)]
