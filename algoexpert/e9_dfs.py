# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)

        return array

def test_case_1():
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")
    return graph

graph = test_case_1()
print(graph.depthFirstSearch([]))
# ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
