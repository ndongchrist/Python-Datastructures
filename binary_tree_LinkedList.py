#Binary Tree using a linked list
import Queue_LinkedList as Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

newBT = TreeNode('Drinks')
hot = TreeNode('hot')
cold = TreeNode('Cold')
tea = TreeNode('tea')
newBT.left = hot
newBT.right = cold
hot.left = tea

def preorderTrav(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preorderTrav(rootNode.left)
    preorderTrav(rootNode.right)

def inoderTrav(rootNode):
    if not rootNode:
        return
    inoderTrav(rootNode.left)
    print(rootNode.data)
    inoderTrav(rootNode.right)

def postorderTrav(rootNode):
    if not rootNode:
        return
    inoderTrav(rootNode.right)
    inoderTrav(rootNode.left)
    print(rootNode.data)
    

def levelOrderTraversal(rootNode):
    if not rootNode:
        return "Not a LinkedList"
    else: 
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.data)
            if (root.left is not None):
                customQueue.enqueue(root.left)
            if (root.right is not None):
                customQueue.enqueue(root.right)

def searchBT(rootNode, Value):
    if not rootNode:
        return "Not a Binary Tree"
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.data == Value:
                return "Success - Value Found"

            if (root.right is not None):
                customQueue.enqueue(root.right)

            if (root.left is not None):
                customQueue.enqueue(root.left)
        return "Not Found"
    

def insertANode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()

            if root.left is not None:
                customQueue.enqueue(root.left)
            else:
                root.left = newNode
                return "successfully Inserted"
            if root.right is not None:
                customQueue.enqueue(root.right)
            else:
                root.right = newNode
                return "successfully Inserted"


new = TreeNode("Aanas")
insertANode(newBT, new)
levelOrderTraversal(newBT)


# inoderTrav(newBT)
# levelOrderTraversal(newBT)
print(searchBT(newBT, 'te'))