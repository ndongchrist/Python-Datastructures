#creating a binary search tree(linked list)
class BSTNode:
    def __init__(self, data) -> None:
        self.data  = data
        self.left = None
        self.right = None

def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
            rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
            if rootNode.left is None:
                rootNode.left = BSTNode(nodeValue)
            else:
                insertNode(rootNode.left, nodeValue)

    else:
        if rootNode.right is None:
            rootNode.right = BSTNode(nodeValue)
        else:
            insertNode(rootNode.right, nodeValue)
    return 'Node Successfully inserted'

def pretraversal(rootNode):
     if rootNode is None:
          return 
     print(rootNode.data)
     pretraversal(rootNode.left)
     pretraversal(rootNode.right) 

def intraversal(rootNode):
     if rootNode is None:
          return 
     intraversal(rootNode.left)
     print(rootNode.data)
     intraversal(rootNode.right) 

def posttraversal(rootNode):
     if rootNode is None:
          return "Not a BST"
     posttraversal(rootNode.left)
     posttraversal(rootNode.right)
     print(rootNode.data)

def search(rootNode, value):
     if rootNode is None:
          return "Not a BST"
     elif rootNode.data == value:
          return f'{rootNode.data} found'
     elif rootNode.data > value:
          if rootNode.left.data == value:
               return "Found on the left"
          else:
               search(rootNode.left.data, value)
     else:
          if rootNode.right.data == value:
               return 'Found on the right'
          else:
               search(rootNode.right.data, value)

             

newBST = BSTNode(60)
insertNode(newBST,50)
insertNode(newBST, 90)
print(search(newBST, 60))
