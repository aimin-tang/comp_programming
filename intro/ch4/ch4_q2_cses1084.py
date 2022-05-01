def solve(n, m, k, apartments, applicants):
    apartments = sorted(apartments)
    applicants = sorted(applicants)
    # apartments: [45, 60, 60, 80]
    # applicants: [30, 60, 75]

    apartment = apartments.pop()
    applicant = applicants.pop()
    result = 0
    while len(applicants) > 0 and len(apartments) > 0:
        if apartment - 5 <= applicant <= apartment + 5:
            result += 1
            apartment = apartments.pop()
            applicant = applicants.pop()
        elif apartment - 5 > applicant:
            apartment = apartments.pop()
        else:
            applicant = applicants.pop()

    return result


n, m, k = 4, 3, 5
applicants = [60, 45, 80, 60]
apartments = [30, 60, 75]

print(solve(n, m, k, apartments, applicants))