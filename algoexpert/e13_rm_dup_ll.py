class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    if not linkedList.next:
        # only 1 node
        return linkedList

    curr_node = linkedList
    next_node = linkedList.next

    while next_node:
        if curr_node.value == next_node.value:
            next_node = next_node.next
            curr_node.next = next_node
        else:
            curr_node = next_node
            next_node = next_node.next

    return linkedList
