class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def get_ancestors(child):
    result = [child]

    curr_node = child
    while curr_node.ancestor:
        curr_node = curr_node.ancestor
        result.append(curr_node)

    return result


def get_common(ancestors1, ancestors2):
    ancestors1 = list(reversed(ancestors1))
    ancestors2 = list(reversed(ancestors2))

    result = None
    idx = 0
    while idx < min(len(ancestors1), len(ancestors2)):
        if ancestors1[idx] == ancestors2[idx]:
            result = ancestors1[idx]
            idx += 1
        else:
            break
    return result


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    ancestors1 = get_ancestors(descendantOne)
    ancestors2 = get_ancestors(descendantTwo)

    result = get_common(ancestors1, ancestors2)
    return result

a = AncestralTree('A')
b = AncestralTree('B')
b.ancestor = a
c = AncestralTree('C')
c.ancestor = a

print(getYoungestCommonAncestor(a, b, c))
