def solve(essay, K):
    result = []
    essay_l = essay.strip().split()
    curr_line = []
    curr_count = 0

    for word in essay_l:
        if curr_count + len(word) <= K:
            curr_line.append(word)
            curr_count += len(word)
        else:
            result.append(' '.join(curr_line))
            curr_line = [word]
            curr_count = len(word)

    result.append(''.join(curr_line))

    return '\n'.join(result)


essay = "hello my name is Bessie and this is my essay"
K = 7
print(solve(essay, K))
