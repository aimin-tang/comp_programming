class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def insert_node(root, new_node):
    curr_node = root
    while True:
        if curr_node.value > new_node.value:
            if curr_node.left:
                curr_node = curr_node.left
            else:
                curr_node.left = new_node
                break
        else:
            if curr_node.right:
                curr_node = curr_node.right
            else:
                curr_node.right = new_node
                break


def reconstructBst(preOrderTraversalValues):
    if not len(preOrderTraversalValues):
        return None

    root = BST(preOrderTraversalValues[0])
    for idx in range(1, len(preOrderTraversalValues)):
        new_node = BST(preOrderTraversalValues[idx])
        insert_node(root, new_node)

    return root
