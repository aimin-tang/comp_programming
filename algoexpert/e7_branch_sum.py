class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(node, psum, result):
    if not node:
        return

    if not node.left and not node.right:
        result.append(psum + node.value)

    dfs(node.left, psum+node.value, result)
    dfs(node.right, psum+node.value, result)


def branchSums(root):
    result = []
    dfs(root, 0, result)
    return result
