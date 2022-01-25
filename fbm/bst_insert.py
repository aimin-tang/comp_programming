class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


def in_order(root):
    if root.left:
        in_order(root.left)
    print(root.info, end=' ')
    if root.right:
        in_order(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        # Enter you code here.
        if not self.root:
            self.root = Node(val)
            self.root.level = 0
            return

        curr_node = self.root

        while curr_node:
            if val <= curr_node.info:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = Node(val)
                    curr_node.left.level = curr_node.level + 1
                    break
            else:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = Node(val)
                    curr_node.right.level = curr_node.level + 1
                    break


tree = BinarySearchTree()
tree.insert(4)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(3)

# preOrder(tree.root)
in_order(tree.root)