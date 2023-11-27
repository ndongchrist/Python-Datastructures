from Queue_LinkedList import Queue 

class AvlNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def pretraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    pretraversal(rootNode.left)
    pretraversal(rootNode.right)

def in_traversal(rootNode):
    if rootNode is None:
        return
    pretraversal(rootNode.left)
    print(rootNode.data)
    pretraversal(rootNode.right)

def in_traversal(rootNode):
    if rootNode is None:
        return
    pretraversal(rootNode.left)
    pretraversal(rootNode.right)
    print(rootNode.data)

def levelOrder(rootNode, value):
    if rootNode is None:
        return "Not an AVL Tree"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.data)
            if root.left is not None:
                customQueue.enqueue(root.left)
            elif root.right is not None:
                customQueue.enqueue(root.right)

def search(rootNode, value):
    if rootNode.data == value:
        return "Found"
    elif rootNode.data > value:
        if rootNode.left.data == value:
            return "Found"
        else: 
            search(rootNode.left, value)
    else:
        if rootNode.right.data == value:
            return "Found"
        else:
            search(rootNode.right, value)

AVLRoot = AvlNode(4)
v1 = AvlNode(6)
v2 = AvlNode(5)
AVLRoot.left = v1
AVLRoot.right = v2

print(search(AVLRoot, 9))



