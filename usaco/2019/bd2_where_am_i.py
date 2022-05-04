def is_good(mailboxes, i):
    result = []
    for start in range(len(mailboxes) - i + 1):
        new_word = mailboxes[start:start + i]
        if new_word in result:
            return False
        else:
            result.append(new_word)

    return True


def solve(mailboxes):
    for i in range(1, len(mailboxes) + 1):
        if is_good(mailboxes, i):
            return i


mailboxes = "ABCDABC"
print(solve(mailboxes))
