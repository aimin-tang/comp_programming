import itertools


def parse_input(input_str):
    lines = input_str.strip().split('\n')
    num = int(lines[0].strip())

    boards = []
    for i in range(num):
        line = lines[i + 1]
        word1, word2 = line.strip().split()
        boards.append((word1, word2))

    return num, boards


def get_words(boards, product):
    words = []
    for i in range(len(product)):
        board = boards[i]
        side = product[i]
        words.append(board[side])

    return words


def get_letter_index(letter):
    letters = 'abcdefghijklmnopqrstuvwxyz'

    return letters.index(letter)


def get_letter_l_from_words(words):
    letter_l = [0] * 26

    for word in words:
        for letter in word:
            letter_l[get_letter_index(letter)] += 1

    return letter_l


def update_letter_l(old_letter_l, new_letter_l):
    result = []
    for i in range(26):
        result.append(max(old_letter_l[i], new_letter_l[i]))

    return result


if __name__ == '__main__':
    input_str = """
    3
    fox box
    dog cat
    car bus
    """
    num, boards = parse_input(input_str)
    old_letter_l = [0] * 26
    for product in itertools.product((0, 1), repeat=num):
        words = get_words(boards, product)
        new_letter_l = get_letter_l_from_words(words)
        old_letter_l = update_letter_l(old_letter_l, new_letter_l)

    print('\n'.join(map(str, old_letter_l)))

# get sides: itertools.product((0, 1), repeat=num)
