# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self

    def contains(self, value):
        # Write your code here.
        if self.value == value:
            return True
        if value < self.value and self.left and self.left.contains(value):
            return True
        if value >= self.value and self.right and self.right.contains(value):
            return True
        return False

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        node, parent, side = self.get_node(value)
        if node.left and node.right:
            

        elif node.left:
            if side == 'left':
                parent.left = node.left
            else:
                parent.right = node.left
        elif node.right:
            if side == 'left':
                parent.left = node.right
            else:
                parent.right = node.right
        else:
            if side == 'left':
                parent.left = None
            else:
                parent.right = None

        return self
