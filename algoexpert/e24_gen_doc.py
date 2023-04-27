from collections import defaultdict

def gen_dict(s):
    result = defaultdict(int)
    for c in s:
        result[c] += 1
    return result

def generateDocument(characters, document):
    cdict = gen_dict(characters)
    ddict = gen_dict(document)

    for c in ddict:
        if c in cdict and cdict[c] >= ddict[c]:
            continue
        else:
            return False

    return True

chars = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

print(generateDocument(chars, document))
