from collections import defaultdict


def tournamentWinner(competitions, results):
    scores = defaultdict(int)
    for idx, (t1, t2) in enumerate(competitions):
        if results[idx]:
            scores[t1] += 1
        else:
            scores[t2] += 1

    max_score = max(scores.values())
    winners = list(filter(lambda k: scores[k] == max_score,
                          scores.keys()))

    if len(winners) == 1:
        return winners[0]
    elif len(winners) == 2:
        t1, t2 = winners[0], winners[1]
        i = competitions.index([t1, t2])
        if i == -1:
            i = competitions.index([t2, t1])
        if results[i]:
            return competitions[i][1]
        else:
            return competitions[i][0]
    else:
        raise RuntimeError('too many winners, no rule here to judge')


competitions = [
    ['html', 'c#'],
    ['c#', 'python'],
    ['python', 'html']
]
results = [0, 0, 1]

print(tournamentWinner(competitions, results))