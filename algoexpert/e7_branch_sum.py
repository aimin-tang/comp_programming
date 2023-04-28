class BT:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def helper(node, psum, result):
    if not node:
        return

    csum = psum + node.value

    helper(node.left, csum, result)

    if not node.left and not node.right:
        result.append(csum)

    helper(node.right, csum, result)

def branchSums(node):
    result = []
    helper(node, 0, result)
    return result

#  tree =   1
#         /   \
#        2     3 
#       / \    / \
#      4   5  6   7
#     / \  /
#    8   9 10   

def test_case_1():
    root = BT(1)
    root.left = BT(2)
    root.left.left = BT(4)
    root.left.left.left = BT(8)
    root.left.left.right = BT(9)
    root.left.right = BT(5)
    root.left.right.left = BT(10)
    root.right = BT(3)
    root.right.left = BT(6)
    root.right.right = BT(7)

    return root

root = test_case_1()
print(branchSums(root))
# for each leaf node, a branch sum is appended.
# eg: 15 from 1 -> 2 -> 4 -> 8
# [15, 16, 18, 10, 11]
