def solve(t, books):
    best = 0
    curr_total = 0

    lptr, rptr = 0, 0
    while lptr < len(books):
        while rptr < len(books):
            if curr_total + books[rptr] < t:
                curr_total += books[rptr]
                rptr += 1
            else:
                break
        best = max(best, rptr - lptr)
        curr_total -= books[lptr]
        lptr += 1

    return best


t = 5
books = [3, 1, 2, 1]
t = 3
books = [2, 2, 3]
print(solve(t, books))