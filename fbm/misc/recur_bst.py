class newNode:

    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

    def insert(self, val):
        if val <= self.key:
            if self.left:
                self.left.insert(val)
            else:
                self.left = newNode(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = newNode(val)

    def contains(self, val):
        if self.key == val:
            return True
        elif val < self.key:
            if self.left:
                return self.left.contains(val)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(val)
            else:
                return False

    def in_order(self):
        if self.left:
            self.left.in_order()

        print(self.key, end=' ')

        if self.right:
            self.right.in_order()

    def pre_order(self):
        print(self.key, end=' ')

        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def post_order(self):
        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()

        print(self.key, end=' ')



# Driver Code
if __name__ == '__main__':
    """ Let us create following BST
           50
           / \
        30     70
        / \   / \
       20 40 60 80 """

    root = newNode(50)
    root.insert(30)
    root.insert(20)
    root.insert(40)
    root.insert(70)
    root.insert(60)
    root.insert(80)

    # inorder traversal of the BST
    print()
    print(root.contains(20))
    print(root.contains(51))

    root.in_order()
    print()
    root.pre_order()
    print()
    root.post_order()
