#circular singly linked List

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class CSLList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

node1 = Node(4)

Clist = CSLList()
Clist.head = node1
Clist.tail = node1
node1.next = node1

print([node1.value for node in Clist])

