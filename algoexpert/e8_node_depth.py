def helper(node, level):
    result = level
    if node.left:
        result += helper(node.left, level+1)
    if node.right:
        result += helper(node.right, level+1)

    return result

def nodeDepths(root):
    return helper(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
