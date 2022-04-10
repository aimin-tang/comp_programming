class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_left(array, node_idx, end_idx):
    if array[node_idx + 1] > array[node_idx]:
        return None
    else:
        return node_idx + 1


def get_right(array, node_idx, end_idx):
    curr_idx = node_idx + 1

    while curr_idx <= end_idx:
        if array[curr_idx] >= array[node_idx]:
            return curr_idx
        else:
            curr_idx += 1

    return None


def helper(array, node_idx, end_idx):
    bst = BST(array[node_idx])

    if end_idx <= node_idx:
        return bst

    l = get_left(array, node_idx, end_idx)
    r = get_right(array, node_idx, end_idx)
    if l and r:
        bst.left = helper(array, l, r - 1)
        bst.right = helper(array, r, end_idx)
    elif l:
        bst.left = helper(array, l, end_idx)
    elif r:
        bst.right = helper(array, r, end_idx)
    else:
        pass

    return bst


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    # return helper(preOrderTraversalValues, 0, len(preOrderTraversalValues) - 1)

# preOrderTraversalValues = [10, 4, 2, 1, 3, 17, 19, 18]
preOrderTraversalValues = [2, 0, 1, 4, 3, 3]
r = reconstructBst(preOrderTraversalValues)
print(r)
