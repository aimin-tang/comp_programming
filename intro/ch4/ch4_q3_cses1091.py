def get_ticket(tickets, customer):
    # tickets: [3, 5, 5, 7, 8]
    idx = len(tickets) - 1
    while idx >= 0:
        if tickets[idx] > customer:
            idx -= 1
        else:
            break

    if idx == -1:
        return -1, tickets

    found = tickets[idx]
    tickets = tickets[:idx] + tickets[idx + 1:]
    return found, tickets


def solve(tickets, customers):
    tickets.sort()

    result = []
    for customer in customers:
        found, tickets = get_ticket(tickets, customer)
        result.append(found)

    return result


n, m = 5, 3
tickets = [5, 3, 7, 8, 5]
customers = [4, 8, 3]
print(solve(tickets, customers))
