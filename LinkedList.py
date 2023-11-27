# A linked list is a form of sequential selection
#and doesn't have to follow an order

#Types of Linked List
# 1 - Singly Linked List
# 2 - Double Linked List (Music App)
# 3 - Circular Linked List (Implementing player turns in a game)
# 4 - Circular Doubled Linked List(Alt + Tab on w)

#elements in a liknked list are not allocated contigously

#Creating a singly linked List
#1 - Create Head and Tail, initialise to null
#2 - Create a blank node
#3 - Link Head and Tail with these Node

#2
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

#1 
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    #inserting elements in a linked List
    def insertSLL(self, value, location):
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                  newNode.next = None
                  self.tail.next = newNode
                  self.tail = newNode
            else:
                 tempNode = self.head
                 index = 0
                 while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                 nextNode = tempNode.next
                 tempNode.next = newNode
                 newNode.next = nextNode

#traverse s singly linked List
    def traverseSSL(self):
        if self.head is None:
            print("Print singly linked list doesn't exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

#serahing a node in a linkedList
    def searchInSSL(self, value):
        if self.head is None:
            print("linked list doesn't exist")
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    print("Found")
                    return node.value
                else:
                    print("Not Found")
                node = node.next


Linked_list = SLinkedList()
Linked_list.insertSLL(1, 1)
Linked_list.insertSLL(2, 1)
Linked_list.insertSLL(3, 1)
Linked_list.insertSLL(4, 1)

Linked_list.insertSLL(0, 0)
Linked_list.insertSLL(10, 3)


print(SLinkedList.searchInSSL(2))
print([node.value for node in Linked_list])
# SLinkedList.traverseSSL()

