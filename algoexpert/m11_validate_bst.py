import math


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def helper(node, minval, maxval):
    if node.value < minval or node.value >= maxval:
        return False

    if node.left and node.right:
        return helper(node.left, minval, node.value) and \
               helper(node.right, node.value, maxval)
    elif node.left:
        return helper(node.left, minval, node.value)
    elif node.right:
        return helper(node.right, node.value, maxval)
    else:
        return True


def validateBst(tree):
    # Write your code here.
    return helper(tree, -math.inf, math.inf)
