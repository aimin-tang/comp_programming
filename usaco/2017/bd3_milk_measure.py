COWS = ['Bessie', 'Elsie', 'Mildred']


def change_amount(amount, log):
    # amount: [7, 7, 7], log: (1, Bessie, 2)
    day, cow, change = log
    idx = COWS.index(cow)
    amount[idx] += change

def get_leaders(amount):
    max_milk = max(amount)
    result = []
    for idx in range(len(amount)):
        if amount[idx] == max_milk:
            result.append(COWS[idx])

    return result

def solve(logs):
    logs.sort()

    amount = [7, 7, 7]
    leaders = COWS[:]
    result = 0

    for day in range(0, len(logs)):
        change_amount(amount, logs[day])
        new_leaders = get_leaders(amount)
        if new_leaders != leaders:
            result += 1
            leaders = new_leaders[:]

    return result

# log format: [(day, cow, change), ... ]
logs = [(7, 'Mildred', 3),
        (4, 'Elsie', -1),
        (9, 'Mildred', -1),
        (1, 'Bessie', +2)]

print(solve(logs))