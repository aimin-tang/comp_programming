class BT:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def helper(node, my_level):
    if not node:
        return 0

    return helper(node.left, my_level + 1) + helper(node.right, my_level + 1) + my_level
    
def solve(node):
    return helper(node, 0)

#  tree =   1
#         /   \
#        2     3 
#       / \    / \
#      4   5  6   7
#     / \  
#    8   9  

def test_case_1():
    root = BT(1)
    root.left = BT(2)
    root.left.left = BT(4)
    root.left.left.left = BT(8)
    root.left.left.right = BT(9)
    root.left.right = BT(5)
    root.right = BT(3)
    root.right.left = BT(6)
    root.right.right = BT(7)

    return root

root = test_case_1()
print(solve(root))
# top is 0. result is 0 (for 1) + 1 * 2 (for 2, 3) + 2 * 4  (for 4, 5, 6, 7) \
# + 3 * 2 (for 8, 9)
# 16
