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


from collections import defaultdict

def bfs(root, result_d):
    visited = [root]
    q = [(root, 0)]
    result_d[0].append(root.info)

    while q:
        node, pos = q.pop(0)
        if node.left and node.left not in visited:
            visited.append(node.left)
            q.append((node.left, pos - 1))
            result_d[pos - 1].append(node.left.info)
        if node.right and node.right not in visited:
            visited.append(node.right)
            q.append((node.right, pos + 1))
            result_d[pos + 1].append(node.right.info)


def topView(root):
    # Write your code here
    result_d = defaultdict(list)
    bfs(root, result_d)

    pos_l = sorted(result_d.keys())
    top_view = []
    for pos in pos_l:
        top_view.append(result_d[pos][0])

    print(' '.join([str(n) for n in top_view]))

bst = BinarySearchTree()
s = '37 23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 ' + \
    '104 98 81 90 68 40 103 77 74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 ' + \
    '84 34 88 27 72 32 62 9 56 109 115 33 15 91 29 85 114 112 20 26 30 93 ' + \
    '96 87 42 38 60 7 73 35 12 10 57 80 13 52 44 16 70 8 39 107 106 63 24 ' +\
    '92 45 75 116 5 61 49 101 71 11 53 43 102 110 1 58 36 28 76 47 113 21 ' +\
    '89 51 19 3'
s = '1 2 5 3 6 4'
# s = '37 23 108 59 86 64 94 14 105 17 111'
# s = '37 23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 '

for num in s.split():
    bst.create(int(num))

topView(bst.root)