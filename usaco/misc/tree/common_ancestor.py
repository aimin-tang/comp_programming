class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def dfs(node, v1, v2):
    # return (False, False, None)
    #         v1     v2     node
    if not node:
        return (False, False, None)

    l = dfs(node.left, v1, v2)
    if l[2]:
        return l
    r = dfs(node.right, v1, v2)
    if r[2]:
        return r

    nv1 = node.info == v1
    nv2 = node.info == v2

    v1_seen = l[0] or r[0] or nv1
    v2_seen = l[1] or r[1] or nv2

    if v1_seen and v2_seen:
        return (True, True, node)
    return (v1_seen, v2_seen, None)


def lca(root, v1, v2):
    # Enter your code here
    found = [False, False]
    result = dfs(root, v1, v2)
    # print(result)

    return result[2]


tree = BinarySearchTree()
t = 6

arr = [4, 2, 3, 1, 7, 6]

for i in range(t):
    tree.create(arr[i])

v = [1, 7]

ans = lca(tree.root, v[0], v[1])
print(ans.info)
