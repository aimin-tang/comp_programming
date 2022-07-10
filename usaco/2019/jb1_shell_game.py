def parse_input(input_lines):
    lines = input_lines.strip().split('\n')
    N = int(lines[0].strip())
    games = []
    for i in range(1, N+1):
        games.append(list(map(int, lines[i].strip().split())))

    return N, games

def play_one_game(pebble_at, game):
    if pebble_at == game[0]:
        pebble_at = game[1]
    elif pebble_at == game[1]:
        pebble_at = game[0]
    
    if game[2] == pebble_at:
        return True, pebble_at
    else:
        return False, pebble_at

def play_N_games(pebble_at, games):
    result = 0
    for game in games:
        win, pebble_at = play_one_game(pebble_at, game)
        if win:
            result += 1

    return result

input_lines = """
3
1 2 1
3 2 1
1 3 1
"""

N, games = parse_input(input_lines)
result = 0
for pebble_at in range(1, 4):
    one_result = play_N_games(pebble_at, games)
    if one_result > result:
        result = one_result

print(result)
