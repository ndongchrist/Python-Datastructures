class Queue:
    def __init__(self, maxSize=None):
        # self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return " ".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def enqueue(self, element):
        self.list.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list[0]
        
    def delete(self):
        self.list = None

customQueue = Queue()
customQueue.enqueue(5)
customQueue.enqueue(9)
customQueue.enqueue(3)
customQueue.enqueue(1)
customQueue.enqueue(1)
customQueue.dequeue()
print(customQueue.peek())