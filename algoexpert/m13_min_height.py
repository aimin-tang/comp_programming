def build_bst(array, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    node = BST(array[mid])
    node.left = build_bst(array, start, mid - 1)
    node.right = build_bst(array, mid + 1, end)

    return node


def minHeightBst(array):
    return build_bst(array, 0, len(array) - 1)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
