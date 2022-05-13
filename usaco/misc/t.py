class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def dfs(node, level):
    if node.left:
        l = dfs(node.left, level + 1)
    else:
        l = level

    if node.right:
        r = dfs(node.right, level + 1)
    else:
        r = level

    return max(l, r)


def height(root):
    return dfs(root, 0)
