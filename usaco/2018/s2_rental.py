def parse_input(input_str):
    lines = input_str.strip().split('\n')
    N, M, R = map(int, lines[0].strip().split())

    cows = [int(lines[i + 1].strip()) for i in range(N)]
    cows.sort(reverse=True)
    stores = []
    for i in range(M):
        line = lines[N+i+1].strip()
        gallons, price = map(int, line.strip().split())
        stores.append((gallons, price))
        stores.sort(key=lambda x: x[1], reverse=True)

    rentals = [int(lines[N+M+i+1].strip()) for i in range(R)]
    rentals.sort(reverse=True)

    return N, M, R, cows, stores, rentals

def get_store_income(i):
    total_milk = sum(cows[:i])
    store_income = 0
    next_store_id = 0

    while total_milk > 0:
        next_store = stores[next_store_id]
        next_store_milk = min(next_store[0], total_milk)
        store_income += next_store_milk * next_store[1]
        total_milk -= next_store_milk
        next_store_id += 1

    return store_income

def solve():
    result = []

    for i in range(N + 1):
        # i: how many cows are for milking, rest (N-i) for rental
        rental_cow_count = min(N - i, len(rentals))
        rental_income = sum(rentals[:rental_cow_count])
        store_cow_count = N - rental_cow_count
        store_income = get_store_income(store_cow_count)
        result.append(rental_income + store_income)

    return max(result)


if __name__ == '__main__':
    input_str = """
    5 3 4
    6
    2
    4
    7
    1
    10 25
    2 10
    15 15
    250
    80
    100
    40
    """
    N, M, R, cows, stores, rentals = parse_input(input_str)
    print(N, M, R, cows, stores, rentals)
    print(solve())

    # testing
