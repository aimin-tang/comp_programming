from collections import defaultdict


def parse_words(f_name):
    with open(f_name) as f:
        lines = f.readlines()

    result1 = defaultdict(int)
    for line in lines:
        line_words = line.strip().split()
        for word in line_words:
            if word.endswith('.'):
                word = word[:-1]
            word = word.lower()
            result1[word] += 1

    count_to_word_d = defaultdict(list)
    # {4: ['good'], 3: ['a', 'day']}

    for word, count in result1.items():
        count_to_word_d[count].append(list)

    result2 = []
    l1 = list(reversed(sorted(count_to_word_d.keys())))
    # l1: [4, 3, 3, 2]

    for l1_idx in range(len(l1)):
        to_extend = count_to_word_d[l1[l1_idx]]
        result2.extend(to_extend)

    return result2[:10]