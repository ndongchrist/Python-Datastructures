#creating a  stack using a linked List

class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:
    def __init__(self):
       self.LList = LinkedList()

    def __str__(self) -> str:
        values = [str(x.value) for x in self.LList]
        return '\n'.join(values)
    
    

    def isEmpty(self):
        if self.LList.head is None:
            return True
        else:
            return False

    def push(self, value):
        newnode = Node(value)
        newnode.next = self.LList.head
        self.LList.head = newnode

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodeValue = self.LList.head.value
            self.LList.head = self.LList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodeValue = self.LList.head.value
            return nodeValue
        
    def delete(self):
        self.LList.head = None
        
stk = Stack()
stk.push(5)
stk.push(7)
stk.push(9)
stk.pop()
stk.delete()
print(stk)