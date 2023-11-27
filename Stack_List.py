#Stacks using List

class Stack:
    def __init__(self):
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
#Stack operations
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self, value):
        self.list.append(value)
        return "Element successfully inserted"
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list[-1]
        
    def delete(self):
        self.list = None
        

customStack = Stack()
customStack.push(5)
customStack.push(5)
customStack.push(5)
customStack.pop()
customStack.peek()
print(customStack )