class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def traverse_bst(tree, array):
    # in order and fill array
    if tree:
        traverse_bst(tree.left, array)
        array.append(tree.value)
        traverse_bst(tree.right, array)


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    array = []
    traverse_bst(tree, array)
    return array[-k]
