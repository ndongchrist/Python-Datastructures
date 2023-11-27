class Queue:
    def __init__(self, maxSize) -> None:
        self.maxSize = maxSize
        self.list = [None]*maxSize
        self.top = -1
        self.start = -1

    def __str__(self) -> str:
        values = [str(x) for x in self.list]
        return " ".join(values)
    
    def isFull(self):
        if self.top + 1  == self.maxSize and self.start == 0:
            return True
        elif self.top + 1 == self.start:
            return False
        else:
            return False
        
    def isEmpty(self):
        if self.start == -1:
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.isFull():
            return "Queue is Full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.list[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            firstElement = self.list[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 ==self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.list[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.list[self.start]
        
    def delete(self):
        self.list = [None] * self.maxSize
        self.start = -1
        self.top = -1

            
customQ = Queue(4)
customQ.enqueue(5)
customQ.enqueue(6)
print(customQ)