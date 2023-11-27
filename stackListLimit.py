class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isFull(self):
        if self.maxSize == len(self.list):
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.list is []:
            return True
        else:
            return False
    
    def push(self, value):
        if self.isFull():
            return "Stack is Full"
        else:
            self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "This Stack is Empty"
        else:
            self.list.pop()

customStack = Stack(3)
customStack.push(4)
customStack.push(5)
customStack.push(2)
# customStack.pop()
print(customStack.push(5))