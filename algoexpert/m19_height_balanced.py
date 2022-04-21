class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def helper(node):
    # return depth, max_diff
    if not node:
        return 0, 0

    l_depth, l_max_diff = helper(node.left)
    r_depth, r_max_diff = helper(node.right)
    depth = max(l_depth, r_depth) + 1
    max_diff = max(l_max_diff, r_max_diff, abs(l_depth - r_depth))
    return depth, max_diff


def heightBalancedBinaryTree(tree):
    # Write your code here.
    return helper(tree)[1] <= 1


n1 = BinaryTree(1)
n2 = BinaryTree(2)
n3 = BinaryTree(3)
n4 = BinaryTree(4)
n5 = BinaryTree(5)
n6 = BinaryTree(6)
n7 = BinaryTree(7)
n8 = BinaryTree(8)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
n5.left = n7
n5.right = n8
tree = n1
print(heightBalancedBinaryTree(tree))
