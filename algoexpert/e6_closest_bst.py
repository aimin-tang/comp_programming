import math

def get_best(v1, v2, key):
    if abs(v1 - key) > abs(v2 - key):
        return v2
    else:
        return v1

def solve_helper(node, key, best):
    if not node:
        return best

    best = get_best(node.value, best, key)
    curr = node.value

    if curr > key:
        return solve_helper(node.left, key, best)
    elif curr < key:
        return solve_helper(node.right, key, best)
    else:
        return key

def solve(node, key):
    return solve_helper(node, key, math.inf)

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
    
#  tree =  10
#         /   \
#        5     15
#       / \    / \
#      2   5  13  22
#     /        \
#    1         14

root = test_case_1()
print(solve(root, 12))
# 13