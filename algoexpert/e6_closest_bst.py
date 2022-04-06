def better_num(n1, n2, target):
    if abs(n1 - target) < abs(n2 - target):
        return n1
    return n2


def findClosestValueInBst(tree, target):
    if tree.value == target:
        return target

    best = tree.value

    if tree.left and target < tree.value:
        l = findClosestValueInBst(tree.left, target)
        best = better_num(l, best, target)
    if tree.right and target > tree.value:
        r = findClosestValueInBst(tree.right, target)
        best = better_num(r, best, target)

    return best


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
