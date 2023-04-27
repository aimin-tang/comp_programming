def better_num(n1, n2, target):
    if abs(n1 - target) < abs(n2 - target):
        return n1
    return n2


def solve(tree, target):
    if tree.value == target:
        return target

    best = tree.value

    if tree.left and target < tree.value:
        l = solve(tree.left, target)
        best = better_num(l, best, target)
    if tree.right and target > tree.value:
        r = solve(tree.right, target)
        best = better_num(r, best, target)

    return best


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def test_case_1():
    root = BST(10)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.right = BST(5)
    root.right = BST(15)
    root.right.left = BST(13)
    root.right.left.right = BST(14)
    root.right.right = BST(22)

    return root

root = test_case_1()
print(solve(root, 12))
