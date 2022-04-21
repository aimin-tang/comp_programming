# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def helper(node):
    # return depth, biggest
    if not node:
        return 0, 0

    l_depth, l_biggest = helper(node.left)
    r_depth, r_biggest = helper(node.right)
    depth = max(l_depth, r_depth) + 1
    biggest = max(l_biggest, r_biggest, l_depth + r_depth)
    return depth, biggest

def binaryTreeDiameter(tree):
    return helper(tree)[1]
