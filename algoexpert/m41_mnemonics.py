def get_letters(num):
    d = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    return d[num]

def append_01(partial_result, num, results):
    result = partial_result + num
    results.append(result)

def append_other(partial_result, num, results):
    for l in get_letters(num):
        result = partial_result + l
        results.append(result)

def phoneNumberMnemonics(phoneNumber):
    if len(phoneNumber) == 0:
        return ['']

    partial_results = phoneNumberMnemonics(phoneNumber[:-1])
    results = []
    for partial_result in partial_results:
        num = phoneNumber[-1]
        if num in ['0', '1']:
            append_01(partial_result, num, results)
        else:
            append_other(partial_result, num, results)

    return [''.join(l) for l in results]

print(phoneNumberMnemonics('1905'))
