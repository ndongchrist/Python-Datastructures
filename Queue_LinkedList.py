  #Queue using the linked List
class Node:
    def __init__(self, nodeValue):
        self.nodeValue = nodeValue
        self.next = None

    def __str__(self) -> str:
        return str(self.nodeValue)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return " ".join(values)

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False 

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            first = self.linkedlist.head.nodeValue
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return first
        
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.linkedlist.head.nodeValue
        
    def delete(self):
        self.linkedlist.tail,self.linkedlist.head = None, None

Q1 = Queue()
Q1.enqueue(4)
Q1.enqueue(3)
Q1.enqueue(2)
Q1.enqueue(1)
print(Q1.dequeue())
print(Q1.peek())

print(Q1)