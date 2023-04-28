class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes

def removeDuplicatesFromLinkedList(ll):
    curr_node = ll
    next_node = ll.next
    while next_node:
        if next_node.value == curr_node.value:
            next_node = next_node.next
            curr_node.next = next_node
        else:
            curr_node = next_node
            next_node = next_node.next

def print_nodes(ll):
    result = []
    curr_node = ll
    while curr_node:
        result.append(curr_node.value)
        curr_node = curr_node.next

    return result

test = LinkedList(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
removeDuplicatesFromLinkedList(test)
print(print_nodes(test))
# 1, 3, 4, 5, 6
# mistake: while vs vhile not
