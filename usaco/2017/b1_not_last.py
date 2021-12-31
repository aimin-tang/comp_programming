def parse_input(input_str):
    lines = input_str.strip().split('\n')
    N = int(lines[0])
    entries = []
    for i in range(1, N+1):
        cow, milk = lines[i].strip().split()
        milk = int(milk)
        entries.append((cow, milk))

    return N, entries

def get_total_milk():
    total_milk = {}
    for name in names:
        total_milk[name] = 0

    for entry in entries:
        name, milk = entry
        total_milk[name] += milk

    return total_milk

def gen_output(total_milk):
    milk_to_cow_d = {}
    for k, v in total_milk.items():
        if v in milk_to_cow_d:
            milk_to_cow_d[v].append(k)
        else:
            milk_to_cow_d[v] = [k]

    milk_set = set(milk_to_cow_d.keys())

    if len(milk_set) == 1:
        return 'Tie'

    not_last_milk = sorted(list(milk_set))[1]
    if len(milk_to_cow_d[not_last_milk]) > 1:
        return 'Tie'

    return milk_to_cow_d[not_last_milk]

if __name__ == '__main__':
    input_str = """
    10
    Bessie 1
    Maggie 13
    Elsie 3
    Elsie 4
    Henrietta 4
    Gertie 12
    Daisy 7
    Annabelle 10
    Bessie 6
    Henrietta 5
    """
    N, entries = parse_input(input_str)
    names = 'Bessie Elsie Daisy Gertie Annabelle Maggie Henrietta'.split()
    total_milk = get_total_milk()
    print(gen_output(total_milk))

    # testing
    # print(parse_input(input_str))
    # print(names)
    # print(get_total_milk())
