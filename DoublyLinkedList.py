class Node:
    def __init__(self, nodeValue):
        self.nodeValue = nodeValue
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        newNode = Node(value)
        newNode.next = None
        newNode.prev = None
        self.head = newNode
        self.tail = newNode

    #inserting an element at the end of the linkedList
    def insertAtEnd(self, value):
        newNode = Node(value)
        newNode.next = None
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
    
    #inserting an element at the beginnning of the linkedList
    def insertAtStart(self, value):
        newNode = Node(value)
        newNode.prev = None
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
    
    #inserting in between 02 nodes
    def middle(self, value, position):
        newNode = Node(value)
        if self.head == None:
            print("Linked List doesn't exist")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.nodeValue == position:
                    newNode.next = current_node.next
                    newNode.prev = current_node
                    current_node.next.prev = newNode
                    current_node.next = newNode

                else:
                    print('Not Found')
                current_node = current_node.next


DoublyLinkedL = DLinkedList()
DoublyLinkedL.createDLL(5)
DoublyLinkedL.insertAtEnd(4)
DoublyLinkedL.insertAtStart(3)
DoublyLinkedL.middle(2, 5)
DoublyLinkedL.middle(5, 5)
print([node.nodeValue for node in DoublyLinkedL])
